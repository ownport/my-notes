# Using Redis for Queues on python

##  RestMQ

[RestMQ](http://restmq.com/) is a message queue which uses HTTP as transport, JSON to format a minimalist protocol and is organized as REST resources. It stands on the shoulder of giants, built over Python, Twisted, Cyclone (a Tornado implementation over twisted) and Redis.

Message queues are created on the fly, as a message is sent to them. They are simple to use as a curl request can be.

There is a simple JSON-based protocol for those looking for a more formal syntax, but it is not mandatory.

The core idea is to use Redis's LIST type to provide the message ordering, and SETs to index queues. Also each queue has a UUID generator to provide atomic and unique ids for each queue item.

This basic protocol can be implemented in any language. Python and Cyclone were used due to the maturity and robustness it offered but there are work started using [Ruby](http://gist.github.com/524240) and [Erlang](http://github.com/gleicon/restmq-erl).

The fixed set of operations provides that even different brokers can interoperate in the simplest level (put and take objects out of the queue), thanks to Redis atomic operations.

There are HTTP clients for pratically all languages. That's all that it takes to use RestMQ within your application. No special protocols or strategies, just dynamically created queues. 


## Links for review

 - [redis-queue, A Simple Tasks Queue Based on Redis DB](http://code.google.com/p/redis-queue/)
 - [Implement a Simple FIFO Queue](http://rediscookbook.org/implement_a_fifo_queue.html)
 - [Simple python queue with Redis](http://peter-hoffmann.com/2012/python-simple-queue-redis-queue.html)
 - [flask-redis](http://flask.pocoo.org/snippets/73/) A basic Message Queue with Redis for flask.
 - [HotQueue](http://pypi.python.org/pypi/hotqueue/0.2.1) is a Python library that allows you to use Redis as a message queue within your Python programs.
 - [RedisRPC](http://pypi.python.org/pypi/redisrpc) is the easiest to use RPC library. It has implementations in Ruby, PHP, and Python.
 - [celery](http://celeryproject.org/) An asynchronous task queue/job queue based on distributed message passing. Much more advanced. Can be used with different storage backends.
 - [rq](http://nvie.com/rq/) Simple python library for queueing jobs and processing them in the background with workers.
 - [resque](https://github.com/defunkt/resque) is a Redis-backed Ruby library for creating background jobs, placing them on multiple queues, and processing them later. Used at github. Includes a nice monitoring web interface.
 - [pyres](https://github.com/binarydud/pyres) A resque clone in python.
 
## Alternatives (not only Python)
 - [defunkt/resque](https://github.com/defunkt/resque) Resque is a Redis-backed Ruby library for creating background jobs, placing them on multiple queues, and processing them later.
 - [Apache ActiveMQ](http://activemq.apache.org/) is the most popular and powerful open source messaging and Integration Patterns server.
