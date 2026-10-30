# sketch

I used sketch to draw 3d diagrams.

In ubuntu you just need to install the 'sketch' package.
(`apt-get install sketch`).
If you want documentation install 'sketch-doc'.

web site is:
http://www.frontiernet.net/~eugene.ressler/
and
http://groups.google.com/group/sketch-users

If you want to read documentation checkout the makefile targets that open up the documentation.
The documentation package also has examples that you can copy from.
Ubuntu also has examples in the sketch-doc package and you can find them at:
`/usr/share/doc/sketch-doc/examples`.

## hints

Stuff in sketch is either point or vector.
Functions like 'translate' want a vector.
Functions like 'line' want two points.
How do you convert a point 'p' into a vector? `(p)-(O)` (where O is the point of the origin, (0,0,0)).
How do you convert a vector 'v' into a point? `v+(O)`
Arithmetic in sketch could only be done on vectors and so in order to find the middle point between
two points p1 and p2 you do:

```text
def mid ((p1)-(O)+(p2)-(O))/2+(O)
```

and then use mid in your calculations. Yes - it is ugly.
You cannot passoff arithmetical expressions of this sort directly to primitive functions since they
expect to receive computed values. Precompute and put into temporary variables and then pass those
off.

## pstricks vs tikz

When you use sketch you must choose to work either in pstricks or tikz. This is done via the line:

```text
global { language tikz }
```

Mind you that pstricks is the default.
The problem is that if you use pstricks (the default) you have problems with pdflatex.
So I use tikz.
Please note that this is NOT transparent. Some code in sketch does refer either to
pstricks or tikz. See that in comments.

## comments in tikz

single like comment are:

```text
% comment
```

and can be from the middle of the line.
Sometimes %% is used but I don't use it.
