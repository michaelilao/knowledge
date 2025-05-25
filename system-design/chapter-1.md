# Chapter 1: Scale from Zero to Millions of Users

## Single Server
User Request -> Domain -> DNS -> API -> Webserver -> Server Response

## DB
Add in a database server to independently scale web and data. 
DB recieves; read, write and update requests and returns data

### DB Types

#### Relational DB (RDBMS)
SQL Databases (MySQL, Postgres, Oracle, etc...) store data in tables and rows

#### Non Relational DB (NoSQL)
NoSQL databases that store non related and unstructued data, like MongoDB. 
Use Cases
- Low Latency
- Data is unstructured
- Store massive amount of data

## Vertical vs Horizontal Scaling

**Vertical Scaling** referes to adding more CPU, Memory, RAM, etc... to your server, scaling up your single server. 
- Simple and good for low traffic
- Single point of failure
- Limitation on how much power you can add

**Horizontal Scaling** refers to adding multiple servers
- Adds redudancy 
- Can scale infinitely
- Adds complexity

### Load Balancer
Evenly distributes traffic to servers. Public IP resolves to the loadbalancer and the load balancer directs traffic to private IP's of the server pool.

### Database Replication
Database replication can be used with a master/slave relationship. The master database supports only write operations. While the slave databases get copies of data and only support read operations. This allows for multiple read requests simultaneuosly. This is used when there is a higher ratio of read to write operations.

- Reliability: If one database is destroyed, data is preserved.
- High Availability: Replicating data across servers, if one data is down, data is stored on another server.

### Cache

Temporary storage for expensive responses or frequently accessed data in memory, so that subsequent requests are served more quickly.

Eviction Policies: If the cache is full which item to remove.

- LRU: Least recently used
- LFU: Least frequently used
- FIFO: First in First Out


### CDN

Network of geographically dispersed servers, used to deliver static content. Serve images, videos, JS etc.

#### Workflow
1. User A tries to get image, tries to get from CDN.
2. If the CDN does not have it will get it from the server with a TTL
3. CDN stores it on its server and returns to user
4. User B tries to get the same image.
5. Images is returned quicker from CDN


### Stateless Web Tier (REST)

Remove state (user state), outside of the web tier and move to a DB. Each web server can access the state from a DB. Stateless does not keep state infromation from 1 request to another. This allows to horizontally scale as with more traffic you can add more servers.

### Message Queue

Serves as a buffer and distributes async requests. Input services called produccers create messages and publish them to the queue, other services called subscribers connected to the queue, perform actions defined by the messages.

Decoupling is the preferred architcture. Producer can post a message to the queue when the consumer is unavailable, and vice-versa. Good for logging, long complex tasks and analytics

### Vertical Database Scaling

Scaling by adding more CPU RAM to an existing machine. 
- Great risk of single point of failure
- Cost is high and there are limits
- Complexity is low

### Horizontal DB Scaling

Known as sharding is splitting 1 db into multiple shards that all share the same schema. User data is allocated to shards based on a shard key like a userID.

Problems in sharding
- Resharding, when a single shard cannot hold more data due to uneven data distribution.
- Celebrity Problem, if a shard is accessed more frequently than the others
- Joining, hard to perform joins accross shards, so data is denormalized and replicated in a single table
