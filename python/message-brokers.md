# Message brokers

[Message Broker](http://en.wikipedia.org/wiki/Message_broker) is an intermediary program which translates the language of a system from one internationally recognized language to another by way of a telecommunications medium.

### Pattern

A message broker is an architectural pattern for message validation, message transformation and message routing. It mediates communication amongst applications, minimizing the mutual awareness that applications should have of each other in order to be able to exchange messages, effectively implementing decoupling.

The purpose of a broker is to take incoming messages from applications and perform some action on them. The following are examples of actions that might be taken in the broker:

 - Route messages to one or more of many destinations
 - Transform messages to an alternative representation
 - Perform message aggregation, decomposing messages into multiple messages and sending them to their destination, then recomposing the responses into one message to return to the user
 - Interact with an external repository to augment a message or store it
 - Invoke Web services to retrieve data
 - Respond to events or errors
 - Provide content and topic-based message routing using the publish/subscribe model
 
### Broker Functionality

Many messaging patterns (like publish/subscribe) can work without a message broker. One pattern that requires a message broker is workload queues, that is message queues that are handled by multiple receivers. Such queues must be managed, transacted, and usually stored reliably, at a single point. 

## Links for review

 - [Messaging pattern](http://en.wikipedia.org/wiki/Messaging_pattern)
 - [http://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol](http://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol)
 - [Distributed Systems with ZeroMQ](http://blog.pythonisito.com/2012/08/distributed-systems-with-zeromq.html)
 - [Website monitoring with Distributed Messages/Tasks Processing(AMQP & RabbitMQ) on Django](http://www.slideshare.net/JimmyDeadcOde/website-monitoring-with-distributed-messagestasks-processing-amqp-rabbitmq-on-django)
 - [ActiveMQ]()
 - [RabbitMQ]()
 - [RestMQ]()
 
