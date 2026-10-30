# TODO

## Now

- split every riddle to it's own file and include them all in the final output.
- we are also running htmlhint with no option and with default config
    - which may be wrong. fix this also.
- make a better favicon for the riddling web-site.
- stop using perl for the scripting and use python instead (will be shorter and easier to read).
    - integrate with pydmt.
- remove the ugly colors from the pdf output.
    - (red and blue). Try to control them.

## idea

create a python library which allows you to create 3d and 2d drawings easily.
it would be object oriented and will emit it's output in various formats (say pstricks, pdf,
tikz, sketch, and more...).
The advantage of this idea over the others is that it would you python as the interpreter with
all of its power. (how about tying this to numpy?!?).

## caching

- Move to version on the pdf created and so allow caching.
    - get ridd of the .htaccess file in web. see [caching.md](caching.md) for details.

## latex code

- find a way to spell check the latex files and add it to the makefile.
- give better colors to the hyper links in the latex.
- mark all TODO items the same way (using a latex macro?!?).

## sketch code

- start breaking down the .sk files into chunks of defs and reusing them all
over to avoid code duplication.

## licensing

- rethink the license for this package.

## build system

- make the makefile check that all the tools that it is going to use are ready for use.
    - Do that using an external perl script.
    - This way people won't get funky error messages well off into the build process.
- write a perl wrapper for lacheck (it is also problematic).
- build each .sk into an image of it's own. This way it will be very easy to work on the drawings
  and I could make a logo for the riddling project itself.

## direct pdf viewing on web

- when using the google API to see the pdf directly in an iframe in my web page links like the table
of content (intra-document PDF links) do not work. Links to the outside do work. Check if we can fix this.
- stop using the google API for pdf publishing - it is shit. It requires login to google.

## misc

- collect links to various riddling sites over the web in the 'doc' folder.
- remove lots of the manuals that I carry in doc and have command to show them from ubuntu (provided
  that they do exist in some ubuntu -doc package that is...).
