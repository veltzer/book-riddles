#!/usr/bin/env python

"""
This is a wrapper to run the lacheck(1) tool from the "lacheck" package.

Why do we need this wrapper?
- lacheck does NOT report in its exit status whether it had warnings or not.
- it is too verbose when there are no warnings.
- some of its warnings are wrong for this book, see IGNORE below.

rsconstruct runs it as an explicit processor (lacheck follows \\input into the
sketch figures, so it must run after sketch):
    wrapper_lacheck.py --inputs <main.tex> <other inputs>... --output-files <stamp>
It checks the main file, which pulls in all the others, and writes the stamp
file when there are no warnings.
"""

import re
import subprocess
import sys

# (warning, source line) pairs to ignore: a warning is ignored only when its
# text matches the first regex and the line it points at matches the second,
# so the same warning anywhere else still fails the build.
IGNORE = [
    # TikZ \foreach lists are written {0,...,6}; \ldots there breaks the drawing
    (r'Dots should be \\ldots', r'\\foreach'),
    # factorials, as in $101!$
    (r'punctuation mark "!" should be placed after end of math mode', r'\d!|\)!'),
    # the space in "\foreach \x in {", "\hypersetup{" and "\text{ a neighbor of }"
    # is intended
    (r'possible unwanted space at "\{"', r'\\foreach|\\hypersetup\{|\\text\{'),
]

WARNING = re.compile(r'^"(?P<file>[^"]*)", line (?P<line>\d+): (?P<message>.*)$')


def parse_args(argv):
    """ Split the --inputs/--output-files argument lists. """
    lists = {"--inputs": [], "--output-files": []}
    current = None
    for arg in argv:
        if arg in lists:
            current = lists[arg]
        elif current is None:
            sys.exit(f"wrapper_lacheck.py: unexpected argument [{arg}]")
        else:
            current.append(arg)
    inputs, outputs = lists["--inputs"], lists["--output-files"]
    if not inputs or len(outputs) != 1:
        sys.exit("wrapper_lacheck.py: need --inputs <main.tex> ... --output-files <stamp>")
    return inputs[0], outputs[0]


def ignored(file, line, message):
    """ Whether a warning is on the IGNORE list. """
    with open(file, encoding="utf-8") as stream:
        lines = stream.read().split("\n")
    source = lines[line - 1] if 0 < line <= len(lines) else ""
    return any(
        re.search(message_re, message) and re.search(line_re, source)
        for message_re, line_re in IGNORE
    )


def main():
    """ main entry point """
    # rsconstruct doctor probes every configured command with --version
    if sys.argv[1:] == ["--version"]:
        print("wrapper_lacheck.py 1")
        return
    main_tex, stamp = parse_args(sys.argv[1:])
    out = subprocess.check_output(["lacheck", main_tex]).decode()
    errors = False
    for line in out.split("\n"):
        if line.startswith("**") or line == "":
            continue
        match = WARNING.match(line)
        if match and ignored(match["file"], int(match["line"]), match["message"]):
            continue
        errors = True
        print(line)
    if errors:
        sys.exit(1)
    with open(stamp, "w", encoding="utf-8") as stream:
        stream.write("lacheck found no warnings\n")


if __name__ == "__main__":
    main()
