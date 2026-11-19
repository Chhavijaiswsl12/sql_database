QNO 1:
table salses
=========================================================
| Column         | Data Type                               |
| -------------- | --------------------------------------- |
| sale_id        | INT                                     |
| customer_name  | VARCHAR(50)                             |
| city           | VARCHAR(30)                             |
| category       | VARCHAR(30)                             |
| product        | VARCHAR(50)                             |
| quantity       | INT                                     |
| price          | DECIMAL(10,2)                           |
| discount       | DECIMAL(10,2)                           |
| sale_date      | DATE                                    |
| payment_method | ENUM('UPI','Card','Cash','Net Banking') |
| status         | ENUM('Completed','Pending','Cancelled') |
| customer_type  | ENUM('New','Regular','Premium')         |
=========================================================


INSERT INTO sales
(customer_name, city, category, product, quantity, price, discount, sale_date, payment_method, status, customer_type)
VALUES
('Rahul','Indore','Electronics','Laptop',2,60000,5000,'2026-01-05','Card','Completed','Premium'),
('Priya','Bhopal','Electronics','Mobile',3,25000,3000,'2026-01-07','UPI','Completed','Regular'),
('Amit','Indore','Clothing','Jeans',5,2000,500,'2026-01-10','Cash','Completed','New'),
('Sneha','Mumbai','Beauty','Cream',8,800,400,'2026-01-12','UPI','Completed','Premium'),
('Rohit','Pune','Electronics','Laptop',1,55000,4000,'2026-01-15','Card','Completed','Regular'),
('Neha','Delhi','Clothing','Kurti',6,1800,600,'2026-01-17','UPI','Completed','Premium'),
('Karan','Indore','Sports','Bat',4,3500,700,'2026-01-20','Cash','Completed','Regular'),
('Pooja','Bhopal','Beauty','Lipstick',10,600,300,'2026-01-22','UPI','Completed','New'),
('Vikas','Delhi','Books','SQL Book',7,900,200,'2026-01-25','Net Banking','Completed','Regular'),
('Anjali','Mumbai','Electronics','Watch',3,7000,800,'2026-01-27','Card','Completed','Premium'),
('Saurabh','Pune','Grocery','Rice',12,900,500,'2026-02-01','UPI','Completed','Regular'),
('Riya','Delhi','Electronics','AC',2,45000,5000,'2026-02-03','Card','Completed','Premium'),
('Manish','Indore','Clothing','Shirt',6,1500,300,'2026-02-05','UPI','Completed','New'),
('Komal','Bhopal','Furniture','Chair',3,8000,1000,'2026-02-07','Cash','Completed','Premium'),
('Deepak','Mumbai','Electronics','Speaker',5,3000,500,'2026-02-12','Card','Cancelled','Regular');




Questions===>
Find the total number of completed sales for each city where quantity is greater than 2. Display cities in descending order of sales count.
Find the total quantity sold for each category where discount is greater than 300. Display highest quantity first.
Find the total sales amount for each city for completed sales only. Display highest-selling city first.
Find the average product price for each category where quantity is at least 3. Display categories by average price descending.
Find the number of sales for each customer type where the order amount (quantity * price) is greater than 5000. Sort by number of sales descending.
Find the total discount given for each city for UPI transactions. Display highest discount first.
Find the total quantity sold through each payment method for completed transactions. Sort by total quantity descending.
Find the average discount for each category where quantity is greater than 4. Display highest average discount first.
Find the maximum product price for each city where the status is Completed. Sort by maximum price descending.
Find the minimum product price for each category where discount is greater than 300. Sort by minimum price ascending.
Find cities having more than 2 completed sales. Sort cities by completed sales count descending.
Find categories having total quantity greater than 10. Sort by total quantity descending.
Find cities having total sales greater than 50,000. Sort by total sales descending.
Find customer types having average product price greater than 10,000. Sort by average price descending.
Find categories having average discount greater than 400. Sort by average discount descending.
Find payment methods having more than 2 completed transactions. Sort by transaction count descending.
Find cities where the maximum product price is greater than 20,000. Sort by maximum price descending.
Find categories where the minimum product price is less than 2,000. Sort by minimum price ascending.
Find customer types where total discount is greater than 2,000. Sort by total discount descending.
Find cities where average quantity per transaction is greater than 4. Sort by average quantity descending.
Find each city’s total sales for completed UPI transactions where quantity is greater than 2. Display only cities having total sales greater than 10,000.
Find each category’s total quantity for completed transactions where discount is greater than 300. Display only categories having total quantity greater than 5.
Find each customer type’s average price for completed transactions where quantity >= 2. Display only customer types whose average price exceeds 10,000.
Find each city’s total discount for UPI transactions where quantity > 3. Display cities having total discount greater than 500.
Find each category’s total sales where payment method is UPI or Card and status is Completed. Display categories having total sales greater than 10,000.
Find each city’s transaction count for January 2026 completed transactions. Display cities having at least 2 transactions.
Find each category’s average sales amount where quantity >= 3 and status = Completed. Display categories whose average sales amount is greater than 5,000.
Find each customer type’s maximum price where payment method is Card and status is Completed. Display only customer types whose maximum price exceeds 20,000.
Find each city’s total quantity for Electronics and Clothing products where status is Completed. Display cities having total quantity greater than 5.
Find each payment method’s total sales where status is Completed and discount is greater than 400. Display payment methods having total sales greater than 20,000.
Find cities having more than 2 completed transactions and total sales greater than 50,000. Sort by total sales descending.
Find categories having total quantity greater than 8 and average price greater than 2,000. Sort by total quantity descending.
Find customer types having more than 2 transactions and total discount greater than 2,000. Sort by total discount descending.
Find cities having average quantity greater than 3 and maximum product price greater than 20,000. Sort by average quantity descending.
Find categories having more than 2 completed transactions and total sales greater than 20,000. Sort by total sales descending.
Find payment methods having more than 2 completed transactions and average price greater than 10,000. Sort by average price descending.
Find cities having total quantity greater than 8 and average discount greater than 300. Sort by total quantity descending.
Find customer types having average price greater than 5,000 and total quantity greater than 8. Sort by total quantity descending.
Find categories having minimum price below 2,000 and maximum price above 20,000. Sort by maximum price descending.
Find cities having total discount greater than 1,000 and total sales greater than 30,000. Sort by total sales descending.
Find the top 3 cities based on total sales, considering only completed transactions with quantity greater than 1 and displaying only cities having more than 1 transaction.
Find the top 3 categories based on total quantity where discount is greater than 300 and total quantity is greater than 5.
Find the top 3 customer types based on average sales amount where status is Completed and transaction count is greater than 1.
Find the top 3 cities based on total discount for UPI transactions where status is Completed and total discount is greater than 500.
Find the top 3 categories based on total sales where quantity is greater than 2, average price is greater than 1,000, and total sales exceeds 10,000.
Find the top 3 cities based on average order value where status is Completed, total quantity is greater than 5, and transaction count is greater than 1.
Find the second-highest city based on total sales after considering only completed transactions and cities having at least 2 transactions.
Find the third-highest category based on total quantity where quantity is greater than 2 and total discount exceeds 500.
Find the 2nd and 3rd highest customer types based on total sales where status is Completed and average price is greater than 5,000.
Find the top 3 cities where:
status is Completed
payment method is UPI or Card
quantity is greater than 1
number of transactions is greater than 1
total quantity is greater than 5
total sales is greater than 20,000

use assignment 8;
ERROR 1049 (42000): Unknown database 'assignment'
mysql> use assignment8;
Database changed
mysql> create table sales_management_system(sale_id int primary key auto_increment,customer_name  VARCHAR(50), city  VARCHAR(30), category  VARCHAR(30), product VARCHAR(50), quantity int, price DECIMAL(10,2), discount DECIMAL(10,2), sale_date DATE, payment_method  ENUM('UPI','Card','Cash','Net Banking'), status ENUM('Completed','Pending','Cancelled'), customer_type ENUM('New','Regular','Premium'));
Query OK, 0 rows affected (0.21 sec)

mysql> INSERT INTO sales_management_system
    -> (customer_name, city, category, product, quantity, price, discount, sale_date, payment_method, status, customer_type)
    -> VALUES
    -> ('Rahul','Indore','Electronics','Laptop',2,60000,5000,'2026-01-05','Card','Completed','Premium'),
    -> ('Priya','Bhopal','Electronics','Mobile',3,25000,3000,'2026-01-07','UPI','Completed','Regular'),
    -> ('Amit','Indore','Clothing','Jeans',5,2000,500,'2026-01-10','Cash','Completed','New'),
    -> ('Sneha','Mumbai','Beauty','Cream',8,800,400,'2026-01-12','UPI','Completed','Premium'),
    -> ('Rohit','Pune','Electronics','Laptop',1,55000,4000,'2026-01-15','Card','Completed','Regular'),
    -> ('Neha','Delhi','Clothing','Kurti',6,1800,600,'2026-01-17','UPI','Completed','Premium'),
    -> ('Karan','Indore','Sports','Bat',4,3500,700,'2026-01-20','Cash','Completed','Regular'),
    -> ('Pooja','Bhopal','Beauty','Lipstick',10,600,300,'2026-01-22','UPI','Completed','New'),
    -> ('Vikas','Delhi','Books','SQL Book',7,900,200,'2026-01-25','Net Banking','Completed','Regular'),
    -> ('Anjali','Mumbai','Electronics','Watch',3,7000,800,'2026-01-27','Card','Completed','Premium'),
    -> ('Saurabh','Pune','Grocery','Rice',12,900,500,'2026-02-01','UPI','Completed','Regular'),
    -> ('Riya','Delhi','Electronics','AC',2,45000,5000,'2026-02-03','Card','Completed','Premium'),
    -> ('Manish','Indore','Clothing','Shirt',6,1500,300,'2026-02-05','UPI','Completed','New'),
    -> ('Komal','Bhopal','Furniture','Chair',3,8000,1000,'2026-02-07','Cash','Completed','Premium'),
    -> ('Deepak','Mumbai','Electronics','Speaker',5,3000,500,'2026-02-12','Card','Cancelled','Regular');
Query OK, 15 rows affected (0.05 sec)
Records: 15  Duplicates: 0  Warnings: 0

mysql> select * from  sales_management_system;
+---------+---------------+--------+-------------+----------+----------+----------+----------+------------+----------------+-----------+---------------+
| sale_id | customer_name | city   | category    | product  | quantity | price    | discount | sale_date  | payment_method | status    | customer_type |
+---------+---------------+--------+-------------+----------+----------+----------+----------+------------+----------------+-----------+---------------+
|       1 | Rahul         | Indore | Electronics | Laptop   |        2 | 60000.00 |  5000.00 | 2026-01-05 | Card           | Completed | Premium       |
|       2 | Priya         | Bhopal | Electronics | Mobile   |        3 | 25000.00 |  3000.00 | 2026-01-07 | UPI            | Completed | Regular       |
|       3 | Amit          | Indore | Clothing    | Jeans    |        5 |  2000.00 |   500.00 | 2026-01-10 | Cash           | Completed | New           |
|       4 | Sneha         | Mumbai | Beauty      | Cream    |        8 |   800.00 |   400.00 | 2026-01-12 | UPI            | Completed | Premium       |
|       5 | Rohit         | Pune   | Electronics | Laptop   |        1 | 55000.00 |  4000.00 | 2026-01-15 | Card           | Completed | Regular       |
|       6 | Neha          | Delhi  | Clothing    | Kurti    |        6 |  1800.00 |   600.00 | 2026-01-17 | UPI            | Completed | Premium       |
|       7 | Karan         | Indore | Sports      | Bat      |        4 |  3500.00 |   700.00 | 2026-01-20 | Cash           | Completed | Regular       |
|       8 | Pooja         | Bhopal | Beauty      | Lipstick |       10 |   600.00 |   300.00 | 2026-01-22 | UPI            | Completed | New           |
|       9 | Vikas         | Delhi  | Books       | SQL Book |        7 |   900.00 |   200.00 | 2026-01-25 | Net Banking    | Completed | Regular       |
|      10 | Anjali        | Mumbai | Electronics | Watch    |        3 |  7000.00 |   800.00 | 2026-01-27 | Card           | Completed | Premium       |
|      11 | Saurabh       | Pune   | Grocery     | Rice     |       12 |   900.00 |   500.00 | 2026-02-01 | UPI            | Completed | Regular       |
|      12 | Riya          | Delhi  | Electronics | AC       |        2 | 45000.00 |  5000.00 | 2026-02-03 | Card           | Completed | Premium       |
|      13 | Manish        | Indore | Clothing    | Shirt    |        6 |  1500.00 |   300.00 | 2026-02-05 | UPI            | Completed | New           |
|      14 | Komal         | Bhopal | Furniture   | Chair    |        3 |  8000.00 |  1000.00 | 2026-02-07 | Cash           | Completed | Premium       |
|      15 | Deepak        | Mumbai | Electronics | Speaker  |        5 |  3000.00 |   500.00 | 2026-02-12 | Card           | Cancelled | Regular       |
+---------+---------------+--------+-------------+----------+----------+----------+----------+------------+----------------+-----------+---------------+
15 rows in set (0.07 sec)

mysql>  select * from  sales_management_system where quantity >2 order by cities desc;
ERROR 1054 (42S22): Unknown column 'cities' in 'order clause'
mysql>  select * from  sales_management_system where quantity >2 order by city desc;
+---------+---------------+--------+-------------+----------+----------+----------+----------+------------+----------------+-----------+---------------+
| sale_id | customer_name | city   | category    | product  | quantity | price    | discount | sale_date  | payment_method | status    | customer_type |
+---------+---------------+--------+-------------+----------+----------+----------+----------+------------+----------------+-----------+---------------+
|      11 | Saurabh       | Pune   | Grocery     | Rice     |       12 |   900.00 |   500.00 | 2026-02-01 | UPI            | Completed | Regular       |
|       4 | Sneha         | Mumbai | Beauty      | Cream    |        8 |   800.00 |   400.00 | 2026-01-12 | UPI            | Completed | Premium       |
|      10 | Anjali        | Mumbai | Electronics | Watch    |        3 |  7000.00 |   800.00 | 2026-01-27 | Card           | Completed | Premium       |
|      15 | Deepak        | Mumbai | Electronics | Speaker  |        5 |  3000.00 |   500.00 | 2026-02-12 | Card           | Cancelled | Regular       |
|       3 | Amit          | Indore | Clothing    | Jeans    |        5 |  2000.00 |   500.00 | 2026-01-10 | Cash           | Completed | New           |
|       7 | Karan         | Indore | Sports      | Bat      |        4 |  3500.00 |   700.00 | 2026-01-20 | Cash           | Completed | Regular       |
|      13 | Manish        | Indore | Clothing    | Shirt    |        6 |  1500.00 |   300.00 | 2026-02-05 | UPI            | Completed | New           |
|       6 | Neha          | Delhi  | Clothing    | Kurti    |        6 |  1800.00 |   600.00 | 2026-01-17 | UPI            | Completed | Premium       |
|       9 | Vikas         | Delhi  | Books       | SQL Book |        7 |   900.00 |   200.00 | 2026-01-25 | Net Banking    | Completed | Regular       |
|       2 | Priya         | Bhopal | Electronics | Mobile   |        3 | 25000.00 |  3000.00 | 2026-01-07 | UPI            | Completed | Regular       |
|       8 | Pooja         | Bhopal | Beauty      | Lipstick |       10 |   600.00 |   300.00 | 2026-01-22 | UPI            | Completed | New           |
|      14 | Komal         | Bhopal | Furniture   | Chair    |        3 |  8000.00 |  1000.00 | 2026-02-07 | Cash           | Completed | Premium       |
+---------+---------------+--------+-------------+----------+----------+----------+----------+------------+----------------+-----------+---------------+
12 rows in set (0.01 sec)

mysql>  select city,count(*) from  sales_management_system where quantity >2 group by city order by count(*) desc ;
+--------+----------+
| city   | count(*) |
+--------+----------+
| Bhopal |        3 |
| Indore |        3 |
| Mumbai |        3 |
| Delhi  |        2 |
| Pune   |        1 |
+--------+----------+
5 rows in set (0.01 sec)

mysql> select category,sum(quantity) from  sales_management_system where discount>300 group by category order by sum(quantity) desc;
+-------------+---------------+
| category    | sum(quantity) |
+-------------+---------------+
| Electronics |            16 |
| Grocery     |            12 |
| Clothing    |            11 |
| Beauty      |             8 |
| Sports      |             4 |
| Furniture   |             3 |
+-------------+---------------+
6 rows
mysql> create database assignment9;
Query OK, 1 row affected (0.09 sec)

mysql> use assignment9;
Database changed
mysql> create table doctors(docterid int primary key auto_increment,
    -> name varchar(50) not null,
    -> specialization varchar(30) unique not null) auto_increment=101;
Query OK, 0 rows affected (0.10 sec)

mysql> create table patients(pa_id int primary key auto_increment, name varchar(50) not null, patientid int,r
    -> 777yuj]==============================
    -> ^C
mysql>
mysql> create table patients(pa_id int primary key auto_increment, name varchar(50) not null, patientid int, foreign key (patientid)) references doctors(docterid);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ') references doctors(docterid)' at line 1
mysql> create table patients(pa_id int primary key auto_increment, name varchar(50) not null, patientid int, foreign key (patientid)) references doctors(docterid);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ') references doctors(docterid)' at line 1
mysql> CREATE TABLE patients (
    ->     pa_id INT PRIMARY KEY AUTO_INCREMENT,
    ->     name VARCHAR(50) NOT NULL,
    ->     patientid INT,
    ->     FOREIGN KEY (patientid) REFERENCES doctors(docterid)
    -> );
Query OK, 0 rows affected (0.27 sec)

mysql> insert into doctors(docterid,name,specialization) values
    -> ^C
mysql>
mysql> use assignment8;
Database changed
mysql> select city, sum(price) from  sales_management_system where status='completed' group by city order by sum(price) desc;
+--------+------------+
| city   | sum(price) |
+--------+------------+
| Indore |   67000.00 |
| Pune   |   55900.00 |
| Delhi  |   47700.00 |
| Bhopal |   33600.00 |
| Mumbai |    7800.00 |
+--------+------------+
5 rows in set (0.11 sec)

mysql> select * from  sales_management_system ;
+---------+---------------+--------+-------------+----------+----------+----------+----------+------------+----------------+-----------+---------------+
| sale_id | customer_name | city   | category    | product  | quantity | price    | discount | sale_date  | payment_method | status    | customer_type |
+---------+---------------+--------+-------------+----------+----------+----------+----------+------------+----------------+-----------+---------------+
|       1 | Rahul         | Indore | Electronics | Laptop   |        2 | 60000.00 |  5000.00 | 2026-01-05 | Card           | Completed | Premium       |
|       2 | Priya         | Bhopal | Electronics | Mobile   |        3 | 25000.00 |  3000.00 | 2026-01-07 | UPI            | Completed | Regular       |
|       3 | Amit          | Indore | Clothing    | Jeans    |        5 |  2000.00 |   500.00 | 2026-01-10 | Cash           | Completed | New           |
|       4 | Sneha         | Mumbai | Beauty      | Cream    |        8 |   800.00 |   400.00 | 2026-01-12 | UPI            | Completed | Premium       |
|       5 | Rohit         | Pune   | Electronics | Laptop   |        1 | 55000.00 |  4000.00 | 2026-01-15 | Card           | Completed | Regular       |
|       6 | Neha          | Delhi  | Clothing    | Kurti    |        6 |  1800.00 |   600.00 | 2026-01-17 | UPI            | Completed | Premium       |
|       7 | Karan         | Indore | Sports      | Bat      |        4 |  3500.00 |   700.00 | 2026-01-20 | Cash           | Completed | Regular       |
|       8 | Pooja         | Bhopal | Beauty      | Lipstick |       10 |   600.00 |   300.00 | 2026-01-22 | UPI            | Completed | New           |
|       9 | Vikas         | Delhi  | Books       | SQL Book |        7 |   900.00 |   200.00 | 2026-01-25 | Net Banking    | Completed | Regular       |
|      10 | Anjali        | Mumbai | Electronics | Watch    |        3 |  7000.00 |   800.00 | 2026-01-27 | Card           | Completed | Premium       |
|      11 | Saurabh       | Pune   | Grocery     | Rice     |       12 |   900.00 |   500.00 | 2026-02-01 | UPI            | Completed | Regular       |
|      12 | Riya          | Delhi  | Electronics | AC       |        2 | 45000.00 |  5000.00 | 2026-02-03 | Card           | Completed | Premium       |
|      13 | Manish        | Indore | Clothing    | Shirt    |        6 |  1500.00 |   300.00 | 2026-02-05 | UPI            | Completed | New           |
|      14 | Komal         | Bhopal | Furniture   | Chair    |        3 |  8000.00 |  1000.00 | 2026-02-07 | Cash           | Completed | Premium       |
|      15 | Deepak        | Mumbai | Electronics | Speaker  |        5 |  3000.00 |   500.00 | 2026-02-12 | Card           | Cancelled | Regular       |
+---------+---------------+--------+-------------+----------+----------+----------+----------+------------+----------------+-----------+---------------+
15 rows in set (0.03 sec)

mysql> select category,avg(price) as total from  sales_management_system where quantity>=3 group by category order by total desc;
+-------------+--------------+
| category    | total        |
+-------------+--------------+
| Electronics | 11666.666667 |
| Furniture   |  8000.000000 |
| Sports      |  3500.000000 |
| Clothing    |  1766.666667 |
| Books       |   900.000000 |
| Grocery     |   900.000000 |
| Beauty      |   700.000000 |
+-------------+--------------+
7 rows in set (0.03 sec)

mysql> select customer_type, count(*) from  sales_management_system where (quantity*price)>5000 group by customer_type order by count(*) desc;
+---------------+----------+
| customer_type | count(*) |
+---------------+----------+
| Premium       |        6 |
| Regular       |        6 |
| New           |        3 |
+---------------+----------+
3 rows in set (0.01 sec)

mysql> select city,sum(discount) from  sales_management_system group by city order by sum(discount) desc;
+--------+---------------+
| city   | sum(discount) |
+--------+---------------+
| Indore |       6500.00 |
| Delhi  |       5800.00 |
| Pune   |       4500.00 |
| Bhopal |       4300.00 |
| Mumbai |       1700.00 |
+--------+---------------+
5 rows in set (0.00 sec)

mysql> select payment_method, sum(quantity) from  sales_management_system where status='completed' group by payment_method order by sum(quantity) desc;
+----------------+---------------+
| payment_method | sum(quantity) |
+----------------+---------------+
| UPI            |            45 |
| Cash           |            12 |
| Card           |             8 |
| Net Banking    |             7 |
+----------------+---------------+
4 rows in set (0.00 sec)

mysql> select category,avg(discount) as total from  sales_management_system where quantity>4 group by category order by total desc;
+-------------+------------+
| category    | total      |
+-------------+------------+
| Grocery     | 500.000000 |
| Electronics | 500.000000 |
| Clothing    | 466.666667 |
| Beauty      | 350.000000 |
| Books       | 200.000000 |
+-------------+------------+
5 rows in set (0.00 sec)

mysql> select city,max(price) as total  from  sales_management_system where status='completed' group by city order by total desc;
+--------+----------+
| city   | total    |
+--------+----------+
| Indore | 60000.00 |
| Pune   | 55000.00 |
| Delhi  | 45000.00 |
| Bhopal | 25000.00 |
| Mumbai |  7000.00 |
+--------+----------+
5 rows in set (0.04 sec)

mysql> select category,min(price) as total from  sales_management_system where discount>300 group by category order by total;
+-------------+---------+
| category    | total   |
+-------------+---------+
| Beauty      |  800.00 |
| Grocery     |  900.00 |
| Clothing    | 1800.00 |
| Electronics | 3000.00 |
| Sports      | 3500.00 |
| Furniture   | 8000.00 |
+-------------+---------+
6 rows in set (0.04 sec)

mysql> select city,count(*) as total from  sales_management_system group by city having total>2 order by total desc;
+--------+-------+
| city   | total |
+--------+-------+
| Indore |     4 |
| Bhopal |     3 |
| Mumbai |     3 |
| Delhi  |     3 |
+--------+-------+
4 rows in set (0.05 sec)

mysql> select category,sum(quantity) as total from  sales_management_system group by category having total>10 order by total desc;
+-------------+-------+
| category    | total |
+-------------+-------+
| Beauty      |    18 |
| Clothing    |    17 |
| Electronics |    16 |
| Grocery     |    12 |
+-------------+-------+
4 rows in set (0.00 sec)

mysql> select city,total(price) as total from  sales_management_system group by city having total>50000 order by total desc;
ERROR 1305 (42000): FUNCTION assignment8.total does not exist
mysql> select city,sum(price) as total from  sales_management_system group by city having total>50000 order by total desc;
+--------+----------+
| city   | total    |
+--------+----------+
| Indore | 67000.00 |
| Pune   | 55900.00 |
+--------+----------+
2 rows in set (0.06 sec)

mysql> select customer_type, avg(price) as total from  sales_management_system group by customer_type having total>10000 order by total desc;
+---------------+--------------+
| customer_type | total        |
+---------------+--------------+
| Premium       | 20433.333333 |
| Regular       | 14716.666667 |
+---------------+--------------+
2 rows in set (0.03 sec)

mysql> select category, avg(discount) as total from  sales_management_systemgroup by category having total>400 order by total desc;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'by category having total>400 order by total desc' at line 1
mysql> select category, avg(discount) as total from  sales_management_systemgroup by category having total>400 order by total desc;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'by category having total>400 order by total desc' at line 1
mysql> select city,count(status) as total from  sales_management_system group by city having total>2 order by total desc;
+--------+-------+
| city   | total |
+--------+-------+
| Indore |     4 |
| Bhopal |     3 |
| Mumbai |     3 |
| Delhi  |     3 |
+--------+-------+
4 rows in set (0.03 sec)

mysql> select city,count(status) as total from  sales_management_system where status='completed' group by city having total>2 order by total desc;
+--------+-------+
| city   | total |
+--------+-------+
| Indore |     4 |
| Bhopal |     3 |
| Delhi  |     3 |
+--------+-------+
3 rows in set (0.03 sec)

mysql> select city, max(price) from sales_management_system group by city having max(price)>20000 order by max(price) desc;
+--------+------------+
| city   | max(price) |
+--------+------------+
| Indore |   60000.00 |
| Pune   |   55000.00 |
| Delhi  |   45000.00 |
| Bhopal |   25000.00 |
+--------+------------+
4 rows in set (0.06 sec)

mysql> select category, min(price) as total  from sales_management_system group by category having total<2000 order by total ;
+----------+---------+
| category | total   |
+----------+---------+
| Beauty   |  600.00 |
| Books    |  900.00 |
| Grocery  |  900.00 |
| Clothing | 1500.00 |
+----------+---------+
4 rows in set (0.01 sec)