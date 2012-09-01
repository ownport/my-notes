# Gevent

Note from [redis-py with gevent](http://stackoverflow.com/questions/10928481/redis-py-with-gevent)
```
from gevent import monkey
monkey.patch_all()

gevent is mainly interesting when several connections at the same time are used, so that the event loop system calls can be factorized. If the user code generates a lot of synchronous roundtrips to Redis on a small number of connections, it will involve latency, even if these connections are managed in an asynchronous way by gevent.
```
