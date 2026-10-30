#!/usr/bin/env python

""" Build docs/riddling.pdf, which GitHub Pages serves from master:/docs.

Invoked by rsconstruct's explicit processor as
    build_pdf.py --inputs <main.tex> <more inputs...> --output-files <out.pdf>
The first input is the document to compile; the rest (the included riddles and
the sketch-generated figures) are only there so a change to them retriggers the
build. pdflatex runs from the repository root, because riddling.tex \\inputs
its parts by root-relative path, and writes its aux/log files into a scratch
directory so nothing lands in the tree.

The title page states when the book was built, from which commit, and the
book's version when the repository has a tag. These are passed to LaTeX as
macros (\\buildtime, \\buildcommit, \\buildversion), so they are not inputs:
the PDF says when it was last actually built, and rsconstruct restoring it
from the cache keeps that stamp. """

import datetime
import os
import shutil
import subprocess
import sys
import tempfile

# The build rewrites this tracked file, so it never counts as an uncommitted
# change of the sources.
PDF = "docs/riddling.pdf"

# Three passes: the first writes the .toc, the second typesets the table of
# contents (which pushes every section several pages on), and the third picks
# up the page numbers that move.
RUNS = 3


def parse_args(argv):
    """ Split the --inputs/--output-files argument lists. """
    lists = {"--inputs": [], "--output-files": []}
    current = None
    for arg in argv:
        if arg in lists:
            current = lists[arg]
        elif current is None:
            sys.exit(f"build_pdf.py: unexpected argument [{arg}]")
        else:
            current.append(arg)
    inputs, outputs = lists["--inputs"], lists["--output-files"]
    if not inputs or len(outputs) != 1:
        sys.exit("build_pdf.py: need --inputs <main.tex> ... --output-files <out.pdf>")
    return inputs[0], outputs[0]


def git(*args):
    """ Output of a git command, or None when it fails (no repo, no tags). """
    result = subprocess.run(["git", *args], capture_output=True, text=True, check=False)
    return result.stdout.strip() if result.returncode == 0 else None


def tex_escape(text):
    """ Escape the characters LaTeX treats specially. """
    for char in "\\#$%&_{}":
        text = text.replace(char, "\\" + char)
    return text.replace("~", "\\textasciitilde{}").replace("^", "\\textasciicircum{}")


def build_info():
    """ The \\def's for the build time, commit and version macros. """
    now = datetime.datetime.now().astimezone()
    offset = now.strftime("%z")
    when = now.strftime(f"%Y-%m-%d %H:%M %Z (UTC{offset[:3]}:{offset[3:]})")
    commit = git("rev-parse", "--short", "HEAD") or "unknown"
    if git("status", "--porcelain", "--", ".", f":!{PDF}"):
        commit += " with uncommitted changes"
    # Exactly the tag when HEAD is tagged, otherwise tag-N-gHASH.
    version = git("describe", "--tags") or ""
    return "".join(
        f"\\def\\{name}{{{tex_escape(value)}}}"
        for name, value in (("buildtime", when), ("buildcommit", commit), ("buildversion", version))
    )


def main():
    """ main entry point """
    # rsconstruct doctor probes every configured command with --version
    if sys.argv[1:] == ["--version"]:
        print("build_pdf.py 1")
        return
    main_tex, output = parse_args(sys.argv[1:])
    stem = os.path.splitext(os.path.basename(main_tex))[0]
    # Computed once so all passes typeset the same stamp.
    defs = build_info()
    with tempfile.TemporaryDirectory() as scratch:
        for _ in range(RUNS):
            result = subprocess.run([
                "pdflatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                f"-output-directory={scratch}",
                f"-jobname={stem}",
                f"{defs}\\input{{{main_tex}}}",
            ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
            if result.returncode != 0:
                sys.stderr.write(result.stdout.decode(errors="replace"))
                sys.exit(result.returncode)
        os.makedirs(os.path.dirname(output) or ".", exist_ok=True)
        shutil.copyfile(os.path.join(scratch, f"{stem}.pdf"), output)


if __name__ == "__main__":
    main()
