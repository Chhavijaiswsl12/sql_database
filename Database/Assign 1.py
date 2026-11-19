mysql> create database college_db;

mysql> use college_db;

mysql> desc students;
+---------+--------------+------+-----+---------+-------+
| Field   | Type         | Null | Key | Default | Extra |
+---------+--------------+------+-----+---------+-------+
| id      | int          | YES  |     | NULL    |       |
| name    | varchar(100) | YES  |     | NULL    |       |
| age     | int          | YES  |     | NULL    |       |
| gender  | varchar(10)  | YES  |     | NULL    |       |
| address | varchar(150) | YES  |     | NULL    |       |
| email   | varchar(150) | YES  |     | NULL    |       |
+---------+--------------+------+-----+---------+-------+

mysql> insert into students values(1,"Khushi sanwaliya",20,"Female","Mandshore","Khushi12@gmail.com"),
    -> (2,"Kirti Asatkar",20,"Female","Indore","Kirtiaasatkar32@gmail.com");
    ->(3,"Chhavi Jaiswal",22,"Female","Dharampuri","Chhavi321@gmail.com"),
    ->(4,"Saloni Parihar",19,"Female","Indore","Saloni4556@gmail.com"),
    ->(5,"Kritika Wagadre",21,"Female","Ujjain","1234Kritika@gmail.com");

mysql> select * from students;
+------+------------------+------+--------+------------+------------+-------------------+
| id   | name             | age  | gender | address    | phone      | email             |
+------+------------------+------+--------+------------+------------+-------------------+
|    1 | Kirti Asatkar    |   20 | Female | Indore, MP | 9876543210 | kirti@gmail.com   |
|    2 | Khushi sanwaliya |   19 | Female | Bhopal, MP | 9876543211 | Khushi@gmail.com  |
|    3 | Chhavi jaiswal   |   21 | Female | Dewas, MP  | 9876543212 | chhavi@gmail.com  |
|    4 | Saloni Parihar   |   20 | Female | Ujjain, MP | 9876543213 | saloni@gmail.com  |
|    5 | Kritika wagadre  |   22 | Female | Indore, MP | 9876543214 | Kritika@gmail.com |
+------+------------------+------+--------+------------+------------+-------------------+
5 rows in set (0.01 sec)