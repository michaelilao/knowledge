# Database Design

Designing a database is the process of structuring and organizing your data into tables. 
1. Requirement Analysis
2. ER Model to visualize tables and columns and their relationships
3. Logical Design -> convert into tables, PK and FK
4. Physical Design -> Optimization & Indexing

## Normalization
Process of splitting a table into multiple to reduce redudanacy

- 1NF: No repeating groups/arrays in a column
- 2NF: Every non-PK ust depend on the PK
- 3NF: Remove transitive dependencies. Ex: | CustomerID | State | Country | can be split into two tables | CustomerID | State | and | State | Country |
- Denormilization: used for performance

## Design Principles
1. Use PK properly, auto increment when applicable
2. Set FKs. Use ON DELETE CASCADE when child records should be removed with parent
3. PK and FK indexes by default
4. Add indexes on freqeunt queried columns
5. Use normilization to keep data consistent, denormalization can be used to speed up performance
6. Use 


## Indexes
1. **Primary Indexes**, automatically created, stores the table in sorted order based on the indexed column
2. **Unique Index**, automatically created on UNIQUE and PK.
3. **Non Clustered**, Stores seperate structure with pointers to table, does not change physical order. CREATE INDEX idx_name on Customers(Name)
4. **Composite Index**, Index on multiple columns CREATE INDEX idx_name on Customers(Name, Age)
5. **Full Text Index**, helpful for fast searching on large text fields. CREATE FULLTEXT INDEX idx_name ON Articles(Content)

#### Good candidates for indexes
- Frequent searches on WHERE
- Columns used in JOIN, ORDER BY, and GROUP BY
- FK
- Large tables with frequent lookups
- Too many indexes slow down insert/update.



