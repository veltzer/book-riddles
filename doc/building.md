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
1. `scripts/build_riddles.py` writes `out/src/riddles.tex`, the body of the
   book: a chapter per category, each `\input`-ing its riddles from
   `src/include/*.tex`.
1. `scripts/build_pdf.py` compiles `src/tex/riddling.tex`, which `\input`s
   `out/src/riddles.tex` (and through it every riddle and the sketch figures),
   and copies the result to `docs/riddling.pdf`.

The last two steps are explicit processors in `rsconstruct.toml` (the book
rather than rsconstruct's pdflatex processor), because only an explicit
processor's `input_globs` can name another processor's outputs; that is also
what makes the first two steps run before pdflatex.

## Checks on the book

- aspell checks the spelling of `src/tex` and `src/include` in US English.
  Words it does not know but are right (names, terms, the codes in the coin
  riddles) go in `.aspell.en.pws`. Its TeX mode does not skip math, so one and
  two letter words are not checked at all.
- lacheck checks the LaTeX of the whole book, through
  `scripts/wrapper_lacheck.py`, which makes warnings fail the build. It lists
  the few kinds of warning that are wrong for this book (TikZ `\foreach` lists,
  factorials), each only on the kind of line it is wrong for.
- `scripts/check_categories.py` fails when a riddle's title does not end with
  its category in parentheses.

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
`\section {Title (Category)}` and with a `\subsection{Solution}`. That is all:
the book has a chapter per category, so the riddle lands in the chapter of its
category (a new category makes a new chapter), and the book prints the title
without the category, which the chapter already names.

Chapters are in alphabetical order, and so are the riddles in each chapter
(ignoring a leading "The" or "A"). A riddle that builds on another one, and
says "the previous riddle", puts it right before itself with a comment line
`% follows: <name>`, where `<name>` is the other riddle's file name without
`.tex`; both must be in the same category. See [names_of_files.md](names_of_files.md) for why the files end
in `.tex`.
