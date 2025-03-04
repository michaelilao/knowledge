# ACID

**Atomicity**: A transaction is all or nothing, if any part fails its rolled back. Ensured by Transactions, `START TRANSACTION`, `COMMIT`, `ROLLBACK`


**Consistency**: A DB moves to one valid state to another without corruption. Ensured by CONSTRAINTS

**Isolaton**: Executes indepently, preventing conflicts. Ensured by Isolation Levels

**Durability**: Once commited its permanent, even in case of a crash

## Stored Procedures

To create a SP

```sql
DELIMITER //
CREATE PROCEDURE procedure_name()
BEGIN
  SELECT * FROM employees

END //
DELIMITER;
```

SP can have IN, OUT, and INOUT paramaters

**IN**: A value you pass into the function

```sql
DELIMITER //

CREATE PROCEDURE GetEmployeeById(IN emp_id INT)
BEGIN
    SELECT * FROM employees WHERE id = emp_id;
END //

DELIMITER ;

CALL GetEmployeeById(101)
```

**OUT**: a paramater you pass into the function that will store a variable and will be returned

```sql
DELIMITER //

CREATE PROCEDURE GetTotalSalary(OUT total_salary DECIMAL(10,2))
BEGIN
    SELECT SUM(salary) INTO total_salary FROM employees;
END //

DELIMITER ;

CALL GetTotalSalary(@salary);
SELECT @salary;

```

**INOUT**: A value that you pass in that can be manimupated and returned

```sql
DELIMITER //

CREATE PROCEDURE IncreaseSalary(INOUT emp_salary DECIMAL(10,2))
BEGIN
    SET emp_salary = emp_salary * 1.10;
END //

DELIMITER ;

SET @salary = 5000;
CALL IncreaseSalary(@salary);
SELECT @salary;
```


You can also use transactions in SP to ensure ACID compliance and complicated biz logic.


```sql
DELIMITER //

CREATE PROCEDURE TransferMoney(
    IN sender_id INT,
    IN receiver_id INT,
    IN amount DECIMAL(10,2)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback in case of an error
        ROLLBACK;
        SELECT 'Transaction Failed!';
    END;

    -- Start Transaction
    START TRANSACTION;

    -- Deduct money from sender
    UPDATE accounts 
    SET balance = balance - amount 
    WHERE id = sender_id;

    -- Add money to receiver
    UPDATE accounts 
    SET balance = balance + amount 
    WHERE id = receiver_id;

    -- Commit transaction if all queries succeed
    COMMIT;

    SELECT 'Transaction Successful!';
END //

DELIMITER ;
```


## Triggers

Triggers are a special kind of SP, that automatically execute based on a specific event. Can be `BEFORE` or `AFTER` events like `INSERT`, `DELETE`, or `UPDATE`. 

```sql
DELIMITER //

CREATE TRIGGER Before_Insert_Employee
BEFORE INSERT ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary < 1000 THEN
        SET NEW.salary = 1000; -- Enforce minimum salary
    END IF;
END //

DELIMITER ;
```

```sql
DELIMITER //

CREATE TRIGGER After_Insert_Employee
AFTER INSERT ON employees
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (action, description, created_at)
    VALUES ('INSERT', CONCAT('New employee added: ', NEW.name), NOW());
END //

DELIMITER ;
```
#### Use Cases
- Helpful for keeping data consistent
- Adding audit logs automatically


The `NEW` keyword is used to reference the new row being added.
The `OLD` keyword is used to reference the old row being updated or deleted

####  When to use `NEW`
- `NEW` is used in `INSERT` triggers to reference the data being added
- `NEW` cannot be used in `DELETE`
- `NEW` is used in `UPDATE` to refer to the updated row
- `NEW` cannot modify data in an `AFTER` trigger since the data has already been commited
- Used for data validation before insert/update
- Setting default values
- Audit Logs

#### When to use `OLD`
- `OLD` is used in `UPDATE` triggers to reference the data before it is changed
- `OLD` is used in `DELETE` triggers to reference the data before its deleted
- `OLD` cannot be used in `INSERT` because it does not exist yet
- `OLD` cannot be used to modify data because it already exists
- Used for tracking updates and recording delete logs
- Enforcing biz logic before deletion

