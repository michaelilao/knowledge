# SQL Commands

SQL commands are used to interact with the DB and fall into 5 categories

1. Data Definition Language
2. Data Manipulation Language
3. Data Control Language 
4. Transactional Control Language

### Data Definition Language

**CREATE**: `CREATE TABLE Users (ID INT PRIMARY KEY, Name VARCHAR(100))`

**ALTER**: `ALTER TABLE USERS ADD Email VARCHAR(255)`

**DROP**: `DROP TABLE USERS`

**TRUNCATE**: Deletes data in table but keeps the structure `TRUNCATE TABLE USERS`

**RENAME**: Renames table/column `ALTER TABLE Users RENAME TO Customers`

- Autocommited and not rolled back


### Data Manipulation Language

**INSERT**: `INSERT INTO USERS (ID, Name) VALUES (1, 'Alice')`

**UPDATE**: `UPDATE Users SET Name = 'Bob' WHERE ID = 1`

**DELETE**: `DELETE FROM Users WHERE ID = 1`

- Can be rolled back 

### Data Control Language

**GRANT**: `GRANT SELECT ON Users to user1`

**REVOKE**: `REVOKE SELECT ON Users FROM user1`

### Transactional Control Language

Begin a transaction then commit it
```sql
START TRANSACTION;

UPDATE ACCOUNTS SET BALANCE = BALANCE - 500 WHERE AccountID = 1
UPDATE ACCOUNTS SET BALANCE = BALANCE + 500 WHERE AccountID = 2

COMMIT;
```

Begin a transaction then roll back
```sql
START TRANSACTION;

UPDATE ACCOUNTS SET BALANCE = BALANCE - 500 WHERE AccountID = 1
UPDATE ACCOUNTS SET BALANCE = BALANCE + 500 WHERE AccountID = 2

ROLLBACK;
```

Begin a transaction and roll back to a savepoint then commit everything up to that savepoint
```sql
START TRANSACTION

UPDATE ACCOUNTS SET BALANCE = BALANCE - 500 WHERE AccountID = 1;
SAVEPOINT sp1;

UPDATE ACCOUNTS SET BALANCE = BALANCE + 500 WHERE AccountID = 2;
SAVEPOINT sp2;

ROLLBACK TO sp1;
COMMIT;
```


### Advanced SQL Clauses

**WHERE**:  `SELECT * FROM CUSTOMERS WHERE Age > 25 AND/OR Name = 'Cassandra'`

**ORDER BY**: `SELECT * FROM CUSTOMERS ORDER BY Name ASC, AGE DESC`

**GROUP BY**: Aggregates data used with functions like `COUNT, SUM, AVG, MAX, MIN`
```sql
SELECT City, COUNT(*) AS TOTAL_Customers 
FROM CUSTOMERS 
GROUP BY CITY
```

**HAVING**: Filter similar to WHERE but on grouped records
```sql
SELECT Department, AVG(Salary) AS Avg_Salary
FROM EMPLOYEES
GROUP BY Department
HAVING AVG(Salary) > 50000;
```
Used on aggregated data since WHERE can't be used on aggregate functions

**LIMIT**: `SELECT * FROM Employees LIMIT 5;`

**OFFSET**: `SELECT * FROM Employees LIMIT 5 OFFSET 5;`, gets the next records 5-10

**CASE**: Acts like if/else in a sql query
```sql
SELECT Name, Salary,
  CASE
    WHEN Salary > 70000 THEN 'High'
    WHEN Salary BETWEEN 40000 AND 70000 THEN 'Medium'
    ELSE 'Low'
  END AS Salary_Cat
FROM Employees
```

**IN**: Checks if a value matches any value in a list. `SELECT * FROM Employees WHERE Department IN ('HR', 'IT')`

### SQL JOINS

**INNER JOIN**: Returns only matching rows from both tables

**LEFT JOIN**: Returns all rows from left table + matching rows from right

**RIGHT JOIN**: Returns all rows from right table + matching rows from left

**FULL JOIN**: Returns all rows from both tables, filling in missing values with NULL

### SQL Views
A virtual table based off a query. Depending on the query it can also be updated directly

```sql
CREATE VIEW view_name AS
SELECT col1, col2
FROM t1
WHERE col1 > 20
```

If there are no JOIN or GROUP BY, then you can update the view directly