# Python coroutines 

## PEP 342/coroutines

This [PEP 342](http://www.python.org/dev/peps/pep-0342/) proposes some enhancements to the API and syntax of generators, to make them usable as simple coroutines.  It is basically a combination of ideas from these two PEPs, which may be considered redundant if this PEP is accepted:

 - [PEP 288](http://www.python.org/dev/peps/pep-0288), Generators Attributes and Exceptions.  The current PEP covers its second half, generator exceptions (in fact the throw() method name was taken from PEP 288). PEP 342 replaces generator attributes, however, with a concept from an earlier revision of PEP 288, the "yield expression".

 - [PEP 325](http://www.python.org/dev/peps/pep-0325), Resource-Release Support for Generators.  PEP 342 ties up a few loose ends in the PEP 325 spec, to make it suitable for actual implementation.

## Greenlet

[The greenlet package](http://pypi.python.org/pypi/greenlet/) is a spin-off of Stackless, a version of CPython that supports micro-threads called "tasklets". Tasklets run pseudo-concurrently (typically in a single or a few OS-level threads) and are synchronized with data exchanges on "channels".

A "greenlet", on the other hand, is a still more primitive notion of micro-thread with no implicit scheduling; coroutines, in other words. This is useful when you want to control exactly when your code runs. You can build custom scheduled micro-threads on top of greenlet; however, it seems that greenlets are useful on their own as a way to make advanced control flow structures. For example, we can recreate generators; the difference with Python's own generators is that our generators can call nested functions and the nested functions can yield values too. Additionally, you don't need a "yield" keyword. See the example in tests/test_generator.py.

Greenlets are provided as a C extension module for the regular unmodified interpreter. Greenlets are lightweight coroutines for in-process concurrent programming.

## Gevent

[gevent](http://www.gevent.org/) is a [coroutine](http://en.wikipedia.org/wiki/Coroutine)-based Python networking library that uses [greenlet](http://codespeak.net/py/0.9.2/greenlet.html) to provide a high-level synchronous API on top of the [libevent](http://monkey.org/~provos/libevent/) event loop.

Features include:

 - Fast event loop based on libevent (epoll on Linux, kqueue on FreeBSD).
 - Lightweight execution units based on greenlet.
 - API that re-uses concepts from the Python standard library (for example there are [Events](http://www.gevent.org/gevent.event.html#module-gevent.event) and [Queues](http://www.gevent.org/gevent.queue.html#module-gevent.queue)).
 - [Cooperative sockets with SSL support](http://www.gevent.org/networking.html)
 - DNS queries performed through libevent-dns.
 - [Monkey patching utility to get 3rd party modules to become cooperative](http://www.gevent.org/intro.html#monkey-patching)
 - [Fast WSGI server based on libevent-http](http://www.gevent.org/servers.html)
 
gevent is [inspired by eventlet](http://blog.gevent.org/2010/02/27/why-gevent/) but features more consistent API, simpler implementation and better performance. Read why others use gevent and check out the list of the open source projects based on gevent.

gevent is written and maintained by [Denis Bilenko](http://denisbilenko.com/) with help from the contributors and is licensed under the MIT license.

## Eventlet

[Eventlet](http://eventlet.net/) is a concurrent networking library for Python that allows you to change how you run your code, not how you write it.

 - It uses epoll or libevent for [highly scalable non-blocking I/O](http://en.wikipedia.org/wiki/Asynchronous_I/O#Select.28.2Fpoll.29_loops).
 - [Coroutines](http://en.wikipedia.org/wiki/Coroutine) ensure that the developer uses a blocking style of programming that is similar to threading, but provide the benefits of non-blocking I/O.
 - The event dispatch is implicit, which means you can easily use Eventlet from the Python interpreter, or as a small part of a larger application.

It's easy to get started using Eventlet, and easy to convert existing applications to use it. Start off by looking at [examples](http://eventlet.net/doc/examples.html), [common design patterns](http://eventlet.net/doc/design_patterns.html), and the list of the [basic API primitives](http://eventlet.net/doc/basic_usage.html).
 
## Bluelet

[Bluelet](https://github.com/sampsyo/bluelet/) is a simple, pure-Python solution for writing intelligible asynchronous socket applications. It uses PEP 342 coroutines to make concurrent I/O look and act like sequential programming.

In this way, it is similar to the Greenlet green-threads library and its associated packages Eventlet and Gevent. Bluelet has a simpler, 100% Python implementation that comes at the cost of flexibility and performance when compared to Greenlet-based solutions. However, it should be sufficient for many applications that don't need serious scalability; it can be thought of as a less-horrible alternative to [asyncore](http://docs.python.org/library/asyncore.html) or an asynchronous replacement for [SocketServer](http://docs.python.org/library/socketserver.html) (and more).


