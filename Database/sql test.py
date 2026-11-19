Employee Management System(3.5)

Write SQL queries for all the following questions using the employees table and sample data provided below.

Table: employees

Columns: employee_id, employee_name, department, city, salary, joining_date, experience, age, gender,
 employment_type, skills, email, manager_id

Sample Data

| employee_id | employee_name | department | city | salary | joining_date | experience | age | gender | employment_type | skills | email | manager_id |
|---:|---|---|---|---:|---|---:|---:|---|---|---|---|---:|
| 101 | Amit Sharma | IT | Indore | 75000 | 2023-05-10 | 5 | 30 | MALE | FULL_TIME | JAVA,SQL,SPRING | amit@company.com | 501 |
| 102 | Sneha Patel | Finance | Pune | 65000 | 2024-02-15 | 4 | 28 | FEMALE | FULL_TIME | SQL,PYTHON | sneha@company.com | 502 |
| 103 | Rahul Verma | Development | Delhi | 85000 | 2022-08-20 | 7 | 32 | MALE | FULL_TIME | JAVA,SQL,REACT | rahul@company.com | 501 |
| 104 | Anjali Gupta | HR | Mumbai | 35000 | 2023-11-01 | 3 | 27 | FEMALE | CONTRACT | SQL | NULL | 503 |
| 105 | Suresh Kumar | IT | Bhopal | 28000 | 2021-06-12 | 6 | 35 | MALE | FULL_TIME | JAVA,SPRING | NULL | NULL |
| 106 | Priya Singh | Development | Indore | 95000 | 2025-01-10 | 4 | 29 | FEMALE | FULL_TIME | PYTHON,REACT,SQL | priya@company.com | 501 |
| 107 | Arjun Mehta | Finance | Delhi | 45000 | 2022-03-25 | 3 | 26 | MALE | PART_TIME | SQL,PYTHON | arjun@company.com | NULL |
| 108 | Simran Kaur | IT | Pune | 55000 | 2024-07-18 | 5 | 31 | FEMALE | FULL_TIME | JAVA,SQL,REACT | simran@company.com | 504 |

Note: The skills column is a MySQL SET column. Use appropriate conditions to check individual skills.

Questions

Q1. (0.5 Marks)

Display employees belonging to IT, Finance, or Development whose salary is between ₹40,000 and ₹90,000, experience is greater than 3 years, email and manager ID are both NOT NULL, and city is neither Mumbai nor Bhopal.

Q2. (0.5 Marks)

Display employees whose names start with 'A' or contain the letter 'a', who joined after '2023-01-01', and whose salary is greater than ₹50,000 OR experience is greater than 6 years. Exclude employees from HR and Mumbai.

Q3. (0.5 Marks)

Display FULL_TIME employees from IT or Development who have *both JAVA and SQL skills or both PYTHON and REACT skills*, earn mosalaryre than ₹60,000, and have a non-NULL email.

Q4. (0.5 Marks)

Display employees from IT, Finance, or HR whose age is between 25 and 40, salary is NOT between ₹30,000 and ₹60,000, experience is greater than 2 years, and city is neither Mumbai nor Bhopal.

Q5. (0.5 Marks)

Display employees who joined between '2022-01-01' and '2025-12-31', have JAVA or PYTHON skills, earn more than ₹45,000, and have either email or manager ID as NULL. Their experience must be greater than 3 years.

Q6. (0.5 Marks)

Display employees whose names start with 'S' or contain the letter 'a', belong to IT or Finance, earn between ₹40,000 and ₹1,00,000, have more than 2 years of experience, and have both email and manager ID NOT NULL. They must have JAVA or PYTHON skills. Display the results ordered by department in ascending order and salary in descending order.

NOTE: Table creation and insertion will be .5 marks

=====================================


(101, 'Amit Sharma', 'IT', 'Indore', 75000, '2023-05-10', 5, 30, 'MALE', 'FULL_TIME', 'JAVA,SQL,SPRING', 'amit@company.com', 501),

(102, 'Sneha Patel', 'Finance', 'Pune', 65000, '2024-02-15', 4, 28, 'FEMALE', 'FULL_TIME', 'SQL,PYTHON', 'sneha@company.com', 502),

(103, 'Rahul Verma', 'Development', 'Delhi', 85000, '2022-08-20', 7, 32, 'MALE', 'FULL_TIME', 'JAVA,SQL,REACT', 'rahul@company.com', 501),

(104, 'Anjali Gupta', 'HR', 'Mumbai', 35000, '2023-11-01', 3, 27, 'FEMALE', 'CONTRACT', 'SQL', NULL, 503),

(105, 'Suresh Kumar', 'IT', 'Bhopal', 28000, '2021-06-12', 6, 35, 'MALE', 'FULL_TIME', 'JAVA,SPRING', NULL, NULL),

(106, 'Priya Singh', 'Development', 'Indore', 95000, '2025-01-10', 4, 29, 'FEMALE', 'FULL_TIME', 'PYTHON,REACT,SQL', 'priya@company.com', 501),

(107, 'Arjun Mehta', 'Finance', 'Delhi', 45000, '2022-03-25', 3, 26, 'MALE', 'PART_TIME', 'SQL,PYTHON', 'arjun@company.com', NULL),

(108, 'Simran Kaur', 'IT', 'Pune', 55000, '2024-07-18', 5, 31, 'FEMALE', 'FULL_TIME', 'JAVA,SQL,REACT', 'simran@company.com', 504);

 create table employees(employee_id int primary key,employee_name varchar(30),department varchar(20), city varchar(30), salary int,
    -> joining_date date, experience int, age int, gender enum('male','female'), employment_type varchar(30), skills set('java','sql','spring','python','react'), email varchar(30), manage_id int);
Query OK, 0 rows affected (0.15 sec)

mysql> insert into employees values(101, 'Amit Sharma', 'IT', 'Indore', 75000, '2023-05-10', 5, 30, 'MALE', 'FULL_TIME', 'JAVA,SQL,SPRING', 'amit@company.com', 501);
Query OK, 1 row affected (0.03 sec)

mysql> insert into employees values(102, 'Sneha Patel', 'Finance', 'Pune', 65000, '2024-02-15', 4, 28, 'FEMALE', 'FULL_TIME', 'SQL,PYTHON', 'sneha@company.com', 502), (103, 'Rahul Verma', 'Development', 'Delhi', 85000, '2022-08-20', 7, 32, 'MALE', 'FULL_TIME', 'JAVA,SQL,REACT', 'rahul@company.com', 501), (103, 'Rahul Verma', 'Development', 'Delhi', 85000, '2022-08-20', 7, 32, 'MALE', 'FULL_TIME', 'JAVA,SQL,REACT', 'rahul@company.com', 501), (104, 'Anjali Gupta', 'HR', 'Mumbai', 35000, '2023-11-01', 3, 27, 'FEMALE', 'CONTRACT', 'SQL', NULL, 503), (105, 'Suresh Kumar', 'IT', 'Bhopal', 28000, '2021-06-12', 6, 35, 'MALE', 'FULL_TIME', 'JAVA,SPRING', NULL, NULL), (106, 'Priya Singh', 'Development', 'Indore', 95000, '2025-01-10', 4, 29, 'FEMALE', 'FULL_TIME', 'PYTHON,REACT,SQL', 'priya@company.com', 501), (107, 'Arjun Mehta', 'Finance', 'Delhi', 45000, '2022-03-25', 3, 26, 'MALE', 'PART_TIME', 'SQL,PYTHON', 'arjun@company.com', NULL), (108, 'Simran Kaur', 'IT', 'Pune', 55000, '2024-07-18', 5, 31, 'FEMALE', 'FULL_TIME', 'JAVA,SQL,REACT', 'simran@company.com', 504);
ERROR 1062 (23000): Duplicate entry '103' for key 'employees.PRIMARY'
mysql> insert into employees values(102, 'Sneha Patel', 'Finance', 'Pune', 65000, '2024-02-15', 4, 28, 'FEMALE', 'FULL_TIME', 'SQL,PYTHON', 'sneha@company.com', 502), (103, 'Rahul Verma', 'Development', 'Delhi', 85000, '2022-08-20', 7, 32, 'MALE', 'FULL_TIME', 'JAVA,SQL,REACT', 'rahul@company.com', 501), (104, 'Anjali Gupta', 'HR', 'Mumbai', 35000, '2023-11-01', 3, 27, 'FEMALE', 'CONTRACT', 'SQL', NULL, 503), (105, 'Suresh Kumar', 'IT', 'Bhopal', 28000, '2021-06-12', 6, 35, 'MALE', 'FULL_TIME', 'JAVA,SPRING', NULL, NULL), (106, 'Priya Singh', 'Development', 'Indore', 95000, '2025-01-10', 4, 29, 'FEMALE', 'FULL_TIME', 'PYTHON,REACT,SQL', 'priya@company.com', 501), (107, 'Arjun Mehta', 'Finance', 'Delhi', 45000, '2022-03-25', 3, 26, 'MALE', 'PART_TIME', 'SQL,PYTHON', 'arjun@company.com', NULL), (108, 'Simran Kaur', 'IT', 'Pune', 55000, '2024-07-18', 5, 31, 'FEMALE', 'FULL_TIME', 'JAVA,SQL,REACT', 'simran@company.com', 504);
Query OK, 7 rows affected (0.01 sec)
Records: 7  Duplicates: 0  Warnings: 0


 select * from employees;
+-------------+---------------+-------------+--------+--------+--------------+------------+------+--------+-----------------+------------------+--------------------+-----------+
| employee_id | employee_name | department  | city   | salary | joining_date | experience | age  | gender | employment_type | skills           | email              | manage_id |
+-------------+---------------+-------------+--------+--------+--------------+------------+------+--------+-----------------+------------------+--------------------+-----------+
|         101 | Amit Sharma   | IT          | Indore |  75000 | 2023-05-10   |          5 |   30 | male   | FULL_TIME       | java,sql,spring  | amit@company.com   |       501 |
|         102 | Sneha Patel   | Finance     | Pune   |  65000 | 2024-02-15   |          4 |   28 | female | FULL_TIME       | sql,python       | sneha@company.com  |       502 |
|         103 | Rahul Verma   | Development | Delhi  |  85000 | 2022-08-20   |          7 |   32 | male   | FULL_TIME       | java,sql,react   | rahul@company.com  |       501 |
|         104 | Anjali Gupta  | HR          | Mumbai |  35000 | 2023-11-01   |          3 |   27 | female | CONTRACT        | sql              | NULL               |       503 |
|         105 | Suresh Kumar  | IT          | Bhopal |  28000 | 2021-06-12   |          6 |   35 | male   | FULL_TIME       | java,spring      | NULL               |      NULL |
|         106 | Priya Singh   | Development | Indore |  95000 | 2025-01-10   |          4 |   29 | female | FULL_TIME       | sql,python,react | priya@company.com  |       501 |
|         107 | Arjun Mehta   | Finance     | Delhi  |  45000 | 2022-03-25   |          3 |   26 | male   | PART_TIME       | sql,python       | arjun@company.com  |      NULL |
|         108 | Simran Kaur   | IT          | Pune   |  55000 | 2024-07-18   |          5 |   31 | female | FULL_TIME       | java,sql,react   | simran@company.com |       504 |
+-------------+---------------+-------------+--------+--------+--------------+------------+------+--------+-----------------+------------------+--------------------+-----------+
8 rows in set (0.00 sec)



