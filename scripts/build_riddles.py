#!/usr/bin/env python

"""
Write the body of the book: one chapter per category, holding every riddle of
src/include/ whose title names that category.

Each riddle file starts with \\section{Title (Category)}. Chapters come in
alphabetical order and so do the riddles in each chapter, except that a riddle
which builds on another one says so with a comment line

    % follows: <name of the other riddle's file, without .tex>

and is put right after it.

For every riddle the output sets \\riddletitle (riddling.tex makes \\section
print it, since the chapter already names the category) and \\inputs the file.

rsconstruct runs it as an explicit processor:
    build_riddles.py --inputs <riddle.tex>... --output-files <riddles.tex>
"""

import os
import re
import sys

SECTION = re.compile(r"\\section\s*\{(?P<title>.*) \((?P<category>[^()]*)\)\}\s*$")
FOLLOWS = re.compile(r"^%\s*follows:\s*(?P<name>\S+)\s*$", re.MULTILINE)


def parse_args(argv):
    """ Split the --inputs/--output-files argument lists. """
    lists = {"--inputs": [], "--output-files": []}
    current = None
    for arg in argv:
        if arg in lists:
            current = lists[arg]
        elif current is None:
            sys.exit(f"build_riddles.py: unexpected argument [{arg}]")
        else:
            current.append(arg)
    inputs, outputs = lists["--inputs"], lists["--output-files"]
    if not inputs or len(outputs) != 1:
        sys.exit("build_riddles.py: need --inputs <riddle.tex>... --output-files <riddles.tex>")
    return inputs, outputs[0]


def read_riddle(path):
    """ The title, category and follows: name of one riddle file. """
    with open(path, encoding="utf-8") as stream:
        text = stream.read()
    match = SECTION.match(text.split("\n", 1)[0])
    if not match:
        sys.exit(f"{path}:1: a riddle must start with \\section{{Title (Category)}}")
    follows = FOLLOWS.search(text)
    return {
        "path": path,
        "name": os.path.splitext(os.path.basename(path))[0],
        "title": match["title"],
        "category": match["category"],
        "follows": follows["name"] if follows else None,
    }


def sort_key(riddle):
    """ Alphabetical by title, ignoring case and a leading article. """
    return re.sub(r"^(the|a) ", "", riddle["title"].casefold())


def order_chapter(riddles):
    """ The riddles of one chapter, each follower right after what it follows. """
    by_name = {riddle["name"]: riddle for riddle in riddles}
    followers = {}
    for riddle in riddles:
        name = riddle["follows"]
        if name is None:
            continue
        if name not in by_name:
            sys.exit(f"{riddle['path']}: follows [{name}], which is not a riddle of the "
                     f"[{riddle['category']}] chapter")
        followers.setdefault(name, []).append(riddle)
    ordered = []

    def place(riddle):
        ordered.append(riddle)
        for follower in sorted(followers.get(riddle["name"], []), key=sort_key):
            place(follower)

    for riddle in sorted(riddles, key=sort_key):
        if riddle["follows"] is None:
            place(riddle)
    if len(ordered) != len(riddles):
        sys.exit(f"follows: lines form a cycle in the [{riddles[0]['category']}] chapter")
    return ordered


def main():
    """ main entry point """
    # rsconstruct doctor probes every configured command with --version
    if sys.argv[1:] == ["--version"]:
        print("build_riddles.py 1")
        return
    inputs, output = parse_args(sys.argv[1:])
    chapters = {}
    for path in inputs:
        riddle = read_riddle(path)
        chapters.setdefault(riddle["category"], []).append(riddle)
    lines = ["% written by scripts/build_riddles.py from src/include/*.tex"]
    for category in sorted(chapters, key=str.casefold):
        lines.append("")
        lines.append(f"\\chapter{{{category}}}")
        for riddle in order_chapter(chapters[category]):
            lines.append(f"\\renewcommand{{\\riddletitle}}{{{riddle['title']}}}")
            lines.append(f"\\input{{{riddle['path']}}}")
    os.makedirs(os.path.dirname(output), exist_ok=True)
    with open(output, "w", encoding="utf-8") as stream:
        stream.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
