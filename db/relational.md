# Relational Databases

Data is organized into tables. **Tables** are comproised of **Rows** and **Columns**.

**Rows** are called records and are entries in the table.

**Columns** are attributes or properties of an entry.

**Primary Key** is a attribute or a group of attributes that uniquely identify a row.

**Foreign Key** establishes a connection to a primary key of another record in another table. Ex: Order Table has a relation to the customer table, every order is related to a customer ID.



## Types of Constraints
There are constraints you can have on each column to enforce behaviour

**PRIMARY KEY**: must be unique and cannot contain null values, one per table. Ex: EmployeeID INT PRIMARY KEY

**FOREIGN KEY**: refers to a primary key in another table. Ex: FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)

- ON DELETE CASCADE, can be added to a foreign key that will delete child records when the parent is deleted. Only for use when you want to delete child records if a parent is removed. Not for when you want to perserve data if the parent is deleted
- ON DELETE SET NULL, can be added to allow for deletion but sets the FK to null if the parent is deleted
- ON UPDATE CASCADE, if the PK referenced changes, that all the related children also have FK updated to match.

**UNIQUE**: ensures columns or groups of columns are unique. A table can have multiple UNIQUE columns

**NOT NULL**: ensures column is not empty

**CHECK**: ensures columns follow a specific condition: CHECK (Age > 0)

**DEFAULT**: gives a default value if no value is assigned at creation. Ex: OrderDate DATE DEFAULT CURRENT_DATE

**ENUM**: ensures a column is a specific value given. Role ENUM('Admin', 'User') NOT NULL


## Data Types

- INT/INTEGER
- FLOAT/DOUBLE
- DECIMAL (p,s)
- CHAR: good for fixed length fields (country codes)
- VARCHAR: good for variable length
- TEXT: good for large texts like blog posts, full indexing is not needed
- ENUM
- DATE/TIME/DATETIME/TIMESTAMP
- BOOL