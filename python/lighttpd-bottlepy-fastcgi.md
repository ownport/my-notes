# bottle + lighttpd + fastcgi simply running

[bottle + lighttpd + fastcgi simply running](http://notionbox.de/detail/3/)

After messing around with bottle and lighttpd I finally found a solution that simply runs:

First be shure to load the lighttpd mod_fastcgi module, we will also use the mod_rewrite module. Add the following lines to /etc/lighttpd/lighttpd.conf:
```
server.modules += ("mod_fastcgi", "mod_rewrite")
```
Now we can start an FastCGI server the python script that uses bottle. Add the following to lighttpd.conf:
```
fastcgi.server = (
    ".py" =>
       (
            "python-fcgi" =>
                (
                    "socket" => "/tmp/fastcgi.python.socket",
                    "bin-path" => "/usr/bin/python /full_path_to/index.py",
                    "check-local" => "disable",
                    "max-procs" => 1,
                )
        )
)
```
Assuming your media-files are located in an directory named "media" lying in the root of your project path we will need an rewrite directive that redirects media file requests to this path. All other request are directed to our bottle script:
```
url.rewrite-once = (
    "^(/media.*)$" => "/$1",
    "^/(.*)$" => "/index.py/$1"
)
```
This is everything needed for the lighttpd configuration. A minimal example for an index.py could look like this:
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
import bottle
import os
from bottle import route, run, view

@route('/')
@view('index')
def index():
    return dict(hello='Hello World')

APP_ROOT = os.path.abspath(os.path.dirname(__file__))
bottle.TEMPLATE_PATH.append(os.path.join(APP_ROOT, 'templates'))
app = bottle.default_app()

if __name__ == '__main__':
    from flup.server.fcgi import WSGIServer
    WSGIServer(app).run()
```
We use the WSGIServer that comes with flup (python-flup). Besides we have to tell bottle to search for templates in the correct location (assuming that the templates lie in a directory named 'templates' in project root). This is done with the bottle TEMPLATE_PATH variable.

