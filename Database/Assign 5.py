QNO  7: Create and Insert into products Table
Columns:

product_id INT

product_name VARCHAR(100)

category VARCHAR(50)

price DECIMAL(7,2)

stock_quantity INT

supplier_name VARCHAR(100)

manufacture_date DATE

expiry_date DATE

Task:

Insert 6 products (some with expiry dates, some without)
--------------------------------------------------------------------------

mysql> create database Tables_in_Product;
Query OK, 1 row affected (0.00 sec)

mysql> use Tables_in_Product;
Database changed

mysql> create table products (product_id INT auto_increment primary key,product_name VARCHAR(100),category VARCHAR(50),price DECIMAL(7,2),stock_quantity INT,supplier_name VARCHAR(100),manufacture_date DATE,expiry_date DATE);
Query OK, 0 rows affected (0.01 sec)

mysql> desc products;
+------------------+--------------+------+-----+---------+----------------+
| Field            | Type         | Null | Key | Default | Extra          |
+------------------+--------------+------+-----+---------+----------------+
| product_id       | int          | NO   | PRI | NULL    | auto_increment |
| product_name     | varchar(100) | YES  |     | NULL    |                |
| category         | varchar(50)  | YES  |     | NULL    |                |
| price            | decimal(7,2) | YES  |     | NULL    |                |
| stock_quantity   | int          | YES  |     | NULL    |                |
| supplier_name    | varchar(100) | YES  |     | NULL    |                |
| manufacture_date | date         | YES  |     | NULL    |                |
| expiry_date      | date         | YES  |     | NULL    |                |
+------------------+--------------+------+-----+---------+----------------+


mysql> insert into products
    -> (product_name, category, price, stock_quantity, supplier_name,
    ->  manufacture_date, expiry_date)
    -> VALUES
    -> ('Milk', 'Dairy', 60.00, 50, 'Amul',
    ->  '2026-10-01', '2026-10-15'),
    ->
    -> ('Rice', 'Grocery', 120.00, 100, 'India Gate',
    ->  '2026-08-10', NULL),
    ->
    -> ('Shampoo', 'Personal Care', 180.50, 30, 'Dove',
    ->  '2026-09-15', NULL),
    ->
    -> ('Biscuits', 'Snacks', 40.00, 80, 'Britannia',
    ->  '2026-10-05', '2027-04-05'),
    ->
    -> ('Cooking Oil', 'Grocery', 150.75, 45, 'Fortune',
    ->  '2026-09-20', NULL),
    ->
    -> ('Yogurt', 'Dairy', 35.00, 25, 'Mother Dairy',
    -> '2026-10-10', '2026-10-20');
Query OK, 6 rows affected (0.01 sec)
Records: 6  Duplicates: 0  Warnings: 0

mysql> select * from products;
+------------+--------------+---------------+--------+----------------+---------------+------------------+-------------+
| product_id | product_name | category      | price  | stock_quantity | supplier_name | manufacture_date | expiry_date |
+------------+--------------+---------------+--------+----------------+---------------+------------------+-------------+
|          1 | Milk         | Dairy         |  60.00 |             50 | Amul          | 2026-10-01       | 2026-10-15  |
|          2 | Rice         | Grocery       | 120.00 |            100 | India Gate    | 2026-08-10       | NULL        |
|          3 | Shampoo      | Personal Care | 180.50 |             30 | Dove          | 2026-09-15       | NULL        |
|          4 | Biscuits     | Snacks        |  40.00 |             80 | Britannia     | 2026-10-05       | 2027-04-05  |
|          5 | Cooking Oil  | Grocery       | 150.75 |             45 | Fortune       | 2026-09-20       | NULL        |
|          6 | Yogurt       | Dairy         |  35.00 |             25 | Mother Dairy  | 2026-10-10       | 2026-10-20  |
+------------+--------------+---------------+--------+----------------+---------------+------------------+-------------+