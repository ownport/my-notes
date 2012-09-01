# Redis

[Redis](http://redis.io/) is an open source, advanced key-value store. It is often referred to as a data structure server since keys can contain strings, hashes, lists, sets and sorted sets.

You can run atomic operations on these types, like appending to a string; incrementing the value in a hash; pushing to a list; computing set intersection, union and difference; or getting the member with highest ranking in a sorted set.

In order to achieve its outstanding performance, Redis works with an in-memory dataset. Depending on your use case, you can persist it either by dumping the dataset to disk every once in a while, or by appending each command to a log.

Redis also supports trivial-to-setup master-slave replication, with very fast non-blocking first synchronization, auto-reconnection on net split and so forth.

Other features include a simple check-and-set mechanism, pub/sub and configuration settings to make Redis behave like a cache.

## Messaging via RedisRPC

The [PUBLISH](http://redis.io/commands/subscribe) and [SUBSCRIBE](http://redis.io/commands/publish) commands enable you to do quick messaging and communication between processes. 

The way it works is simple:

 - SUBSCRIBE will listen to a channel
 - PUBLISH allows you to push a message into a channel
 
Those two commands are all you need to build a messaging system with Redis.

## Open questions

 - Should we use [pipelining](http://rediscookbook.org/pipeline_multiple_commands.html) as must? 

## Links

 - [Redis Pub/Sub…how does it work?](http://robots.thoughtbot.com/post/6325247416/redis-pub-sub-how-does-it-work)
