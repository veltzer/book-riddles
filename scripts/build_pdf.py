#!/usr/bin/env python

""" Build docs/riddling.pdf, which GitHub Pages serves from master:/docs.

Invoked by rsconstruct's explicit processor as
    build_pdf.py --inputs <main.tex> <more inputs...> --output-files <out.pdf>
The first input is the document to compile; the rest (the included riddles and
the sketch-generated figures) are only there so a change to them retriggers the
build. pdflatex runs from the repository root, because riddling.tex \\inputs
its parts by root-relative path, and writes its aux/log files into a scratch
directory so nothing lands in the tree.

The build is reproducible: the same sources give a byte-identical PDF
(riddling.tex omits the PDF dates and trailer id). The title page carries no
build time, commit or version, because rsconstruct caches the PDF by the
contents of its inputs alone: anything taken from the clock or from git would
make two builds of the same sources differ, and a cache restore would bring
back whatever stamp the cached copy happened to get. """

import os
import shutil
import subprocess
import sys
import tempfile

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


def main():
    """ main entry point """
    # rsconstruct doctor probes every configured command with --version
    if sys.argv[1:] == ["--version"]:
        print("build_pdf.py 1")
        return
    main_tex, output = parse_args(sys.argv[1:])
    stem = os.path.splitext(os.path.basename(main_tex))[0]
    with tempfile.TemporaryDirectory() as scratch:
        for _ in range(RUNS):
            result = subprocess.run([
                "pdflatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                f"-output-directory={scratch}",
                f"-jobname={stem}",
                main_tex,
            ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
            if result.returncode != 0:
                sys.stderr.write(result.stdout.decode(errors="replace"))
                sys.exit(result.returncode)
        os.makedirs(os.path.dirname(output) or ".", exist_ok=True)
        shutil.copyfile(os.path.join(scratch, f"{stem}.pdf"), output)


if __name__ == "__main__":
    main()
