# Database Management System (DBMS)

DBMS: structured collection of data, allows for create, read update and delete of data.

Need for a DBMS
- reduced redudancy
- data integrity and consistency
- security
- simplified data access
- support for data relationships
- concurrency

## Database Languages
**DDL**: Data Definition Language -> Create, Alter, Truncate. Defines how data is structured

**DML**: Data Manipulation Language -> Select, Create, Update, Delete. Manipulates data.

**DCL**: Data Control Language -> Grant Revoke. Provides privledges to a specific db user.

**TCL**: Transaction Control Language -> Rollback, commit, savepoint. Used in store procedures and transactiosn to ensure ACID

## DBMS Architecture
Tier 1: DB, Client, Server all on one machines. Ex: Excel

Tier 2: Client, App connects to a DB via Network. Ex: Desktop Application

Tier 3: Client, App connects to a server that connects to a DB via networks. Ex: Web applications