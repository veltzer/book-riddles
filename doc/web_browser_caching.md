# Web browser caching

When you embed the HTML output of this project into a web page and update
to a new version of the material then some users may have issues with seeing
the old data because of browser caches.
The output of this project is therefore considered "dynamic" (since you
may update it at any time without notice and the users should not cache it).
As such, the web server must be told to send headers to the web client so
as to tell it not to cache the files. This is done via the .htaccess file.
see:
http://www.askapache.com/htaccess/using-http-headers-with-htaccess.html
The file involved is web/htaccess
And during the installation it is copied to be .htaccess in the right place.
