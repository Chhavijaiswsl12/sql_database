QNO  8: Create and Insert into employees Table
Columns:

emp_id INT

emp_name VARCHAR(100)

gender VARCHAR(10)

dob DATE

department VARCHAR(100)

position VARCHAR(100)

salary DECIMAL(8,2)

joining_date DATE

phone VARCHAR(15)

Task:

Insert 5 employee records
-----------------------------------------------------------------

mysql> create database Tables_in_Employee;
Query OK, 1 row affected (0.00 sec)

mysql> use Tables_in_Employee;
Database changed
mysql> create table employees (emp_id INT auto_increment primary key,emp_name VARCHAR(100),gender VARCHAR(10),dob DATE,department VARCHAR(100),position VARCHAR(100),salary DECIMAL(8,2),joining_date DATE,phone VARCHAR(15));
Query OK, 0 rows affected (0.01 sec)

mysql> desc employees;
+--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| emp_id       | int          | NO   | PRI | NULL    | auto_increment |
| emp_name     | varchar(100) | YES  |     | NULL    |                |
| gender       | varchar(10)  | YES  |     | NULL    |                |
| dob          | date         | YES  |     | NULL    |                |
| department   | varchar(100) | YES  |     | NULL    |                |
| position     | varchar(100) | YES  |     | NULL    |                |
| salary       | decimal(8,2) | YES  |     | NULL    |                |
| joining_date | date         | YES  |     | NULL    |                |
| phone        | varchar(15)  | YES  |     | NULL    |                |
+--------------+--------------+------+-----+---------+----------------+
9 rows in set (0.00 sec)

mysql> INSERT INTO employees
    -> (emp_name, gender, dob, department, position, salary, joining_date, phone)
    -> VALUES
    -> ('Amit Sharma', 'Male', '1995-05-12', 'IT', 'Software Developer', 55000.00, '2022-06-15', '9876543210'),
    ->
    -> ('Priya Verma', 'Female', '1998-08-20', 'HR', 'HR Manager', 60000.00, '2021-03-10', '9876543211'),
    ->
    -> ('Rahul Patel', 'Male', '1996-11-05', 'Finance', 'Accountant', 45000.00, '2023-01-20', '9876543212'),
    ->
    -> ('Sneha Gupta', 'Female', '1997-02-14', 'Marketing', 'Marketing Executive', 40000.00, '2024-04-01', '9876543213'),
    ->
    -> ('Vikas Singh', 'Male', '1994-09-25', 'IT', 'Project Manager', 75000.00, '2020-07-12', '9876543214');
Query OK, 5 rows affected (0.00 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select * from employees;
+--------+-------------+--------+------------+------------+---------------------+----------+--------------+------------+
| emp_id | emp_name    | gender | dob        | department | position            | salary   | joining_date | phone      |
+--------+-------------+--------+------------+------------+---------------------+----------+--------------+------------+
|      1 | Amit Sharma | Male   | 1995-05-12 | IT         | Software Developer  | 55000.00 | 2022-06-15   | 9876543210 |
|      2 | Priya Verma | Female | 1998-08-20 | HR         | HR Manager          | 60000.00 | 2021-03-10   | 9876543211 |
|      3 | Rahul Patel | Male   | 1996-11-05 | Finance    | Accountant          | 45000.00 | 2023-01-20   | 9876543212 |
|      4 | Sneha Gupta | Female | 1997-02-14 | Marketing  | Marketing Executive | 40000.00 | 2024-04-01   | 9876543213 |
|      5 | Vikas Singh | Male   | 1994-09-25 | IT         | Project Manager     | 75000.00 | 2020-07-12   | 9876543214 |
+--------+-------------+--------+------------+------------+---------------------+----------+--------------+------------+