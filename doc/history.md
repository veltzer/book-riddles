# History

Approaches this project tried and dropped, kept for the lessons. The original
notes are in the git history.

## Converting the book to HTML

The book was once also published as HTML, made with latex2html. The drawings
came out badly, pdftohtml gave poor results, and the other tools listed at
http://enc.com.au/docs/latexhtml/ did not do better, so HTML generation was
dropped in 2011 and only the PDF is published.

The same choice explains a LaTeX hint from that time: `\htmladdnormallink`
was used for links because `\href` looked bad in latex2html's output, and
`\url` shows the whole address instead of a text. Without HTML, `\href` is fine.

## Producing the PDF

The first Makefile went latex -> dvi -> ps -> pdf (latex, dvips, ps2pdf),
because pdflatex then had trouble with the sketch drawings and the dvi route
gave smaller files. Switching sketch to TikZ output made pdflatex work, and the
book has been built with pdflatex ever since. qpdf was used to linearize the
PDF and raise its version to 1.5; the version and the author fields are now set
in riddling.tex itself (`\pdfminorversion`, hyperref's `pdfauthor`).

The Makefile, and later pydmt, were replaced by rsconstruct; see
[building.md](building.md).

## Showing the PDF on the web

- An apache server with a `.htaccess` sending no-cache headers, so readers
  would not keep an old copy of the PDF under the same name. The alternatives
  considered were a new file name per version, and fetching the PDF from
  JavaScript.
- flexpaper (Flash based), which failed on Flash security settings in some
  browsers, and plain `<object>` embedding, which many browsers did not support.
- The Google Docs viewer, which required readers to be logged in to Google.
- A vendored copy of the pdf.js viewer on GitHub Pages. It was removed in 2026:
  that version (2.3.41) was open to CVE-2024-4367, and every current browser
  shows PDFs by itself.

Today GitHub Pages serves `docs/` from master, and the site links straight to
`docs/riddling.pdf`.
