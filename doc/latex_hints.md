# LaTeX hints

## running pdflatex

references:
http://ringlord.com/latex-to-pdf-howto.html

- the executable we run:
  we need to run pdflatex and and pdftex since pdflatex has access to all the libraries of tex
  while pdftex does not.
- if you want to see if the thumbnail generation thing worked you can use acroread by adobe.
    - a package by the name of 'acroread' is available for ubuntu.

## bookmarks in the pdf files

If you want the bookmarks you need to run pdflatex more than once on the input.
If you only run one time you get no bookmarks (it's a second pass thing...).
The same goes for the table of contents, and this book needs three runs: the second typesets the
table of contents, which moves every section a few pages on, and the third fixes their page numbers.
See [building.md](building.md).

## comments in latex files

Just add % at the start of the line and the rest is a comment.

references:
http://www.rasmusen.org/x/2007/09/07/comments-in-latex/

## links in latex files

Use `\href{http://en.wikipedia.org/wiki/Catalan_number}{Catalan numbers}`.
(`\htmladdnormallink` was used while the book was also converted to HTML; see
[history.md](history.md).)
