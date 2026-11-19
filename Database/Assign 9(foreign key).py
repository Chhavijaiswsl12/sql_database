> create database assignment9;
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