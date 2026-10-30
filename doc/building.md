# Building the book

```bash
rsconstruct tool install machine   # TeX Live parts, sketch, and the linters
rsconstruct build
```

The build writes `docs/riddling.pdf`, which is committed: GitHub Pages serves
`docs/` from master, so the committed file is the published book.

## The steps

1. Every `src/sk/*.sk` 3D scene is rendered to TikZ code by sketch, through
   `scripts/wrapper_sketch.py`, into `out/src/sk/*.tex`.
1. `scripts/build_pdf.py` compiles `src/tex/riddling.tex`, which `\input`s
   every riddle from `src/include/*.tex` and the sketch figures, and copies the
   result to `docs/riddling.pdf`.

The second step is an explicit processor in `rsconstruct.toml` rather than
rsconstruct's pdflatex processor, because only an explicit processor's
`input_globs` can name another processor's outputs; that is also what makes
sketch run first.

## Details worth knowing

- pdflatex runs three times: the first pass writes the table of contents, the
  second typesets it (which moves every section a few pages on), and the third
  picks up the moved page numbers. With two passes the contents are wrong.
- The title page shows when the PDF was built (to the minute), the commit it
  was built from (marked "with uncommitted changes" when the sources differ
  from it), and `git describe --tags` when the repository has tags.
  `build_pdf.py` passes these to LaTeX as `\buildtime`, `\buildcommit` and
  `\buildversion`. They are not inputs of the build, so a PDF restored from the
  cache keeps the stamp of the build that made it.
- The packages the book needs are listed in `[dependencies]` in
  `rsconstruct.toml`, with the reason for each.
- `itemize` labels are taken from the math fonts. Current LaTeX takes three of
  the four levels from the TS1 font, which without the cm-super package is only
  available as a blurry bitmap font.

## Adding a riddle

Write it as `src/include/<name>.tex`, starting with
`\section {Title (Category)}` and with a `\subsection{Solution}`, and add
`\input{src/include/<name>.tex}` to `src/tex/riddling.tex` before
`\label{end}`. See [names_of_files.md](names_of_files.md) for why the files end
in `.tex`.
