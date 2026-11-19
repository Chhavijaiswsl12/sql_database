mysql> create table staff_update
    -> staff_id int primary key auto_increment
    -> staff_name varchar(50)
    -> department varchar(30)
    -> city varchar(30)
    -> city varchar(30)^C
mysql> create table staff_update
    -> (staff_id int primary key auto_increment
    -> , staff_name varchar(50),
    -> department varchar(30),
    -> city varchar(30),
    -> salary DECIMAL(10,2)
    -> ,experience INT,
    -> age INT,
    -> joining_date DATE,
    -> status  VARCHAR(20))
    -> ;
Query OK, 0 rows affected (0.13 sec)

mysql> insert into staff_update(staff_name,department,city,salary,experience,age,joining_date,status) values
    -> ('Aarav', 'IT', 'Indore', 48000, 3, 26, '2022-04-15', 'Active'),
    -> ('Bhavna', 'HR', 'Bhopal', 56000, 5, 31, '2020-08-20', 'Active'),
    -> ('Chetan', 'Finance', 'Delhi', 62000, 7, 35, '2018-03-10', 'Active'),
    -> ('Divya', 'IT', 'Pune', 78000, 9, 38, '2016-11-05', 'Active'),
    -> ('Eshan', 'Sales', 'Indore', 51000, 4, 29, '2021-06-18', 'Inactive'),
    -> ('Farah', 'HR', NULL, 68000, 6, 34, '2019-01-25', 'Active');
Query OK, 6 rows affected (0.17 sec)
Records: 6  Duplicates: 0  Warnings: 0

mysql> update staff_update set salary=52000 where staff_id=1;
Query OK, 1 row affected (0.05 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from staff_update;
+----------+------------+------------+--------+----------+------------+------+--------------+----------+
| staff_id | staff_name | department | city   | salary   | experience | age  | joining_date | status   |
+----------+------------+------------+--------+----------+------------+------+--------------+----------+
|        1 | Aarav      | IT         | Indore | 52000.00 |          3 |   26 | 2022-04-15   | Active   |
|        2 | Bhavna     | HR         | Bhopal | 56000.00 |          5 |   31 | 2020-08-20   | Active   |
|        3 | Chetan     | Finance    | Delhi  | 62000.00 |          7 |   35 | 2018-03-10   | Active   |
|        4 | Divya      | IT         | Pune   | 78000.00 |          9 |   38 | 2016-11-05   | Active   |
|        5 | Eshan      | Sales      | Indore | 51000.00 |          4 |   29 | 2021-06-18   | Inactive |
|        6 | Farah      | HR         | NULL   | 68000.00 |          6 |   34 | 2019-01-25   | Active   |
+----------+------------+------------+--------+----------+------------+------+--------------+----------+
6 rows in set (0.01 sec)

mysql> update staff_update set department='finance' , city='indore' where staff_name='bhavna';
Query OK, 1 row affected (0.03 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from staff_update;
+----------+------------+------------+--------+----------+------------+------+--------------+----------+
| staff_id | staff_name | department | city   | salary   | experience | age  | joining_date | status   |
+----------+------------+------------+--------+----------+------------+------+--------------+----------+
|        1 | Aarav      | IT         | Indore | 52000.00 |          3 |   26 | 2022-04-15   | Active   |
|        2 | Bhavna     | finance    | indore | 56000.00 |          5 |   31 | 2020-08-20   | Active   |
|        3 | Chetan     | Finance    | Delhi  | 62000.00 |          7 |   35 | 2018-03-10   | Active   |
|        4 | Divya      | IT         | Pune   | 78000.00 |          9 |   38 | 2016-11-05   | Active   |
|        5 | Eshan      | Sales      | Indore | 51000.00 |          4 |   29 | 2021-06-18   | Inactive |
|        6 | Farah      | HR         | NULL   | 68000.00 |          6 |   34 | 2019-01-25   | Active   |
+----------+------------+------------+--------+----------+------------+------+--------------+----------+
6 rows in set (0.00 sec)

mysql> update staff_update set salary=salary+4000 where salary<60000 and experience>=3 and department !='sales';
Query OK, 2 rows affected (0.01 sec)
Rows matched: 2  Changed: 2  Warnings: 0

mysql> select * from staff_update;
+----------+------------+------------+--------+----------+------------+------+--------------+----------+
| staff_id | staff_name | department | city   | salary   | experience | age  | joining_date | status   |
+----------+------------+------------+--------+----------+------------+------+--------------+----------+
|        1 | Aarav      | IT         | Indore | 56000.00 |          3 |   26 | 2022-04-15   | Active   |
|        2 | Bhavna     | finance    | indore | 60000.00 |          5 |   31 | 2020-08-20   | Active   |
|        3 | Chetan     | Finance    | Delhi  | 62000.00 |          7 |   35 | 2018-03-10   | Active   |
|        4 | Divya      | IT         | Pune   | 78000.00 |          9 |   38 | 2016-11-05   | Active   |
|        5 | Eshan      | Sales      | Indore | 51000.00 |          4 |   29 | 2021-06-18   | Inactive |
|        6 | Farah      | HR         | NULL   | 68000.00 |          6 |   34 | 2019-01-25   | Active   |
+----------+------------+------------+--------+----------+------------+------+--------------+----------+
6 rows in set (0.00 sec)

mysql> update staff_update set salary=salary+3000 where department='it' and experience>=3 or department='hr' and experience>=5;
Query OK, 3 rows affected (0.02 sec)
Rows matched: 3  Changed: 3  Warnings: 0

mysql> select * from staff_update;
+----------+------------+------------+--------+----------+------------+------+--------------+----------+
| staff_id | staff_name | department | city   | salary   | experience | age  | joining_date | status   |
+----------+------------+------------+--------+----------+------------+------+--------------+----------+
|        1 | Aarav      | IT         | Indore | 59000.00 |          3 |   26 | 2022-04-15   | Active   |
|        2 | Bhavna     | finance    | indore | 60000.00 |          5 |   31 | 2020-08-20   | Active   |
|        3 | Chetan     | Finance    | Delhi  | 62000.00 |          7 |   35 | 2018-03-10   | Active   |
|        4 | Divya      | IT         | Pune   | 81000.00 |          9 |   38 | 2016-11-05   | Active   |
|        5 | Eshan      | Sales      | Indore | 51000.00 |          4 |   29 | 2021-06-18   | Inactive |
|        6 | Farah      | HR         | NULL   | 71000.00 |          6 |   34 | 2019-01-25   | Active   |
+----------+------------+------------+--------+----------+------------+------+--------------+----------+
6 rows in set (0.00 sec)

mysql> update staff_update set salary=salary*1.1 where department in('it','finanace') and salary<70000;
Query OK, 1 row affected (0.03 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from staff_update;
+----------+------------+------------+--------+----------+------------+------+--------------+----------+
| staff_id | staff_name | department | city   | salary   | experience | age  | joining_date | status   |
+----------+------------+------------+--------+----------+------------+------+--------------+----------+
|        1 | Aarav      | IT         | Indore | 64900.00 |          3 |   26 | 2022-04-15   | Active   |
|        2 | Bhavna     | finance    | indore | 60000.00 |          5 |   31 | 2020-08-20   | Active   |
|        3 | Chetan     | Finance    | Delhi  | 62000.00 |          7 |   35 | 2018-03-10   | Active   |
|        4 | Divya      | IT         | Pune   | 81000.00 |          9 |   38 | 2016-11-05   | Active   |
|        5 | Eshan      | Sales      | Indore | 51000.00 |          4 |   29 | 2021-06-18   | Inactive |
|        6 | Farah      | HR         | NULL   | 71000.00 |          6 |   34 | 2019-01-25   | Active   |
+----------+------------+------------+--------+----------+------------+------+--------------+----------+
6 rows in set (0.00 sec)

mysql> update staff_update set salary=salary+2500 where department not in('hr' or 'sales') and experience between 5 and 8;
ERROR 1292 (22007): Truncated incorrect DOUBLE value: 'hr'
mysql> update staff_update set salary=salary+2500 where department not in('hr' ,'sales') and experience between 5 and 8;
Query OK, 2 rows affected (0.03 sec)
Rows matched: 2  Changed: 2  Warnings: 0

mysql> select * from staff_update;
+----------+------------+------------+--------+----------+------------+------+--------------+----------+
| staff_id | staff_name | department | city   | salary   | experience | age  | joining_date | status   |
+----------+------------+------------+--------+----------+------------+------+--------------+----------+
|        1 | Aarav      | IT         | Indore | 64900.00 |          3 |   26 | 2022-04-15   | Active   |
|        2 | Bhavna     | finance    | indore | 62500.00 |          5 |   31 | 2020-08-20   | Active   |
|        3 | Chetan     | Finance    | Delhi  | 64500.00 |          7 |   35 | 2018-03-10   | Active   |
|        4 | Divya      | IT         | Pune   | 81000.00 |          9 |   38 | 2016-11-05   | Active   |
|        5 | Eshan      | Sales      | Indore | 51000.00 |          4 |   29 | 2021-06-18   | Inactive |
|        6 | Farah      | HR         | NULL   | 71000.00 |          6 |   34 | 2019-01-25   | Active   |
+----------+------------+------------+--------+----------+------------+------+--------------+----------+
6 rows in set (0.00 sec)
