# Optimization

Optimizing databases can be done on the architecture, system or query level, to improve performance and query times

## Database Sharding
Process of splitting a large database into smaller shards and distributing them across servers
- Shards contain a subset of each row from a table
- Queries are routed to the correct shard based of a shard key like `customer_id`
- Each shard operates independently

Ex: Store users by their location
1. Shard 1 -> NA
2. Shard 2 -> EU
2. Shard 3 -> Asia

Benefits & Challenges
- Improves scalability and response time
- Complex queries for cross shard joins
- Shard Key selection is critical

## Database Partitioning
Splitting larger database into partitions that all remain on the same server

1. Range Partitions, divided based on a value of ranges. Ex: 2021 go to 1. 2022 go to 2.
2. List Partitions, divided based on predefined lists. Ex: USA goes to 1. CAD goes to 2.
3. Hash Partiion, a hash function that distributes data evenly

Benefits & Challenges
- Speeds of query and improves data management
- Helps with archiving old data
- Schema changes can be complex

## Database Replication
Involves replicating a database across multiple servers to improve performance, redudancy and tolerance.

1. Master-Slave, one master handles all writes and the slaves handle reads.
2. Master-Master, multiple masters handle both read/writes. For multi region-db

Benefits & Challenges
- Improves read performance
- Supports global scalability and fault tolerance
- Increased storage costs
- Data consistency issues


## Query Optimization
Query optimization ensures db queries run efficiently using optimal execution plans. To analyze queries we can use `EXPLAIN ANALYZE` to execute the query and show performance statistics.

- Used to identify bottlenecks
- See how indexes are used
- Find inefficient joins and table scans

```sql
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 101;
```

```sql
Seq Scan on orders  (cost=0.00..35.50 rows=10 width=100) (actual time=0.012..0.015 rows=10 loops=1)
  Filter: (customer_id = 101)
Planning Time: 0.125 ms
Execution Time: 0.220 ms
```

- Seq Scan shows it was a sequential scan, bad for large tables
- Cost is the estimated cost
- Rows is the estimated rows that match
- Planning Time -> time spent optimizing query
- Executution Time -> time spent executing query

We can add an index to improve performance
```sql
CREATE INDEX idx_customer_id ON orders(customer_id);
```

New result
```sql
Index Scan using idx_customer_id on orders  (cost=0.15..8.30 rows=10 width=100) (actual time=0.001..0.002 rows=10 loops=1)
```
- Index Scan meant it used an index to find rows quickly


### Optimizing Joins

```sql
EXPLAIN ANALYZE 
SELECT orders.id, customers.name 
FROM orders 
JOIN customers ON orders.customer_id = customers.id;

Nested Loop  (cost=0.40..125.00 rows=500 width=150) (actual time=0.015..10.220 rows=500 loops=1)
```
- Nested Loop is inefficient for large tables, add indexes to improve performance

```sql
CREATE INDEX idx_customers_id ON customers(id);
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
```
```
Hash Join  (cost=0.40..75.00 rows=500 width=150) (actual time=0.005..2.220 rows=500 loops=1)
```
- Hash join is faster than nested loop for large datasets

#### Optimizing using Partitions

```sql
EXPLAIN ANALYZE SELECT * FROM sales WHERE year = 2023;

Seq Scan on sales (cost=0.00..50000.00 rows=50000 width=120) (actual time=5.001..20.015 rows=50000 loops=1)
```

```sql
ALTER TABLE sales PARTITION BY RANGE (year) (
    PARTITION p2022 VALUES LESS THAN (2023),
    PARTITION p2023 VALUES LESS THAN (2024)
);
```

```sql
Partition Pruning: Removed partitions p2022
Index Scan on sales_2023 (cost=0.20..1000.00 rows=500 width=120) (actual time=0.005..2.010 rows=500 loops=1)
```
- Partition Pruning scans only relevant tables