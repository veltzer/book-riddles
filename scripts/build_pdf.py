#!/usr/bin/env python

""" Build docs/riddling.pdf, which GitHub Pages serves from master:/docs.

Invoked by rsconstruct's explicit processor as
    build_pdf.py --inputs <main.tex> <more inputs...> --output-files <out.pdf>
The first input is the document to compile; the rest (the included riddles and
the sketch-generated figures) are only there so a change to them retriggers the
build. pdflatex runs from the repository root, because riddling.tex \\inputs
its parts by root-relative path, and writes its aux/log files into a scratch
directory so nothing lands in the tree.

The title page names the commit the book was built from and that commit's
date, passed to LaTeX as macros (\\buildtime, \\buildcommit). The build is
reproducible: the same sources give a byte-identical PDF. So the stamp holds
nothing that changes between runs of the same sources:
- the commit is the last one that changed anything but the PDF itself, not
  HEAD: committing the PDF moves HEAD, and stamping HEAD would make every
  rebuild after that commit differ;
- the time is that commit's committer date in UTC, not the wall clock or the
  local time zone;
- there is no `git describe` version: CI's release workflow tags a commit
  after building it, so the description of a commit changes after the fact.
With uncommitted changes the commit is marked so, and the PDF is final only
once those changes are committed and the book is built again. """

import datetime as dt
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
    """ The \\def's for the commit and commit date macros. """
    sources = ("--", ".", f":!{PDF}")
    last = git("log", "-1", "--format=%H %ct", *sources)
    if last:
        commit, stamp = last.split()
        commit = commit[:7]
        when = dt.datetime.fromtimestamp(int(stamp), dt.UTC).strftime("%Y-%m-%d %H:%M UTC")
    else:
        commit, when = "unknown", "unknown"
    if git("status", "--porcelain", *sources):
        commit += " with uncommitted changes"
    return "".join(
        f"\\def\\{name}{{{tex_escape(value)}}}"
        for name, value in (("buildtime", when), ("buildcommit", commit))
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
