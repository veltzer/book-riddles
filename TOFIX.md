# TOFIX

Findings from a code scan on 2026-10-04. All resolved on 2026-10-31: the book
is built by rsconstruct, the vendored pdf.js viewer is gone (the site links the
PDF directly), ruff and pyrefly cover `instances/` (which fixed real bugs in
`series/solution_better.py`), the print_stars lint exceptions are inline,
tidy checks the site's own page, the clone link uses https, the
birthday-problem and pi-estimation scripts compute what they claim, and
`config/project.lua` and `doc/` describe the current build.
