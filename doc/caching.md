# Issues of caching in this project

Web servers, like apache that I use, allow web browsers to cache content like pdfs, jpgs and such for some time.
Since I update the same file called riddles.pdf or some such then this caching is a problem since I cannot see
the new version.

## How can we solve this?

1. put a .htaccess that tells the web server to send http headers that tell the clients browser not to cache
the content in this folder -> this is what we currently do.
1. create a new file (riddles-version.pdf for instance) each time the version gets updated and link to
the new file from the web page. This is a better solution since caching will be enabled and we could
potentially have old versions too. The problem is that the web page needs to be generated automatically
somehow.
1. fetch the file using ajax when we show the pdf using some kind of "pdf viewer for javascript" solution.
Will this solve the problem? I'm not sure.
