QNO  3: ALTER students Table
Task:

Add a column dob DATE

Rename column phone to mobile_number

Modify column age to SMALLINT

Drop column email

mysql> use college_db;
mysql> create table student1(id int,name varchar(100),age int,gender varchar(10),address varchar(150),phone varchar(15),email varchar(100));

mysql> desc student1;
+---------+--------------+------+-----+---------+-------+
| Field   | Type         | Null | Key | Default | Extra |
+---------+--------------+------+-----+---------+-------+
| id      | int          | YES  |     | NULL    |       |
| name    | varchar(100) | YES  |     | NULL    |       |
| age     | int          | YES  |     | NULL    |       |
| gender  | varchar(10)  | YES  |     | NULL    |       |
| address | varchar(150) | YES  |     | NULL    |       |
| phone   | varchar(15)  | YES  |     | NULL    |       |
| email   | varchar(100) | YES  |     | NULL    |       |
+---------+--------------+------+-----+---------+-------+


mysql> insert into student1 select * from students;
Query OK, 5 rows affected (0.01 sec)

mysql> select * from student1;
+------+------------------+------+--------+------------+------------+-------------------+
| id   | name             | age  | gender | address    | phone      | email             |
+------+------------------+------+--------+------------+------------+-------------------+
|    1 | Kirti Asatkar    |   20 | Female | Indore, MP | 9876543210 | kirti@gmail.com   |
|    2 | Khushi sanwaliya |   19 | Female | Bhopal, MP | 9876543211 | Khushi@gmail.com  |
|    3 | Chhavi jaiswal   |   21 | Female | Dewas, MP  | 9876543212 | chhavi@gmail.com  |
|    4 | Saloni Parihar   |   20 | Female | Ujjain, MP | 9876543213 | saloni@gmail.com  |
|    5 | Kritika wagadre  |   22 | Female | Indore, MP | 9876543214 | Kritika@gmail.com |
+------+------------------+------+--------+------------+------------+-------------------+

mysql> alter table student1 add column dob date;
Query OK, 0 rows affected (0.03 sec)

mysql> alter table student1 change column phone mobile_number varchar(15);
Query OK, 0 rows affected (0.02 sec)

mysql> alter table student1 modify column age smallint;
Query OK, 5 rows affected (0.06 sec)

mysql> alter table student1 drop column email;
Query OK, 0 rows affected (0.02 sec)

mysql> alter table student1 drop column email;
Query OK, 0 rows affected (0.02 sec)

mysql> desc student1;
+---------------+--------------+------+-----+---------+-------+
| Field         | Type         | Null | Key | Default | Extra |
+---------------+--------------+------+-----+---------+-------+
| id            | int          | YES  |     | NULL    |       |
| name          | varchar(100) | YES  |     | NULL    |       |
| age           | smallint     | YES  |     | NULL    |       |
| gender        | varchar(10)  | YES  |     | NULL    |       |
| address       | varchar(150) | YES  |     | NULL    |       |
| mobile_number | varchar(15)  | YES  |     | NULL    |       |
| dob           | date         | YES  |     | NULL    |       |
+---------------+--------------+------+-----+---------+-------+
7 rows in set (0.01 sec)

mysql> select * from student1;
+------+------------------+------+--------+------------+---------------+------+
| id   | name             | age  | gender | address    | mobile_number | dob  |
+------+------------------+------+--------+------------+---------------+------+
|    1 | Kirti Asatkar    |   20 | Female | Indore, MP | 9876543210    | NULL |
|    2 | Khushi sanwaliya |   19 | Female | Bhopal, MP | 9876543211    | NULL |
|    3 | Chhavi jaiswal   |   21 | Female | Dewas, MP  | 9876543212    | NULL |
|    4 | Saloni Parihar   |   20 | Female | Ujjain, MP | 9876543213    | NULL |
|    5 | Kritika wagadre  |   22 | Female | Indore, MP | 9876543214    | NULL |
+------+------------------+------+--------+------------+---------------+------+
5 rows in set (0.00 sec)