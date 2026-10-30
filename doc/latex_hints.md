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

If you want the bookmarks you need to run pdflatex TWO TIMES on the input.
If you only run one time you get no bookmarks (it's a second pass thing...).
Stangely, this also reduces the size of the output file so it's good either way.

## comments in latex files

Just add % at the start of the line and the rest is a comment.

references:
http://www.rasmusen.org/x/2007/09/07/comments-in-latex/

## hyperlinkx in latex files

I tried to put them this way:

```latex
\href{http://en.wikipedia.org/wiki/Catalan_number}{Catalan numbers}
```

But it turned out that this works well in PDF but doesn't show nice in HTML.

Then I tried this way:

```latex
\url{http://en.wikipedia.org/wiki/Catalan_number}
```

It works in both PDF and HTML but does not allow set custom text for the link and shows
the entire link (ugly!).

Then I tried this way:

```latex
\htmladdnormallink{Catalan numbers}{http://en.wikipedia.org/wiki/Catalan_number}
```

And it works well in both!!!

Lets try it another way.
