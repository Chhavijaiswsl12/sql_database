mysql> use `a-12(subquery)`;
Database changed
mysql> create table department(dept_id int primary key, dep_name varchar(30), location varchar(30));
Query OK, 0 rows affected (0.36 sec)

mysql> create table employee(emp_id int primary key, emp_name    VARCHAR(30)
    -> salary decimal(10,2), dept_id int);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'salary decimal(10,2), dept_id int)' at line 2
mysql> create table employee(emp_id int primary key, emp_name    VARCHAR(30)
    -> , salary decimal(10,2), dept_id int);
Query OK, 0 rows affected (0.06 sec)

mysql> INSERT INTO department (dept_id, dept_name, location)
    -> VALUES
    -> (1, 'HR', 'Indore'),
    -> (2, 'IT', 'Pune'),
    -> (3, 'Finance', 'Mumbai'),
    -> (4, 'Sales', 'Indore'),
    -> (5, 'Admin', 'Delhi'),
    -> (6, 'Research', 'Bangalore');
ERROR 1054 (42S22): Unknown column 'dept_name' in 'field list'
mysql> ALTER TABLE employee
    -> ADD CONSTRAINT fk_employee_department
    -> FOREIGN KEY (dept_id)
    -> REFERENCES department(dept_id);
Query OK, 0 rows affected (0.17 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> ALTER TABLE employee
    -> ADD CONSTRAINT fk_employee_department
    -> FOREIGN KEY (dept_id)
    -> REFERENCES department(dept_id);
ERROR 1826 (HY000): Duplicate foreign key constraint name 'fk_employee_department'
mysql> INSERT INTO department (dept_id, dep_name, location)
    -> VALUES
    -> (1, 'HR', 'Indore'),
    -> (2, 'IT', 'Pune'),
    -> (3, 'Finance', 'Mumbai'),
    -> (4, 'Sales', 'Indore'),
    -> (5, 'Admin', 'Delhi'),
    -> (6, 'Research', 'Bangalore');
Query OK, 6 rows affected (0.03 sec)
Records: 6  Duplicates: 0  Warnings: 0

mysql> INSERT INTO employee (emp_id, emp_name, salary, dept_id)
    -> VALUES
    -> (101, 'Rahul', 45000, 1),
    -> (102, 'Priya', 55000, 2),
    -> (103, 'Aman', 40000, 3),
    -> (104, 'Neha', 60000, 2),
    -> (105, 'Karan', 35000, 4),
    -> (106, 'Sneha', 50000, 1),
    -> (107, 'Rohit', 70000, 6),
    -> (108, 'Pooja', 30000, 5),
    -> (109, 'Vikas', 65000, 2),
    -> (110, 'Anjali', 42000, 4),
    -> (111, 'Mohit', 38000, 3),
    -> (112, 'Kavita', 48000, 6),
    -> (113, 'Arjun', 52000, 1),
    -> (114, 'Simran', 33000, 5),
    -> (115, 'Deepak', 58000, 2);
Query OK, 15 rows affected (0.01 sec)
Records: 15  Duplicates: 0  Warnings: 0

mysql> select * from employee;
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    101 | Rahul    | 45000.00 |       1 |
|    102 | Priya    | 55000.00 |       2 |
|    103 | Aman     | 40000.00 |       3 |
|    104 | Neha     | 60000.00 |       2 |
|    105 | Karan    | 35000.00 |       4 |
|    106 | Sneha    | 50000.00 |       1 |
|    107 | Rohit    | 70000.00 |       6 |
|    108 | Pooja    | 30000.00 |       5 |
|    109 | Vikas    | 65000.00 |       2 |
|    110 | Anjali   | 42000.00 |       4 |
|    111 | Mohit    | 38000.00 |       3 |
|    112 | Kavita   | 48000.00 |       6 |
|    113 | Arjun    | 52000.00 |       1 |
|    114 | Simran   | 33000.00 |       5 |
|    115 | Deepak   | 58000.00 |       2 |
+--------+----------+----------+---------+
15 rows in set (0.05 sec)

mysql> select * from department;
+---------+----------+-----------+
| dept_id | dep_name | location  |
+---------+----------+-----------+
|       1 | HR       | Indore    |
|       2 | IT       | Pune      |
|       3 | Finance  | Mumbai    |
|       4 | Sales    | Indore    |
|       5 | Admin    | Delhi     |
|       6 | Research | Bangalore |
+---------+----------+-----------+
6 rows in set (0.00 sec)

mysql> select avg(salary) from emoployee;
ERROR 1146 (42S02): Table 'a-12(subquery).emoployee' doesn't exist
mysql> select avg(salary) from employee;
+--------------+
| avg(salary)  |
+--------------+
| 48066.666667 |
+--------------+
1 row in set (0.01 sec)

mysql> select * from employee where salary>avg(salary)
    -> ;
ERROR 1111 (HY000): Invalid use of group function
mysql> select avg(salary),emp_name from employee group by emp_name having salary>avg(salary) ;
ERROR 1054 (42S22): Unknown column 'salary' in 'having clause'
mysql> select * from employee where salary=( select * from employee where salary>avg(salary);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
mysql> select * from employee where salary=( select salary from employee where salary>avg(salary) from employee;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'from employee' at line 1
mysql> select * from employee where salary=( select salary from employee where salary>avg(salary) ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
mysql> select * from employee where salary=( select salary  where salary>avg(salary) from employee ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'from employee' at line 1
mysql> select * from employee where salary=( select avg(salary) from employee ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
mysql> select * from employee where salary=( select avg(salary) from employee );
Empty set (0.02 sec)

mysql> select * from employee where salary>( select avg(salary) from employee );
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    102 | Priya    | 55000.00 |       2 |
|    104 | Neha     | 60000.00 |       2 |
|    106 | Sneha    | 50000.00 |       1 |
|    107 | Rohit    | 70000.00 |       6 |
|    109 | Vikas    | 65000.00 |       2 |
|    113 | Arjun    | 52000.00 |       1 |
|    115 | Deepak   | 58000.00 |       2 |
+--------+----------+----------+---------+
7 rows in set (0.00 sec)

mysql> select * from employee where
    -> salary = (select max(salary) from employee);
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    109 | Vijay    | 70000.00 |       2 |
+--------+----------+----------+---------+
1 row in set (0.01 sec)

mysql> select * from employee where
    -> salary = (select min(salary) from employee);
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    112 | Arjun    | 25000.00 |       5 |
+--------+----------+----------+---------+
1 row in set (0.00 sec)

mysql> select * from employee where
    -> salary > (select salary from employee wher emp_name = "Amit");
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'emp_name = "Amit")' at line 2
mysql> select * from employee where
    -> salary > (select salary from employee where emp_name = "Amit");
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    102 | Rahul    | 50000.00 |       2 |
|    103 | Priya    | 40000.00 |       2 |
|    104 | Neha     | 60000.00 |       3 |
|    105 | Rohit    | 35000.00 |       3 |
|    106 | Sneha    | 45000.00 |       4 |
|    107 | Karan    | 55000.00 |       4 |
|    109 | Vijay    | 70000.00 |       2 |
|    110 | Ankit    | 32000.00 |       5 |
|    111 | Meena    | 65000.00 |       3 |
+--------+----------+----------+---------+
9 rows in set (0.01 sec)

mysql> select * from employee where
    -> salary < (select salary from employee where emp_name = "Rahul");
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    101 | Amit     | 30000.00 |       1 |
|    103 | Priya    | 40000.00 |       2 |
|    105 | Rohit    | 35000.00 |       3 |
|    106 | Sneha    | 45000.00 |       4 |
|    108 | Pooja    | 28000.00 |       1 |
|    110 | Ankit    | 32000.00 |       5 |
|    112 | Arjun    | 25000.00 |       5 |
+--------+----------+----------+---------+
7 rows in set (0.00 sec)

mysql> select * from employee where
    -> dept_id = (select dept_id from department where location = "Indore");
ERROR 1242 (21000): Subquery returns more than 1 row
mysql> select dept_id from department where location = "Indore";
+---------+
| dept_id |
+---------+
|       1 |
|       4 |
+---------+
2 rows in set (0.00 sec)

mysql> select * from employee where
    -> dept_id in (select dept_id from department where location = "Indore");
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    101 | Amit     | 30000.00 |       1 |
|    106 | Sneha    | 45000.00 |       4 |
|    107 | Karan    | 55000.00 |       4 |
|    108 | Pooja    | 28000.00 |       1 |
+--------+----------+----------+---------+
4 rows in set (0.02 sec)

mysql> select * from employee where
    -> dept_id in (select dept_id from department where dept_name in ("IT","Finance"));
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    102 | Rahul    | 50000.00 |       2 |
|    103 | Priya    | 40000.00 |       2 |
|    104 | Neha     | 60000.00 |       3 |
|    105 | Rohit    | 35000.00 |       3 |
|    109 | Vijay    | 70000.00 |       2 |
|    111 | Meena    | 65000.00 |       3 |
+--------+----------+----------+---------+
6 rows in set (0.00 sec)

mysql> select * from employee where
    -> dept_id not in (select dept_id from department where location = "Indore");
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    102 | Rahul    | 50000.00 |       2 |
|    103 | Priya    | 40000.00 |       2 |
|    104 | Neha     | 60000.00 |       3 |
|    105 | Rohit    | 35000.00 |       3 |
|    109 | Vijay    | 70000.00 |       2 |
|    110 | Ankit    | 32000.00 |       5 |
|    111 | Meena    | 65000.00 |       3 |
|    112 | Arjun    | 25000.00 |       5 |
+--------+----------+----------+---------+
8 rows in set (0.01 sec)

mysql> select * from employee where
    -> dept_id not in (select dept_id from department);
Empty set (0.00 sec)

mysql> select dept_id from department where
    -> dept_id not in (select dept_id from employee);
+---------+
| dept_id |
+---------+
|       6 |
+---------+
1 row in set (0.00 sec)

mysql> select * from department where
    -> dept_id not in (select dept_id from employee);
+---------+-----------+-----------+
| dept_id | dept_name | location  |
+---------+-----------+-----------+
|       6 | Research  | Bangalore |
+---------+-----------+-----------+
1 row in set (0.00 sec)

mysql> select * from employee where
    -> salary > (select avg(salary) from employee where
    -> dept_id in (select dept_id from department where dept_name = "IT"));
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    104 | Neha     | 60000.00 |       3 |
|    107 | Karan    | 55000.00 |       4 |
|    109 | Vijay    | 70000.00 |       2 |
|    111 | Meena    | 65000.00 |       3 |
+--------+----------+----------+---------+
4 rows in set (0.00 sec)

mysql> select * from employee where
    -> salary > (select avg(salary) from employee where
    -> dept_id in (select dept_id from department where dept_name = "Finance"));
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    104 | Neha     | 60000.00 |       3 |
|    107 | Karan    | 55000.00 |       4 |
|    109 | Vijay    | 70000.00 |       2 |
|    111 | Meena    | 65000.00 |       3 |
+--------+----------+----------+---------+
4 rows in set (0.00 sec)

mysql> select avg(salary) from employee where
    -> dept_id in (select dept_id from department where dept_name = "Finance");
+--------------+
| avg(salary)  |
+--------------+
| 53333.333333 |
+--------------+
1 row in set (0.00 sec)

mysql> select avg(salary) from employee where
    -> dept_id in (select dept_id from department where dept_name = "IT");
+--------------+
| avg(salary)  |
+--------------+
| 53333.333333 |
+--------------+
1 row in set (0.00 sec)

mysql> select * from employee where
    -> salary < (select min(salary) from employee where
    -> dept_id in (select dept_id from department where dept_name = "Sales"));
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    101 | Amit     | 30000.00 |       1 |
|    103 | Priya    | 40000.00 |       2 |
|    105 | Rohit    | 35000.00 |       3 |
|    108 | Pooja    | 28000.00 |       1 |
|    110 | Ankit    | 32000.00 |       5 |
|    112 | Arjun    | 25000.00 |       5 |
+--------+----------+----------+---------+
6 rows in set (0.00 sec)

mysql> select * from employee where
    -> salary < any(select salary from employee where
    -> dept_id in (select dept_id from department where dept_name = "IT"));
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    101 | Amit     | 30000.00 |       1 |
|    102 | Rahul    | 50000.00 |       2 |
|    103 | Priya    | 40000.00 |       2 |
|    104 | Neha     | 60000.00 |       3 |
|    105 | Rohit    | 35000.00 |       3 |
|    106 | Sneha    | 45000.00 |       4 |
|    107 | Karan    | 55000.00 |       4 |
|    108 | Pooja    | 28000.00 |       1 |
|    110 | Ankit    | 32000.00 |       5 |
|    111 | Meena    | 65000.00 |       3 |
|    112 | Arjun    | 25000.00 |       5 |
+--------+----------+----------+---------+
11 rows in set (0.00 sec)

mysql> select * from employee where
    -> salary < all(select salary from employee where
    -> dept_id in (select dept_id from department where dept_name = "HR"));
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    112 | Arjun    | 25000.00 |       5 |
+--------+----------+----------+---------+
1 row in set (0.01 sec)

mysql> select * from employee where
    -> salary < any(select salary from employee where
    -> dept_id in (select dept_id from department where dept_name = "HR"));
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    108 | Pooja    | 28000.00 |       1 |
|    112 | Arjun    | 25000.00 |       5 |
+--------+----------+----------+---------+
2 rows in set (0.00 sec)

mysql> select * from employee where
    -> salary > any(select salary from employee where
    -> dept_id in (select dept_id from department where dept_name = "HR"));
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    101 | Amit     | 30000.00 |       1 |
|    102 | Rahul    | 50000.00 |       2 |
|    103 | Priya    | 40000.00 |       2 |
|    104 | Neha     | 60000.00 |       3 |
|    105 | Rohit    | 35000.00 |       3 |
|    106 | Sneha    | 45000.00 |       4 |
|    107 | Karan    | 55000.00 |       4 |
|    109 | Vijay    | 70000.00 |       2 |
|    110 | Ankit    | 32000.00 |       5 |
|    111 | Meena    | 65000.00 |       3 |
+--------+----------+----------+---------+
10 rows in set (0.00 sec)

mysql> select * from employee where
    -> salary < all(select salary from employee where
    -> dept_id in (select dept_id from department where dept_name = "HR"));
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    112 | Arjun    | 25000.00 |       5 |
+--------+----------+----------+---------+
1 row in set (0.00 sec)

mysql> select * from employee where
    -> salary > any(select salary from employee where
    -> dept_id in (select dept_id from department where dept_name = "HR"));
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    101 | Amit     | 30000.00 |       1 |
|    102 | Rahul    | 50000.00 |       2 |
|    103 | Priya    | 40000.00 |       2 |
|    104 | Neha     | 60000.00 |       3 |
|    105 | Rohit    | 35000.00 |       3 |
|    106 | Sneha    | 45000.00 |       4 |
|    107 | Karan    | 55000.00 |       4 |
|    109 | Vijay    | 70000.00 |       2 |
|    110 | Ankit    | 32000.00 |       5 |
|    111 | Meena    | 65000.00 |       3 |
+--------+----------+----------+---------+
10 rows in set (0.00 sec)

mysql> select * from employee where
    -> salary > all(select salary from employee where
    -> dept_id in (select dept_id from department where dept_name = "HR"));
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    102 | Rahul    | 50000.00 |       2 |
|    103 | Priya    | 40000.00 |       2 |
|    104 | Neha     | 60000.00 |       3 |
|    105 | Rohit    | 35000.00 |       3 |
|    106 | Sneha    | 45000.00 |       4 |
|    107 | Karan    | 55000.00 |       4 |
|    109 | Vijay    | 70000.00 |       2 |
|    110 | Ankit    | 32000.00 |       5 |
|    111 | Meena    | 65000.00 |       3 |
+--------+----------+----------+---------+
9 rows in set (0.00 sec)

mysql> select * from employee where
    -> salary > any(select salary from employee where
    -> dept_id in (select dept_id from department where dept_name = "Finance"));
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    102 | Rahul    | 50000.00 |       2 |
|    103 | Priya    | 40000.00 |       2 |
|    104 | Neha     | 60000.00 |       3 |
|    106 | Sneha    | 45000.00 |       4 |
|    107 | Karan    | 55000.00 |       4 |
|    109 | Vijay    | 70000.00 |       2 |
|    111 | Meena    | 65000.00 |       3 |
+--------+----------+----------+---------+
7 rows in set (0.00 sec)

mysql> select * from employee where
    -> salary < all(select salary from employee where
    -> dept_id in (select dept_id from department where dept_name = "IT"));
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    101 | Amit     | 30000.00 |       1 |
|    105 | Rohit    | 35000.00 |       3 |
|    108 | Pooja    | 28000.00 |       1 |
|    110 | Ankit    | 32000.00 |       5 |
|    112 | Arjun    | 25000.00 |       5 |
+--------+----------+----------+---------+
5 rows in set (0.00 sec)

mysql> select * from employee where
    -> salary > select avg(salary) from employee where
    -> dept_id  (select dept_id from department where dept_name = "IT"));
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'select avg(salary) from employee where
dept_id  (select dept_id from department ' at line 2
mysql> select * from employee where
    ->
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
mysql> select * from employee where
    -> salary > (select avg(salary) from employee where
    -> dept_id = select dept_id from department
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'select dept_id from department' at line 3
mysql> select * from employee where
    -> (dept_id,salary>) in (select dept_id,avg(salary) from employee
    -> group by dept_id);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ') in (select dept_id,avg(salary) from employee
group by dept_id)' at line 2
mysql> select * from employee where
    -> (dept_id,salary>) in (select dept_id,avg(salary) from employee
    -> group by dept_id);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ') in (select dept_id,avg(salary) from employee
group by dept_id)' at line 2
mysql> select * from employee where
    -> salary > ( select avg(salary) from employee
    -> where dept_id = e.dept_id);
ERROR 1054 (42S22): Unknown column 'e.dept_id' in 'where clause'
mysql> select * from employee as e where
    -> salary > ( select avg(salary) from employee
    -> where dept_id = e.dept_id);
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    101 | Amit     | 30000.00 |       1 |
|    104 | Neha     | 60000.00 |       3 |
|    107 | Karan    | 55000.00 |       4 |
|    109 | Vijay    | 70000.00 |       2 |
|    110 | Ankit    | 32000.00 |       5 |
|    111 | Meena    | 65000.00 |       3 |
+--------+----------+----------+---------+
6 rows in set (0.00 sec)

mysql> select * from employee where
    -> salary < ( select avg(salary) from employee
    -> where dept_id = e.dept_id);
ERROR 1054 (42S22): Unknown column 'e.dept_id' in 'where clause'
mysql> select * from employee as e where
    -> salary < ( select avg(salary) from employee
    -> where dept_id = e.dept_id);
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    102 | Rahul    | 50000.00 |       2 |
|    103 | Priya    | 40000.00 |       2 |
|    105 | Rohit    | 35000.00 |       3 |
|    106 | Sneha    | 45000.00 |       4 |
|    108 | Pooja    | 28000.00 |       1 |
|    112 | Arjun    | 25000.00 |       5 |
+--------+----------+----------+---------+
6 rows in set (0.00 sec)

mysql> select * from employee where
    -> salary = ( select avg(salary) from employee
    -> where dept_id = e.dept_id);
ERROR 1054 (42S22): Unknown column 'e.dept_id' in 'where clause'
mysql> select * from employee as e where
    -> salary = ( select avg(salary) from employee
    -> where dept_id = e.dept_id);
Empty set (0.00 sec)

mysql> select * from employee where
    -> (Dept_id,salary) in (select Dept_id,max(salary)
    -> from employee group by dept_id);
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    101 | Amit     | 30000.00 |       1 |
|    107 | Karan    | 55000.00 |       4 |
|    109 | Vijay    | 70000.00 |       2 |
|    110 | Ankit    | 32000.00 |       5 |
|    111 | Meena    | 65000.00 |       3 |
+--------+----------+----------+---------+
5 rows in set (0.01 sec)

mysql> select * from employee where
    -> (Dept_id,salary) in (select Dept_id,min(salary)
    -> from employee group by dept_id);
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    103 | Priya    | 40000.00 |       2 |
|    105 | Rohit    | 35000.00 |       3 |
|    106 | Sneha    | 45000.00 |       4 |
|    108 | Pooja    | 28000.00 |       1 |
|    112 | Arjun    | 25000.00 |       5 |
+--------+----------+----------+---------+
5 rows in set (0.00 sec)

mysql> select * from employee where
    -> (Dept_id,salary) not in (select Dept_id,max(salary)
    -> from employee group by dept_id);
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    102 | Rahul    | 50000.00 |       2 |
|    103 | Priya    | 40000.00 |       2 |
|    104 | Neha     | 60000.00 |       3 |
|    105 | Rohit    | 35000.00 |       3 |
|    106 | Sneha    | 45000.00 |       4 |
|    108 | Pooja    | 28000.00 |       1 |
|    112 | Arjun    | 25000.00 |       5 |
+--------+----------+----------+---------+
7 rows in set (0.00 sec)

mysql> select * from employee where
    -> (Dept_id,salary) not in (select Dept_id,min(salary)
    -> from employee group by dept_id);
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    101 | Amit     | 30000.00 |       1 |
|    102 | Rahul    | 50000.00 |       2 |
|    104 | Neha     | 60000.00 |       3 |
|    107 | Karan    | 55000.00 |       4 |
|    109 | Vijay    | 70000.00 |       2 |
|    110 | Ankit    | 32000.00 |       5 |
|    111 | Meena    | 65000.00 |       3 |
+--------+----------+----------+---------+
7 rows in set (0.00 sec)

mysql> select * from employee where
    -> salary = ( select max(salary) from employee as e where
    -> e.emp_id <> ( select emp_id from employee
    -> where salary = ( select max(salary) from employee)));
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    111 | Meena    | 65000.00 |       3 |
+--------+----------+----------+---------+
1 row in set (0.01 sec)

mysql> select max(salary) from employee where
    -> salary < (select max(salary) from employee where
    -> salary < (select max(salary) from employee));
+-------------+
| max(salary) |
+-------------+
|    60000.00 |
+-------------+
1 row in set (0.01 sec)

mysql> select * from employee where
    -> salary = (select max(salary) from employee where
    -> salary < (select max(salary) from employee where
    -> salary < (select max(salary) from employee)));
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    104 | Neha     | 60000.00 |       3 |
+--------+----------+----------+---------+
1 row in set (0.00 sec)

mysql> select * from department where
    -> dept_id in ( select dept_id from employee);
+---------+-----------+----------+
| dept_id | dept_name | location |
+---------+-----------+----------+
|       1 | HR        | Indore   |
|       2 | IT        | Pune     |
|       3 | Finance   | Mumbai   |
|       4 | Sales     | Indore   |
|       5 | Admin     | Delhi    |
+---------+-----------+----------+
5 rows in set (0.01 sec)

mysql> select * from department where
    -> dept_id not in ( select dept_id from employee);
+---------+-----------+-----------+
| dept_id | dept_name | location  |
+---------+-----------+-----------+
|       6 | Research  | Bangalore |
+---------+-----------+-----------+
1 row in set (0.01 sec)

select * from department where
    -> dept_id in ( select dept_id from employee
    -> where salary > 60000);
+---------+-----------+----------+
| dept_id | dept_name | location |
+---------+-----------+----------+
|       2 | IT        | Pune     |
|       3 | Finance   | Mumbai   |
+---------+-----------+----------+
2 rows in set (0.00 sec)

mysql> select * from department where
    -> dept_id in ( select dept_id from employee
    -> where salary < 30000);
+---------+-----------+----------+
| dept_id | dept_name | location |
+---------+-----------+----------+
|       1 | HR        | Indore   |
|       5 | Admin     | Delhi    |
+---------+-----------+----------+
2 rows in set (0.00 sec)

select * from employee where
    -> dept_id in (select dept_id from department);
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    101 | Amit     | 30000.00 |       1 |
|    102 | Rahul    | 50000.00 |       2 |
|    103 | Priya    | 40000.00 |       2 |
|    104 | Neha     | 60000.00 |       3 |
|    105 | Rohit    | 35000.00 |       3 |
|    106 | Sneha    | 45000.00 |       4 |
|    107 | Karan    | 55000.00 |       4 |
|    108 | Pooja    | 28000.00 |       1 |
|    109 | Vijay    | 70000.00 |       2 |
|    110 | Ankit    | 32000.00 |       5 |
|    111 | Meena    | 65000.00 |       3 |
|    112 | Arjun    | 25000.00 |       5 |
+--------+----------+----------+---------+
12 rows in set (0.02 sec)

mysql> select * from employee as e where
    -> salary > (select avg(salary) from employee where
    -> dept_id = e.dept_id);
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    101 | Amit     | 30000.00 |       1 |
|    104 | Neha     | 60000.00 |       3 |
|    107 | Karan    | 55000.00 |       4 |
|    109 | Vijay    | 70000.00 |       2 |
|    110 | Ankit    | 32000.00 |       5 |
|    111 | Meena    | 65000.00 |       3 |
+--------+----------+----------+---------+
6 rows in set (0.01 sec)

mysql> select * from employee as e where
    -> salary = (select max(salary) from employee where
    -> dept_id = e.dept_id);
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    101 | Amit     | 30000.00 |       1 |
|    107 | Karan    | 55000.00 |       4 |
|    109 | Vijay    | 70000.00 |       2 |
|    110 | Ankit    | 32000.00 |       5 |
|    111 | Meena    | 65000.00 |       3 |
+--------+----------+----------+---------+
5 rows in set (0.00 sec)

mysql> select * from employee as e where
    -> salary = (select min(salary) from employee where
    -> dept_id = e.dept_id);
+--------+----------+----------+---------+
| emp_id | emp_name | salary   | dept_id |
+--------+----------+----------+---------+
|    103 | Priya    | 40000.00 |       2 |
|    105 | Rohit    | 35000.00 |       3 |
|    106 | Sneha    | 45000.00 |       4 |
|    108 | Pooja    | 28000.00 |       1 |
|    112 | Arjun    | 25000.00 |       5 |
+--------+----------+----------+---------+
5 rows in set (0.00 sec)




-- Q1. Employees whose salary is greater than company average.

SELECT *
FROM employee
WHERE salary > (
    SELECT AVG(salary)
    FROM employee
);


-- Q2. Employee(s) receiving the highest salary.

SELECT *
FROM employee
WHERE salary = (
    SELECT MAX(salary)
    FROM employee
);


-- Q3. Employee(s) receiving the lowest salary.

SELECT *
FROM employee
WHERE salary = (
    SELECT MIN(salary)
    FROM employee
);


-- Q4. Employees earning more than Amit.

SELECT *
FROM employee
WHERE salary > (
    SELECT salary
    FROM employee
    WHERE emp_name = 'Amit'
);


-- Q5. Employees earning less than Rahul.

SELECT *
FROM employee
WHERE salary < (
    SELECT salary
    FROM employee
    WHERE emp_name = 'Rahul'
);


-- Q6. Employees working in departments located in Indore.

SELECT *
FROM employee
WHERE dept_id IN (
    SELECT dept_id
    FROM department
    WHERE location = 'Indore'
);


-- Q7. Employees working in IT or Finance departments.

SELECT *
FROM employee
WHERE dept_id IN (
    SELECT dept_id
    FROM department
    WHERE dept_name IN ('IT', 'Finance')
);


-- Q8. Employees not working in departments located in Indore.

SELECT *
FROM employee
WHERE dept_id NOT IN (
    SELECT dept_id
    FROM department
    WHERE location = 'Indore'
);


-- Q9. Departments having no employees.

SELECT *
FROM department
WHERE dept_id NOT IN (
    SELECT dept_id
    FROM employee
);


-- Q10. Employees earning more than average IT department salary.

SELECT *
FROM employee
WHERE salary > (
    SELECT AVG(e.salary)
    FROM employee e
    WHERE e.dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name = 'IT'
    )
);


-- Q11. Employees earning more than average Finance salary.

SELECT *
FROM employee
WHERE salary > (
    SELECT AVG(e.salary)
    FROM employee e
    WHERE e.dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name = 'Finance'
    )
);


-- Q12. Employees receiving the highest salary in IT.

SELECT *
FROM employee
WHERE dept_id = (
    SELECT dept_id
    FROM department
    WHERE dept_name = 'IT'
)
AND salary = (
    SELECT MAX(salary)
    FROM employee
    WHERE dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name = 'IT'
    )
);


-- Q13. Employees earning less than the lowest salary in Sales.

SELECT *
FROM employee
WHERE salary < (
    SELECT MIN(salary)
    FROM employee
    WHERE dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name = 'Sales'
    )
);


-- Q14. Employees earning more than at least one HR employee.

SELECT *
FROM employee
WHERE salary > ANY (
    SELECT e.salary
    FROM employee e
    WHERE e.dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name = 'HR'
    )
);


-- Q15. Employees earning more than every HR employee.

SELECT *
FROM employee
WHERE salary > ALL (
    SELECT e.salary
    FROM employee e
    WHERE e.dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name = 'HR'
    )
);


-- Q16. Employees earning less than at least one IT employee.

SELECT *
FROM employee
WHERE salary < ANY (
    SELECT e.salary
    FROM employee e
    WHERE e.dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name = 'IT'
    )
);


-- Q17. Employees earning more than every Finance employee.

SELECT *
FROM employee
WHERE salary > ALL (
    SELECT e.salary
    FROM employee e
    WHERE e.dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name = 'Finance'
    )
);


-- Q18. Employees earning less than every IT employee.

SELECT *
FROM employee
WHERE salary < ALL (
    SELECT e.salary
    FROM employee e
    WHERE e.dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name = 'IT'
    )
);


-- Q19. Employees earning more than their department average.

SELECT *
FROM employee e
WHERE salary > (
    SELECT AVG(e2.salary)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
);


-- Q20. Employees earning less than their department average.

SELECT *
FROM employee e
WHERE salary < (
    SELECT AVG(e2.salary)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
);


-- Q21. Employees earning exactly their department average.

SELECT *
FROM employee e
WHERE salary = (
    SELECT AVG(e2.salary)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
);


-- Q22. Highest-paid employee(s) from each department.

SELECT *
FROM employee e
WHERE salary = (
    SELECT MAX(e2.salary)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
);


-- Q23. Lowest-paid employee(s) from each department.

SELECT *
FROM employee e
WHERE salary = (
    SELECT MIN(e2.salary)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
);


-- Q24. Employees who are not the highest-paid in their department.

SELECT *
FROM employee e
WHERE salary < (
    SELECT MAX(e2.salary)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
);


-- Q25. Employees who are not the lowest-paid in their department.

SELECT *
FROM employee e
WHERE salary > (
    SELECT MIN(e2.salary)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
);



-- ============================================================
-- PART 2: RANKINGS, EXISTENCE & CORRELATED SUBQUERIES (Q26 - Q50)
-- ============================================================


-- Q26. Second-highest distinct salary without LIMIT.

SELECT MAX(salary) AS second_highest_salary
FROM employee
WHERE salary < (
    SELECT MAX(salary)
    FROM employee
);


-- Q27. Employee(s) having the second-highest distinct salary.

SELECT *
FROM employee
WHERE salary = (
    SELECT MAX(salary)
    FROM employee
    WHERE salary < (
        SELECT MAX(salary)
        FROM employee
    )
);


-- Q28. Third-highest distinct salary without LIMIT.

SELECT MAX(salary) AS third_highest_salary
FROM employee
WHERE salary < (
    SELECT MAX(salary)
    FROM employee
    WHERE salary < (
        SELECT MAX(salary)
        FROM employee
    )
);


-- Q29. Employee(s) having the third-highest distinct salary.

SELECT *
FROM employee
WHERE salary = (
    SELECT MAX(salary)
    FROM employee
    WHERE salary < (
        SELECT MAX(salary)
        FROM employee
        WHERE salary < (
            SELECT MAX(salary)
            FROM employee
        )
    )
);


-- Q30. Departments having at least one employee.

SELECT *
FROM department d
WHERE EXISTS (
    SELECT 1
    FROM employee e
    WHERE e.dept_id = d.dept_id
);


-- Q31. Departments having no employees.

SELECT *
FROM department d
WHERE NOT EXISTS (
    SELECT 1
    FROM employee e
    WHERE e.dept_id = d.dept_id
);


-- Q32. Departments where at least one employee earns more than 60000.

SELECT *
FROM department d
WHERE EXISTS (
    SELECT 1
    FROM employee e
    WHERE e.dept_id = d.dept_id
    AND e.salary > 60000
);


-- Q33. Departments where no employee earns more than 60000.

SELECT *
FROM department d
WHERE NOT EXISTS (
    SELECT 1
    FROM employee e
    WHERE e.dept_id = d.dept_id
    AND e.salary > 60000
);


-- Q34. Departments where at least one employee earns less than 30000.

SELECT *
FROM department d
WHERE EXISTS (
    SELECT 1
    FROM employee e
    WHERE e.dept_id = d.dept_id
    AND e.salary < 30000
);


-- Q35. Departments where no employee earns less than 30000.

SELECT *
FROM department d
WHERE NOT EXISTS (
    SELECT 1
    FROM employee e
    WHERE e.dept_id = d.dept_id
    AND e.salary < 30000
);


-- Q36. Employees belonging to an existing department.

SELECT *
FROM employee
WHERE dept_id IN (
    SELECT dept_id
    FROM department
);


-- Q37. Employees earning more than their department average.
-- Using correlated subquery.

SELECT *
FROM employee e
WHERE salary > (
    SELECT AVG(e2.salary)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
);


-- Q38. Employees earning the maximum salary of their department.
-- Using correlated subquery.

SELECT *
FROM employee e
WHERE salary = (
    SELECT MAX(e2.salary)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
);


-- Q39. Employees earning the minimum salary of their department.
-- Using correlated subquery.

SELECT *
FROM employee e
WHERE salary = (
    SELECT MIN(e2.salary)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
);


-- Q40. Each employee with department average salary.

SELECT
    emp_id,
    emp_name,
    salary,
    dept_id,
    (
        SELECT AVG(e2.salary)
        FROM employee e2
        WHERE e2.dept_id = e.dept_id
    ) AS department_average_salary
FROM employee e;


-- Q41. Each employee with department highest salary.

SELECT
    emp_id,
    emp_name,
    salary,
    dept_id,
    (
        SELECT MAX(e2.salary)
        FROM employee e2
        WHERE e2.dept_id = e.dept_id
    ) AS department_highest_salary
FROM employee e;


-- Q42. Each employee with department lowest salary.

SELECT
    emp_id,
    emp_name,
    salary,
    dept_id,
    (
        SELECT MIN(e2.salary)
        FROM employee e2
        WHERE e2.dept_id = e.dept_id
    ) AS department_lowest_salary
FROM employee e;


-- Q43. Each employee with company average salary.

SELECT
    emp_id,
    emp_name,
    salary,
    (
        SELECT AVG(salary)
        FROM employee
    ) AS company_average_salary
FROM employee;


-- Q44. Each employee with difference from company average.

SELECT
    emp_id,
    emp_name,
    salary,
    salary - (
        SELECT AVG(salary)
        FROM employee
    ) AS salary_difference
FROM employee;


-- Q45. Employee details with department name using subquery.

SELECT
    emp_id,
    emp_name,
    salary,
    (
        SELECT dept_name
        FROM department d
        WHERE d.dept_id = e.dept_id
    ) AS dept_name
FROM employee e;


-- Q46. Departments whose average salary is greater than company average.

SELECT
    d.dept_id,
    d.dept_name
FROM department d
WHERE (
    SELECT AVG(e.salary)
    FROM employee e
    WHERE e.dept_id = d.dept_id
) > (
    SELECT AVG(salary)
    FROM employee
);


-- Q47. Departments whose average salary is less than company average.

SELECT
    d.dept_id,
    d.dept_name
FROM department d
WHERE (
    SELECT AVG(e.salary)
    FROM employee e
    WHERE e.dept_id = d.dept_id
) < (
    SELECT AVG(salary)
    FROM employee
);


-- Q48. Department(s) having the highest average salary.

SELECT
    d.dept_id,
    d.dept_name,
    (
        SELECT AVG(e.salary)
        FROM employee e
        WHERE e.dept_id = d.dept_id
    ) AS average_salary
FROM department d
WHERE (
    SELECT AVG(e.salary)
    FROM employee e
    WHERE e.dept_id = d.dept_id
) = (
    SELECT MAX(dept_avg)
    FROM (
        SELECT AVG(salary) AS dept_avg
        FROM employee
        GROUP BY dept_id
    ) AS department_averages
);


-- Q49. Department(s) having the lowest average salary.

SELECT
    d.dept_id,
    d.dept_name,
    (
        SELECT AVG(e.salary)
        FROM employee e
        WHERE e.dept_id = d.dept_id
    ) AS average_salary
FROM department d
WHERE (
    SELECT AVG(e.salary)
    FROM employee e
    WHERE e.dept_id = d.dept_id
) = (
    SELECT MIN(dept_avg)
    FROM (
        SELECT AVG(salary) AS dept_avg
        FROM employee
        GROUP BY dept_id
    ) AS department_averages
);


-- Q50. Employees working in the department having the highest average salary.

SELECT *
FROM employee
WHERE dept_id IN (
    SELECT dept_id
    FROM employee
    GROUP BY dept_id
    HAVING AVG(salary) = (
        SELECT MAX(dept_avg)
        FROM (
            SELECT AVG(salary) AS dept_avg
            FROM employee
            GROUP BY dept_id
        ) AS department_averages
    )
);



-- ============================================================
-- PART 3: ADVANCED DEPARTMENTAL & SALARY AGGREGATIONS (Q51 - Q80)
-- ============================================================


-- Q51. Employees working in the department having the lowest average salary.

SELECT *
FROM employee
WHERE dept_id IN (
    SELECT dept_id
    FROM employee
    GROUP BY dept_id
    HAVING AVG(salary) = (
        SELECT MIN(dept_avg)
        FROM (
            SELECT AVG(salary) AS dept_avg
            FROM employee
            GROUP BY dept_id
        ) AS department_averages
    )
);


-- Q52. Departments having more employees than average employees per department.
-- Includes departments having zero employees in the average calculation.

SELECT
    d.dept_id,
    d.dept_name
FROM department d
WHERE (
    SELECT COUNT(*)
    FROM employee e
    WHERE e.dept_id = d.dept_id
) > (
    SELECT AVG(employee_count)
    FROM (
        SELECT
            d2.dept_id,
            COUNT(e2.emp_id) AS employee_count
        FROM department d2
        LEFT JOIN employee e2
            ON e2.dept_id = d2.dept_id
        GROUP BY d2.dept_id
    ) AS department_counts
);


-- Q53. Departments where every employee earns more than 30000.
-- Empty departments also satisfy this condition.

SELECT *
FROM department d
WHERE NOT EXISTS (
    SELECT 1
    FROM employee e
    WHERE e.dept_id = d.dept_id
    AND e.salary <= 30000
);


-- Q54. Departments having at least one employee earning > 50000
-- and at least one employee earning < 35000.

SELECT *
FROM department d
WHERE EXISTS (
    SELECT 1
    FROM employee e
    WHERE e.dept_id = d.dept_id
    AND e.salary > 50000
)
AND EXISTS (
    SELECT 1
    FROM employee e
    WHERE e.dept_id = d.dept_id
    AND e.salary < 35000
);


-- Q55. Departments where every employee earns less than 70000.
-- Empty departments also satisfy this condition.

SELECT *
FROM department d
WHERE NOT EXISTS (
    SELECT 1
    FROM employee e
    WHERE e.dept_id = d.dept_id
    AND e.salary >= 70000
);


-- Q56. Employees earning more than the average of all department averages.

SELECT *
FROM employee
WHERE salary > (
    SELECT AVG(dept_avg)
    FROM (
        SELECT AVG(salary) AS dept_avg
        FROM employee
        GROUP BY dept_id
    ) AS department_averages
);


-- Q57. Department(s) whose maximum salary is highest among departments.

SELECT
    d.dept_id,
    d.dept_name
FROM department d
WHERE (
    SELECT MAX(e.salary)
    FROM employee e
    WHERE e.dept_id = d.dept_id
) = (
    SELECT MAX(salary)
    FROM employee
);


-- Q58. Department(s) whose minimum salary is lowest among departments.

SELECT
    d.dept_id,
    d.dept_name
FROM department d
WHERE (
    SELECT MIN(e.salary)
    FROM employee e
    WHERE e.dept_id = d.dept_id
) = (
    SELECT MIN(salary)
    FROM employee
);


-- Q59. Employees earning more than the maximum HR salary.

SELECT *
FROM employee
WHERE salary > (
    SELECT MAX(e.salary)
    FROM employee e
    WHERE e.dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name = 'HR'
    )
);


-- Q60. Employees earning less than the minimum Finance salary.

SELECT *
FROM employee
WHERE salary < (
    SELECT MIN(e.salary)
    FROM employee e
    WHERE e.dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name = 'Finance'
    )
);


-- Q61. Employees earning more than every HR employee
-- but less than at least one IT employee.

SELECT *
FROM employee
WHERE salary > ALL (
    SELECT e.salary
    FROM employee e
    WHERE e.dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name = 'HR'
    )
)
AND salary < ANY (
    SELECT e.salary
    FROM employee e
    WHERE e.dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name = 'IT'
    )
);


-- Q62. Employees earning more than at least one Finance employee
-- but less than every IT employee.

SELECT *
FROM employee
WHERE salary > ANY (
    SELECT e.salary
    FROM employee e
    WHERE e.dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name = 'Finance'
    )
)
AND salary < ALL (
    SELECT e.salary
    FROM employee e
    WHERE e.dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name = 'IT'
    )
);


-- Q63. Employees working in departments whose average salary > 40000.

SELECT *
FROM employee
WHERE dept_id IN (
    SELECT dept_id
    FROM employee
    GROUP BY dept_id
    HAVING AVG(salary) > 40000
);


-- Q64. Departments whose average salary > 40000
-- and at least one employee earns > 60000.

SELECT *
FROM department d
WHERE (
    SELECT AVG(e.salary)
    FROM employee e
    WHERE e.dept_id = d.dept_id
) > 40000
AND EXISTS (
    SELECT 1
    FROM employee e
    WHERE e.dept_id = d.dept_id
    AND e.salary > 60000
);


-- Q65. Employees earning more than department average
-- but less than company average.

SELECT *
FROM employee e
WHERE salary > (
    SELECT AVG(e2.salary)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
)
AND salary < (
    SELECT AVG(salary)
    FROM employee
);


-- Q66. Employees earning less than department average
-- but greater than company average.

SELECT *
FROM employee e
WHERE salary < (
    SELECT AVG(e2.salary)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
)
AND salary > (
    SELECT AVG(salary)
    FROM employee
);


-- Q67. Highest-paid employee(s) from each department
-- without GROUP BY to directly select the employee.

SELECT *
FROM employee e
WHERE NOT EXISTS (
    SELECT 1
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
    AND e2.salary > e.salary
);


-- Q68. Second-highest distinct salary employee from each department.

SELECT *
FROM employee e
WHERE 1 = (
    SELECT COUNT(DISTINCT e2.salary)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
    AND e2.salary > e.salary
);


-- Q69. Departments having at least two employees.

SELECT *
FROM department d
WHERE (
    SELECT COUNT(*)
    FROM employee e
    WHERE e.dept_id = d.dept_id
) >= 2;


-- Q70. Employees working in departments having more employees than HR.

SELECT *
FROM employee
WHERE dept_id IN (
    SELECT dept_id
    FROM employee
    GROUP BY dept_id
    HAVING COUNT(*) > (
        SELECT COUNT(*)
        FROM employee
        WHERE dept_id = (
            SELECT dept_id
            FROM department
            WHERE dept_name = 'HR'
        )
    )
);


-- Q71. Employees working in departments having fewer employees than IT.

SELECT *
FROM employee
WHERE dept_id IN (
    SELECT dept_id
    FROM employee
    GROUP BY dept_id
    HAVING COUNT(*) < (
        SELECT COUNT(*)
        FROM employee
        WHERE dept_id = (
            SELECT dept_id
            FROM department
            WHERE dept_name = 'IT'
        )
    )
);


-- Q72. Departments having the same average salary as Finance.

SELECT
    d.dept_id,
    d.dept_name
FROM department d
WHERE (
    SELECT AVG(e.salary)
    FROM employee e
    WHERE e.dept_id = d.dept_id
) = (
    SELECT AVG(e.salary)
    FROM employee e
    WHERE e.dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name = 'Finance'
    )
);


-- Q73. Employees whose salary equals the highest salary
-- of any department other than their own.

SELECT *
FROM employee e
WHERE salary = (
    SELECT MAX(e2.salary)
    FROM employee e2
    WHERE e2.dept_id <> e.dept_id
);


-- Q74. Employees earning more than the average salary of every department.

SELECT *
FROM employee
WHERE salary > ALL (
    SELECT AVG(salary)
    FROM employee
    GROUP BY dept_id
);


-- Q75. Employees earning more than the average salary of at least one department.

SELECT *
FROM employee
WHERE salary > ANY (
    SELECT AVG(salary)
    FROM employee
    GROUP BY dept_id
);


-- Q76. Employee(s) whose salary is closest to company average.

SELECT *
FROM employee
WHERE ABS(
    salary - (SELECT AVG(salary) FROM employee)
) = (
    SELECT MIN(
        ABS(salary - (SELECT AVG(salary) FROM employee))
    )
    FROM employee
);


-- Q77. Department(s) whose average salary is closest to company average.

SELECT
    d.dept_id,
    d.dept_name,
    (
        SELECT AVG(e.salary)
        FROM employee e
        WHERE e.dept_id = d.dept_id
    ) AS department_average_salary
FROM department d
WHERE ABS(
    (
        SELECT AVG(e.salary)
        FROM employee e
        WHERE e.dept_id = d.dept_id
    )
    -
    (SELECT AVG(salary) FROM employee)
) = (
    SELECT MIN(
        ABS(dept_avg - (SELECT AVG(salary) FROM employee))
    )
    FROM (
        SELECT AVG(salary) AS dept_avg
        FROM employee
        GROUP BY dept_id
    ) AS department_averages
);


-- Q78. Employees earning more than company average
-- but not the highest-paid employee in the company.

SELECT *
FROM employee
WHERE salary > (
    SELECT AVG(salary)
    FROM employee
)
AND salary < (
    SELECT MAX(salary)
    FROM employee
);


-- Q79. Employees earning more than department average
-- and working in departments having at least two employees.

SELECT *
FROM employee e
WHERE salary > (
    SELECT AVG(e2.salary)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
)
AND (
    SELECT COUNT(*)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
) >= 2;


-- Q80. Employees satisfying all four conditions:
-- 1. Salary > company average.
-- 2. Salary > department average.
-- 3. Department has at least two employees.
-- 4. Not the highest-paid employee in company.

SELECT *
FROM employee e
WHERE salary > (
    SELECT AVG(salary)
    FROM employee
)
AND salary > (
    SELECT AVG(e2.salary)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
)
AND (
    SELECT COUNT(*)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
) >= 2
AND salary < (
    SELECT MAX(salary)
    FROM employee
);



-- ============================================================
-- CHALLENGE QUESTIONS (Q81 - Q90)
-- ============================================================


-- Q81. Department having the second-highest distinct average salary.

SELECT
    d.dept_id,
    d.dept_name,
    (
        SELECT AVG(e.salary)
        FROM employee e
        WHERE e.dept_id = d.dept_id
    ) AS average_salary
FROM department d
WHERE (
    SELECT AVG(e.salary)
    FROM employee e
    WHERE e.dept_id = d.dept_id
) = (
    SELECT MAX(dept_avg)
    FROM (
        SELECT AVG(salary) AS dept_avg
        FROM employee
        GROUP BY dept_id
    ) AS department_averages
    WHERE dept_avg < (
        SELECT MAX(dept_avg)
        FROM (
            SELECT AVG(salary) AS dept_avg
            FROM employee
            GROUP BY dept_id
        ) AS all_department_averages
    )
);


-- Q82. Employees working in the department having
-- the second-highest distinct average salary.

SELECT *
FROM employee
WHERE dept_id IN (
    SELECT dept_id
    FROM employee
    GROUP BY dept_id
    HAVING AVG(salary) = (
        SELECT MAX(dept_avg)
        FROM (
            SELECT AVG(salary) AS dept_avg
            FROM employee
            GROUP BY dept_id
        ) AS department_averages
        WHERE dept_avg < (
            SELECT MAX(dept_avg)
            FROM (
                SELECT AVG(salary) AS dept_avg
                FROM employee
                GROUP BY dept_id
            ) AS all_department_averages
        )
    )
);


-- Q83. Second-highest distinct salary employee from every department.

SELECT *
FROM employee e
WHERE (
    SELECT COUNT(DISTINCT e2.salary)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
    AND e2.salary > e.salary
) = 1;


-- Q84. Department(s) having the second-highest distinct maximum salary.

SELECT
    d.dept_id,
    d.dept_name,
    (
        SELECT MAX(e.salary)
        FROM employee e
        WHERE e.dept_id = d.dept_id
    ) AS department_maximum_salary
FROM department d
WHERE (
    SELECT MAX(e.salary)
    FROM employee e
    WHERE e.dept_id = d.dept_id
) = (
    SELECT MAX(dept_max)
    FROM (
        SELECT MAX(salary) AS dept_max
        FROM employee
        GROUP BY dept_id
    ) AS department_maximums
    WHERE dept_max < (
        SELECT MAX(dept_max)
        FROM (
            SELECT MAX(salary) AS dept_max
            FROM employee
            GROUP BY dept_id
        ) AS all_department_maximums
    )
);


-- Q85. Employees earning more than the average salary
-- of the department having the second-highest average salary.

SELECT *
FROM employee
WHERE salary > (
    SELECT MAX(dept_avg)
    FROM (
        SELECT AVG(salary) AS dept_avg
        FROM employee
        GROUP BY dept_id
    ) AS department_averages
    WHERE dept_avg < (
        SELECT MAX(dept_avg)
        FROM (
            SELECT AVG(salary) AS dept_avg
            FROM employee
            GROUP BY dept_id
        ) AS all_department_averages
    )
);


-- Q86. Employee(s) whose salary is closest to the highest salary
-- without being the highest-paid employee.

SELECT *
FROM employee
WHERE salary = (
    SELECT MAX(salary)
    FROM employee
    WHERE salary < (
        SELECT MAX(salary)
        FROM employee
    )
);


-- Q87. Departments where salary difference between highest
-- and lowest salary is greater than 30000.

SELECT
    d.dept_id,
    d.dept_name
FROM department d
WHERE (
    SELECT MAX(e.salary)
    FROM employee e
    WHERE e.dept_id = d.dept_id
) - (
    SELECT MIN(e.salary)
    FROM employee e
    WHERE e.dept_id = d.dept_id
) > 30000;


-- Q88. Employees earning above department average
-- with a difference greater than 10000.

SELECT *
FROM employee e
WHERE salary - (
    SELECT AVG(e2.salary)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
) > 10000;


-- Q89. Departments where highest-paid employee earns
-- more than the highest-paid HR employee.

SELECT *
FROM department d
WHERE (
    SELECT MAX(e.salary)
    FROM employee e
    WHERE e.dept_id = d.dept_id
) > (
    SELECT MAX(e.salary)
    FROM employee e
    WHERE e.dept_id = (
        SELECT dept_id
        FROM department
        WHERE dept_name = 'HR'
    )
);


-- Q90. Employees earning more than every employee
-- in HR, Finance and Sales.

SELECT *
FROM employee
WHERE salary > ALL (
    SELECT e.salary
    FROM employee e
    WHERE e.dept_id IN (
        SELECT dept_id
        FROM department
        WHERE dept_name IN ('HR', 'Finance', 'Sales')
    )
);



-- ============================================================
-- FINAL INTERVIEW CHALLENGE (Q91 - Q100)
-- ============================================================


-- Q91. Third-highest distinct salary employee.
-- Restrictions: No JOIN, LIMIT or WINDOW FUNCTIONS.

SELECT *
FROM employee e
WHERE 2 = (
    SELECT COUNT(DISTINCT e2.salary)
    FROM employee e2
    WHERE e2.salary > e.salary
);


-- Q92. Second-highest distinct salary employee in each department.
-- Restrictions: No LIMIT or WINDOW FUNCTIONS.

SELECT *
FROM employee e
WHERE 1 = (
    SELECT COUNT(DISTINCT e2.salary)
    FROM employee e2
    WHERE e2.dept_id = e.dept_id
    AND e2.salary > e.salary
);


-- -- Q93. Departments where every employee earns
-- -- more than company average salary.
-- -- Requires at least one employee in the department.

-- SELECT *
-- FROM department d
-- WHERE EXISTS (
--     SELECT 1
--     FROM employee e
--     WHERE e.dept_id = d.dept_id
-- )
-- AND NOT EXISTS (
--     SELECT 1
--     FROM employee e
--     WHERE e.dept_id = d.dept_id
--     AND e.salary <= (
--         SELECT AVG(salary)
--         FROM employee
--     )
-- );


-- -- Q94. Departments where at least one employee earns
-- -- more than company average and at least one earns less.

-- SELECT *
-- FROM department d
-- WHERE EXISTS (
--     SELECT 1
--     FROM employee e
--     WHERE e.dept_id = d.dept_id
--     AND e.salary > (
--         SELECT AVG(salary)
--         FROM employee
--     )
-- )
-- AND EXISTS (
--     SELECT 1
--     FROM employee e
--     WHERE e.dept_id = d.dept_id
--     AND e.salary < (
--         SELECT AVG(salary)
--         FROM employee
--     )
-- );


-- -- Q95. Employees satisfying all three conditions:
-- -- 1. Salary > department average.
-- -- 2. Salary > company average.
-- -- 3. Salary < highest company salary.

-- SELECT *
-- FROM employee e
-- WHERE salary > (
--     SELECT AVG(e2.salary)
--     FROM employee e2
--     WHERE e2.dept_id = e.dept_id
-- )
-- AND salary > (
--     SELECT AVG(salary)
--     FROM employee
-- )
-- AND salary < (
--     SELECT MAX(salary)
--     FROM employee
-- );


-- -- Q96. Department having highest average salary
-- -- and all employees belonging to that department.

-- SELECT *
-- FROM employee
-- WHERE dept_id IN (
--     SELECT dept_id
--     FROM employee
--     GROUP BY dept_id
--     HAVING AVG(salary) = (
--         SELECT MAX(dept_avg)
--         FROM (
--             SELECT AVG(salary) AS dept_avg
--             FROM employee
--             GROUP BY dept_id
--         ) AS department_averages
--     )
-- );


-- -- Q97. Department having lowest average salary
-- -- and all employees belonging to that department.

-- SELECT *
-- FROM employee
-- WHERE dept_id IN (
--     SELECT dept_id
--     FROM employee
--     GROUP BY dept_id
--     HAVING AVG(salary) = (
--         SELECT MIN(dept_avg)
--         FROM (
--             SELECT AVG(salary) AS dept_avg
--             FROM employee
--             GROUP BY dept_id
--         ) AS department_averages
--     )
-- );


-- -- Q98. Department having the highest number of employees
-- -- and all employees belonging to that department.

-- SELECT *
-- FROM employee
-- WHERE dept_id IN (
--     SELECT dept_id
--     FROM employee
--     GROUP BY dept_id
--     HAVING COUNT(*) = (
--         SELECT MAX(employee_count)
--         FROM (
--             SELECT COUNT(*) AS employee_count
--             FROM employee
--             GROUP BY dept_id
--         ) AS department_counts
--     )
-- );


-- -- Q99. Department having the lowest number of employees,
-- -- excluding departments with zero employees,
-- -- and all employees belonging to that department.

-- SELECT *
-- FROM employee
-- WHERE dept_id IN (
--     SELECT dept_id
--     FROM employee
--     GROUP BY dept_id
--     HAVING COUNT(*) = (
--         SELECT MIN(employee_count)
--         FROM (
--             SELECT COUNT(*) AS employee_count
--             FROM employee
--             GROUP BY dept_id
--         ) AS department_counts
--     )
-- );


-- -- Q100. Employees satisfying all four conditions:
-- -- 1. Salary > department average.
-- -- 2. Salary > company average.
-- -- 3. Employee is not highest-paid in department.
-- -- 4. Department has at least two employees.

-- SELECT *
-- FROM employee e
-- WHERE salary > (
--     SELECT AVG(e2.salary)
--     FROM employee e2
--     WHERE e2.dept_id = e.dept_id
-- )
-- AND salary > (
--     SELECT AVG(salary)
--     FROM employee
-- )
-- AND salary < (
--     SELECT MAX(e2.salary)
--     FROM employee e2
--     WHERE e2.dept_id = e.dept_id
-- )
-- AND (
--     SELECT COUNT(*)
--     FROM employee e2
--     WHERE e2.dept_id = e.dept_id
-- ) >= 2;


-- --