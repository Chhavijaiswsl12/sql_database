mysql> use  `a-11(joins)`;
Database changed
mysql> create table department(
    ->     department_id int PRIMARY KEY,
    ->     department_name VARCHAR(50)
    -> );
Query OK, 0 rows affected (0.10 sec)

mysql> CREATE Table employees(
    ->     emp_id int PRIMARY KEY AUTO_INCREMENT,
    ->     emp_name VARCHAR(40),
    ->     dept_id int
    -> );
Query OK, 0 rows affected (0.04 sec)

mysql> ALTER TABLE employees add FOREIGN KEY(dept_id) REFERENCES department(department_id);
Query OK, 0 rows affected (0.13 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> INSERT INTO employees(
    ->     emp_name,dept_id
    -> )VALUES
    -> ('alice',101),
    -> ('Bob',102),
    -> ('Charlie',103),
    -> ('David',101)
    -> ;
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`a-11(joins)`.`employees`, CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `department` (`department_id`))
mysql> INSERT into department
    -> VALUES
    -> (101,'HR'),
    -> (102,'IT'),
    -> (103,'Finance');
Query OK, 3 rows affected (0.01 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from employees;
Empty set (0.01 sec)

mysql> desc employees;
+----------+-------------+------+-----+---------+----------------+
| Field    | Type        | Null | Key | Default | Extra          |
+----------+-------------+------+-----+---------+----------------+
| emp_id   | int         | NO   | PRI | NULL    | auto_increment |
| emp_name | varchar(40) | YES  |     | NULL    |                |
| dept_id  | int         | YES  | MUL | NULL    |                |
+----------+-------------+------+-----+---------+----------------+
3 rows in set (0.02 sec)

mysql> INSERT INTO employees (emp_name, dept_id)
    -> VALUES
    -> ('Alice', 101),
    -> ('Bob', 102),
    -> ('Charlie', 103),
    -> ('David', 101);
Query OK, 4 rows affected (0.01 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> select * from department;
+---------------+-----------------+
| department_id | department_name |
+---------------+-----------------+
|           101 | HR              |
|           102 | IT              |
|           103 | Finance         |
+---------------+-----------------+
3 rows in set (0.00 sec)

mysql> select * from employees;
+--------+----------+---------+
| emp_id | emp_name | dept_id |
+--------+----------+---------+
|      5 | Alice    |     101 |
|      6 | Bob      |     102 |
|      7 | Charlie  |     103 |
|      8 | David    |     101 |
+--------+----------+---------+
4 rows in set (0.00 sec)

mysql> select emp_name, department_name from employees as e inner join department as d on e.dept_id=d.department_id;
+----------+-----------------+
| emp_name | department_name |
+----------+-----------------+
| Alice    | HR              |
| David    | HR              |
| Bob      | IT              |
| Charlie  | Finance         |
+----------+-----------------+
4 rows in set (0.00 sec)

mysql> select emp_name, department_name from employees as e inner join department as d on e.dept_id=d.department_id where department='hr';
ERROR 1054 (42S22): Unknown column 'department' in 'where clause'
mysql> select emp_name, department_name from employees as e inner join department as d on e.dept_id=d.department_id where department_name='hr';
+----------+-----------------+
| emp_name | department_name |
+----------+-----------------+
| Alice    | HR              |
| David    | HR              |
+----------+-----------------+
2 rows in set (0.00 sec)

mysql> select emp_id,emp_name, department_name from employees as e left join department as d on e.dept_id=d.department_id;
+--------+----------+-----------------+
| emp_id | emp_name | department_name |
+--------+----------+-----------------+
|      5 | Alice    | HR              |
|      6 | Bob      | IT              |
|      7 | Charlie  | Finance         |
|      8 | David    | HR              |
+--------+----------+-----------------+
4 rows in set (0.13 sec)

mysql> select emp_name,count(emp_id),department_name from employees as e join department as d on e.dept_id=d.department_id;
ERROR 1140 (42000): In aggregated query without GROUP BY, expression #1 of SELECT list contains nonaggregated column 'a-11(joins).e.emp_name'; this is incompatible with sql_mode=only_full_group_by
mysql> select emp_name,count(emp_id),department_name from employees as e join department as d on e.dept_id=d.department_id group by department_name;
ERROR 1055 (42000): Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'a-11(joins).e.emp_name' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
mysql> select emp_name,count(emp_id),department_name from employees as e join department as d on e.dept_id=d.department_id group by d.department_name;
ERROR 1055 (42000): Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'a-11(joins).e.emp_name' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
mysql> select emp_name,count(e.emp_id),department_name from employees as e join department as d on e.dept_id=d.department_id group by d.department_name;
ERROR 1055 (42000): Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'a-11(joins).e.emp_name' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
mysql> select e.emp_name,count(e.emp_id),department_name from employees as e join department as d on e.dept_id=d.department_id group by d.department_name;
ERROR 1055 (42000): Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'a-11(joins).e.emp_name' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
mysql> select e.emp_name,count(e.emp_id),d.department_name from employees as e join department as d on e.dept_id=d.department_id group by d.department_name;
ERROR 1055 (42000): Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'a-11(joins).e.emp_name' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
mysql> select e.emp_name,count(e.emp_id) as total,d.department_name from employees as e join department as d on e.dept_id=d.department_id group by d.department_name;
ERROR 1055 (42000): Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'a-11(joins).e.emp_name' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
mysql> select count(e.emp_id) as total,d.department_name from employees as e join department as d on e.dept_id=d.department_id group by d.department_name;
+-------+-----------------+
| total | department_name |
+-------+-----------------+
|     2 | HR              |
|     1 | IT              |
|     1 | Finance         |
+-------+-----------------+
3 rows in set (0.04 sec)

mysql> select count(e.emp_id) as total,d.department_name from employees as e join department as d on e.dept_id=d.department_id where department is null group by d.department_name;
ERROR 1054 (42S22): Unknown column 'department' in 'where clause'
mysql> select count(e.emp_id) as total,d.department_name from employees as e join department as d on e.dept_id=d.department_id where d.department_name is null group by d.department_name;
Empty set (0.03 sec)

mysql> select count(e.emp_id) as total,d.department_name from employees as e join department as d on e.dept_id=d.department_id where d.department_name is null group by d.department_name;
Empty set (0.00 sec)

mysql> select count(e.emp_id) as total,d.department_name from employees as e left join department as d on e.dept_id=d.department_id where d.department_name is null group by d.department_name;
Empty set (0.04 sec)

mysql> select count(e.emp_id) ,d.department_name from employees as e left join department as d on e.dept_id=d.department_id where d.department_name is null group by d.department_name;
Empty set (0.00 sec)

mysql> select count(e.emp_name) ,d.department_name from employees as e left join department as d on e.dept_id=d.department_id where d.department_name is null group by d.department_name;
Empty set (0.00 sec)

mysql> select emp_name,department_name from employees as e right join department as d on e.dept_id=d.department_id;
+----------+-----------------+
| emp_name | department_name |
+----------+-----------------+
| Alice    | HR              |
| David    | HR              |
| Bob      | IT              |
| Charlie  | Finance         |
+----------+-----------------+
4 rows in set (0.02 sec)

mysql> select emp_name,department_name from employees as e right join department as d on e.dept_id=d.department_id;
+----------+-----------------+
| emp_name | department_name |
+----------+-----------------+
| Alice    | HR              |
| David    | HR              |
| Bob      | IT              |
| Charlie  | Finance         |
+----------+-----------------+
4 rows in set (0.02 sec)

mysql> select,d.department_name from employees as e right join department as d on e.dept_id=d.department_id where department is null group by d.department_name;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ',d.department_name from employees as e right join department as d on e.dept_id=d' at line 1
mysql> select d.department_name from employees as e right join department as d on e.dept_id=d.department_id where department is null group by d.department_name;
ERROR 1054 (42S22): Unknown column 'department' in 'where clause'
mysql> select d.department_name from employees as e right join department as d on e.dept_id=d.department_id where department_name is null group by d.department_name;
Empty set (0.03 sec)

mysql> select d.department_name from employees as e  join department as d on e.dept_id=d.department_id where department_name is null group by d.department_name;
Empty set (0.00 sec)

mysql> select d.department_name from employees as e  join department as d on e.dept_id=d.department_id where department_name is null ;
Empty set (0.00 sec)

mysql> select d.department_name from employees as e  right join department as d on e.dept_id=d.department_id where department_name is null ;
Empty set (0.00 sec)

mysql> select d.department_name from employees as e  right join department as d on e.dept_id=d.department_id where department_name is null ;
Empty set (0.00 sec)

mysql> select d.department_name from employees as e  right join department as d on e.dept_id=d.department_id where e.emp_name is null ;
Empty set (0.00 sec)

mysql> select emp_id,emp_name,department_name from employees as e left join department as d and employees as e right join department as d ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'and employees as e right join department as d' at line 1
mysql> select emp_id,emp_name,department_name from employees as e left join department as d and employees as e right join department as d ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'and employees as e right join department as d' at line 1
mysql> ;
ERROR:
No query specified

mysql> select emp_id,emp_name,department_name from employees as e left join department as d as total;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'as total' at line 1
mysql> select emp_id,emp_name,department_name from (employees as e left join department as d) as total;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ') as total' at line 1
mysql> select emp_id,emp_name,department_name from employees as e left join department as d union employees as e right join department as d ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'union employees as e right join department as d' at line 1
mysql> SELECT e.emp_id, e.emp_name, d.department_name
    -> FROM employees AS e
    -> LEFT JOIN department AS d
    -> ON e.dept_id = d.department_id
    ->
    -> UNION
    ->
    -> SELECT e.emp_id, e.emp_name, d.department_name
    -> FROM employees AS e
    -> RIGHT JOIN department AS d
    -> ON e.dept_id = d.department_id;
+--------+----------+-----------------+
| emp_id | emp_name | department_name |
+--------+----------+-----------------+
|      5 | Alice    | HR              |
|      6 | Bob      | IT              |
|      7 | Charlie  | Finance         |
|      8 | David    | HR              |
+--------+----------+-----------------+
4 rows in set (0.05 sec)

mysql> create table customer(cust_id int primary key,cust_name varchar(30));
Query OK, 0 rows affected (0.20 sec)

mysql> create table orders(order_id int primary key, cust_id int,foreign key(cust_id) references customer(cust_id), order_date date, total_amount int);
Query OK, 0 rows affected (0.09 sec)

mysql> ALTER TABLE orders
    -> DROP FOREIGN KEY orders_ibfk_1;
Query OK, 0 rows affected (0.05 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> INSERT INTO customer VALUES
    -> (101, 'Alice'),
    -> (102, 'Bob'),
    -> (103, 'Charlie'),
    -> (104, 'David'),
    -> (105, 'Emma');
Query OK, 5 rows affected (0.05 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> INSERT INTO orders VALUES
    -> (201, 101, '2026-10-01', 5000),
    -> (202, 102, '2026-10-05', 3000),
    -> (203, 101, '2026-10-15', 7000),
    -> (204, 103, '2026-10-20', 2500),
    -> (205, 106, '2026-10-22', 4000),
    -> (206, 107, '2026-10-25', 6000);
Query OK, 6 rows affected (0.01 sec)
Records: 6  Duplicates: 0  Warnings: 0

mysql> select * from customer;
+---------+-----------+
| cust_id | cust_name |
+---------+-----------+
|     101 | Alice     |
|     102 | Bob       |
|     103 | Charlie   |
|     104 | David     |
|     105 | Emma      |
+---------+-----------+
5 rows in set (0.04 sec)

mysql> select * from orders ;
+----------+---------+------------+--------------+
| order_id | cust_id | order_date | total_amount |
+----------+---------+------------+--------------+
|      201 |     101 | 2026-10-01 |         5000 |
|      202 |     102 | 2026-10-05 |         3000 |
|      203 |     101 | 2026-10-15 |         7000 |
|      204 |     103 | 2026-10-20 |         2500 |
|      205 |     106 | 2026-10-22 |         4000 |
|      206 |     107 | 2026-10-25 |         6000 |
+----------+---------+------------+--------------+
6 rows in set (0.00 sec)

mysql> select cust_name,order_id,order_date,total_amount from customer as c left join orders as o on c.cust_id=o.cust_id;
+-----------+----------+------------+--------------+
| cust_name | order_id | order_date | total_amount |
+-----------+----------+------------+--------------+
| Alice     |      201 | 2026-10-01 |         5000 |
| Alice     |      203 | 2026-10-15 |         7000 |
| Bob       |      202 | 2026-10-05 |         3000 |
| Charlie   |      204 | 2026-10-20 |         2500 |
| David     |     NULL | NULL       |         NULL |
| Emma      |     NULL | NULL       |         NULL |
+-----------+----------+------------+--------------+
6 rows in set (0.05 sec)

mysql> select cust_name,order_id,order_date,total_amount from customer as c right join orders as o on c.cust_id=o.cust_id;
+-----------+----------+------------+--------------+
| cust_name | order_id | order_date | total_amount |
+-----------+----------+------------+--------------+
| Alice     |      201 | 2026-10-01 |         5000 |
| Bob       |      202 | 2026-10-05 |         3000 |
| Alice     |      203 | 2026-10-15 |         7000 |
| Charlie   |      204 | 2026-10-20 |         2500 |
| NULL      |      205 | 2026-10-22 |         4000 |
| NULL      |      206 | 2026-10-25 |         6000 |
+-----------+----------+------------+--------------+
6 rows in set (0.03 sec)

mysql>  select cust_name,order_id,order_date,total_amount from customer as c left join orders as o on c.cust_id=o.cust_id union  select cust_name,order_id,order_date,total_amount from customer as c right join orders as o on c.cust_id=o.cust_id;
+-----------+----------+------------+--------------+
| cust_name | order_id | order_date | total_amount |
+-----------+----------+------------+--------------+
| Alice     |      201 | 2026-10-01 |         5000 |
| Alice     |      203 | 2026-10-15 |         7000 |
| Bob       |      202 | 2026-10-05 |         3000 |
| Charlie   |      204 | 2026-10-20 |         2500 |
| David     |     NULL | NULL       |         NULL |
| Emma      |     NULL | NULL       |         NULL |
| NULL      |      205 | 2026-10-22 |         4000 |
| NULL      |      206 | 2026-10-25 |         6000 |
+-----------+----------+------------+--------------+
8 rows in set (0.05 sec)

mysql> select cust_name,order_id,order_date from customer as c right cross join orders as o ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'cross join orders as o' at line 1
mysql> select cust_name,order_id,order_date from customer  cross join orders  ;
+-----------+----------+------------+
| cust_name | order_id | order_date |
+-----------+----------+------------+
| Emma      |      201 | 2026-10-01 |
| David     |      201 | 2026-10-01 |
| Charlie   |      201 | 2026-10-01 |
| Bob       |      201 | 2026-10-01 |
| Alice     |      201 | 2026-10-01 |
| Emma      |      202 | 2026-10-05 |
| David     |      202 | 2026-10-05 |
| Charlie   |      202 | 2026-10-05 |
| Bob       |      202 | 2026-10-05 |
| Alice     |      202 | 2026-10-05 |
| Emma      |      203 | 2026-10-15 |
| David     |      203 | 2026-10-15 |
| Charlie   |      203 | 2026-10-15 |
| Bob       |      203 | 2026-10-15 |
| Alice     |      203 | 2026-10-15 |
| Emma      |      204 | 2026-10-20 |
| David     |      204 | 2026-10-20 |
| Charlie   |      204 | 2026-10-20 |
| Bob       |      204 | 2026-10-20 |
| Alice     |      204 | 2026-10-20 |
| Emma      |      205 | 2026-10-22 |
| David     |      205 | 2026-10-22 |
| Charlie   |      205 | 2026-10-22 |
| Bob       |      205 | 2026-10-22 |
| Alice     |      205 | 2026-10-22 |
| Emma      |      206 | 2026-10-25 |
| David     |      206 | 2026-10-25 |
| Charlie   |      206 | 2026-10-25 |
| Bob       |      206 | 2026-10-25 |
| Alice     |      206 | 2026-10-25 |
+-----------+----------+------------+
30 rows in set (0.03 sec)

mysql>