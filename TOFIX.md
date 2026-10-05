# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/tex/riddling.tex:129` - the book is no longer buildable: it `\input`s `out/src/sk/*.tex` (also `:139`, `:149`), which only the removed pydmt-era Makefile generated from `src/sk/*.sk` via sketch, and `rsconstruct.toml` has no sketch or `pdflatex` processor, so the published `docs/riddling.pdf` is a hand-copied artifact that edits to the `.tex` never reach. Add sketch + `pdflatex` steps (the unused `scripts/wrapper_sketch.py`/`scripts/wrapper_lacheck.py` were written for exactly this) and generate `docs/riddling.pdf` from the build.

## Medium

- `docs/build/pdf.js:126` - the vendored pdf.js viewer served on Pages is version 2.3.41, which is affected by CVE-2024-4367 (arbitrary JavaScript execution when a crafted PDF is opened; fixed in 4.2.67); update the vendored viewer or link the PDF directly.
- `rsconstruct.toml:33` and `rsconstruct.toml:37` - `ruff`/`mypy` scan `src` (TeX/sketch/jpg only) and `config` (Lua only) but not `instances/`, which holds 25 Python files that are therefore never linted; set src_dirs to `["scripts", "instances"]`. (`ruff check instances` today reports one finding: EXE002, `instances/__init__.py` is executable without a shebang - `chmod -x` it.)
- `rsconstruct.toml:82-84` - the comment says `docs/web` (vendored pdf.js) is not linted, but `rsconstruct processor files tidy` shows the only file tidy checks is `docs/web/viewer.html`; the repo's own `docs/index.html` is not checked. Point tidy at the own page and keep the vendored viewer out.
- `rsconstruct.toml:67` - `src_exclude_dirs = ["instances/print_stars"]` is a config-level lint exclusion; the shadowed/unused `i` is the riddle, so mark those lines with inline `// cppcheck-suppress` comments in `instances/print_stars/*.cc` instead and drop the exclude.
- `tera.templates/docs/index.html.tera:36` - the "git clone link" uses `git://github.com/...`; GitHub turned off the unauthenticated git protocol in 2022, so the link is dead; use `https://github.com/.../book-riddles.git`.
- `instances/birthday_problem/solve.py:11` and `instances/birthday_problem/solve.py:20` - draws `randint(0, 365)` (366 days) one billion times into a Python list (tens of GB of RAM), and then counts repeats, which does not compute the birthday-problem probability at all; simulate groups of `n` people and count the fraction with a shared birthday, using `randint(0, 364)`.
- `config/project.lua:5-12` - `DESCRIPTION_LONG` tells users to run `scripts/ubuntu_install.sh` (does not exist) and `make` (the Makefile was removed) and says output goes to `out/`; update to the rsconstruct workflow.

## Low

- `instances/birthday_problem/doit.py:3-5` - docstring says "Birthday problem" but the script measures the expected number of coin flips until the first 1 (a geometric distribution); fix the docstring or move the file.
- `instances/pi_estimation/solution.py:13` and `instances/pi_estimation/solution.py:17` - `samples = 1000000` is never used and the loop is `while True`, so the script never ends; loop `samples` times and print the final estimate.
- `instances/path/Path.java:18` (also `:25`, `:30`, `:35`, `:36`, `:62`, `:66`) - `new Integer(...)` is deprecated for removal; use autoboxing or `Integer.valueOf`.
- `rsconstruct.toml:26-30` - `dep_inputs` repeats exactly the three files already listed in `dep_auto`; delete the duplicate list.
- `doc/TODO.txt:4-5` - item about running htmlhint is obsolete (htmlhint was removed); `doc/TODO.txt:23` refers to a `.htaccess` in `web/` that does not exist; `doc/TODO.txt:42-45` refer to "the makefile" and a perl lacheck wrapper (now a Python one exists); prune.
