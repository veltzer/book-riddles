# TODO

## Now

- make a better favicon for the riddling web-site.
- remove the ugly colors from the pdf output.
    - (red and blue). Try to control them.

## idea

create a python library which allows you to create 3d and 2d drawings easily.
it would be object oriented and will emit it's output in various formats (say pstricks, pdf,
tikz, sketch, and more...).
The advantage of this idea over the others is that it would you python as the interpreter with
all of its power. (how about tying this to numpy?!?).

## latex code

- find a way to spell check the latex files and add it to the build.
- give better colors to the hyper links in the latex.
- mark all TODO items the same way (using a latex macro?!?).
- run lacheck in the build; `scripts/wrapper_lacheck.py` (which makes lacheck's warnings fail the
  run) is ready but not wired in.

## sketch code

- start breaking down the .sk files into chunks of defs and reusing them all
  over to avoid code duplication.
- build each .sk into an image of it's own. This way it will be very easy to work on the drawings
  and I could make a logo for the riddling project itself.

## licensing

- rethink the license for this package.
