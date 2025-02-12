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



 
