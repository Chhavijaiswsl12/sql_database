
mysql> create database a10 case_study;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'case_study' at line 1
mysql> CREATE DATABASE `a-10 (case study)`;
Query OK, 1 row affected (0.12 sec)

mysql> use  `a-10 (case study)`;
Database changed
mysql> create table department(dep_id int primary key, dep_name varchar(50),floor_no int);
Query OK, 0 rows affected (0.17 sec)

mysql> create table patient(patient_id int primary key,patient_name varchar(30), gender enum('male','female'), city varchar(30));
Query OK, 0 rows affected (0.04 sec)

mysql> create table medicine(medi_id int primary key, medi_name varchar(30),manufacture varchar(50), price int);
Query OK, 0 rows affected (0.04 sec)

mysql> INSERT INTO department (dep_id, dep_name, floor_no)
    -> VALUES
    -> (101, 'Cardiology', 3),
    -> (102, 'Neurology', 4),
    -> (103, 'Orthopedics', 2),
    -> (104, 'Dermatology', 1);
Query OK, 4 rows affected (0.02 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> INSERT INTO patient (patient_id, patient_name, gender, city)
    -> VALUES
    -> (301, 'Rahul Verma', 'male', 'Indore'),
    -> (302, 'Sneha Sharma', 'female', 'Bhopal'),
    -> (303, 'Amit Patel', 'male', 'Indore'),
    -> (304, 'Pooja Gupta', 'female', 'Ujjain'),
    -> (305, 'Rohan Jain', 'male', 'Dewas'),
    -> (306, 'Neha Patel', 'female', 'Indore');
Query OK, 6 rows affected (0.03 sec)
Records: 6  Duplicates: 0  Warnings: 0

mysql> INSERT INTO medicine (medi_id, medi_name, manufacture, price)
    -> VALUES
    -> (401, 'Paracetamol', 'ABC Pharma', 30),
    -> (402, 'Azithromycin', 'XYZ Pharma', 120),
    -> (403, 'Pantoprazole', 'MedLife', 80),
    -> (404, 'Amoxicillin', 'HealthCare Pharma', 150),
    -> (405, 'Ibuprofen', 'ABC Pharma', 60),
    -> (406, 'Cetirizine', 'MedLife', 45);
Query OK, 6 rows affected (0.01 sec)
Records: 6  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM department;
+--------+-------------+----------+
| dep_id | dep_name    | floor_no |
+--------+-------------+----------+
|    101 | Cardiology  |        3 |
|    102 | Neurology   |        4 |
|    103 | Orthopedics |        2 |
|    104 | Dermatology |        1 |
+--------+-------------+----------+
4 rows in set (0.03 sec)

mysql>
mysql> SELECT * FROM doctor;
ERROR 1146 (42S02): Table 'a-10 (case study).doctor' doesn't exist
mysql>
mysql> SELECT * FROM patient;
+------------+--------------+--------+--------+
| patient_id | patient_name | gender | city   |
+------------+--------------+--------+--------+
|        301 | Rahul Verma  | male   | Indore |
|        302 | Sneha Sharma | female | Bhopal |
|        303 | Amit Patel   | male   | Indore |
|        304 | Pooja Gupta  | female | Ujjain |
|        305 | Rohan Jain   | male   | Dewas  |
|        306 | Neha Patel   | female | Indore |
+------------+--------------+--------+--------+
6 rows in set (0.00 sec)

mysql>
mysql> SELECT * FROM medicine;
+---------+--------------+-------------------+-------+
| medi_id | medi_name    | manufacture       | price |
+---------+--------------+-------------------+-------+
|     401 | Paracetamol  | ABC Pharma        |    30 |
|     402 | Azithromycin | XYZ Pharma        |   120 |
|     403 | Pantoprazole | MedLife           |    80 |
|     404 | Amoxicillin  | HealthCare Pharma |   150 |
|     405 | Ibuprofen    | ABC Pharma        |    60 |
|     406 | Cetirizine   | MedLife           |    45 |
+---------+--------------+-------------------+-------+
6 rows in set (0.00 sec)

mysql> create table docter(docter_id int primary key, docter_name varchar(50), specialization varchar(30), dep_id int, foreign key(dep_id) references department(dep_id)) on delete set null,on update cascade);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'on delete set null,on update cascade)' at line 1
mysql> create table docter(docter_id int primary key, docter_name varchar(50), specialization varchar(30), dep_id int, foreign key(dep_id) references department(dep_id)) on delete set null on update cascade);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'on delete set null on update cascade)' at line 1
mysql> create table docter(docter_id int primary key, docter_name varchar(50), specialization varchar(30), dep_id int, foreign key(dep_id) references department(dep_id) on delete set null on update cascade);
Query OK, 0 rows affected (0.09 sec)

mysql> INSERT INTO doctor (doctor_id, doctor_name, specialization, department_id)
    -> VALUES
    -> (201, 'Dr. Rajesh Sharma', 'Cardiologist', 101),
    -> (202, 'Dr. Neha Verma', 'Neurologist', 102),
    -> (203, 'Dr. Amit Jain', 'Orthopedic', 103),
    -> (204, 'Dr. Priya Singh', 'Dermatologist', 104),
    -> (205, 'Dr. Karan Mehta', 'Cardiologist', 101);
ERROR 1146 (42S02): Table 'a-10 (case study).doctor' doesn't exist
mysql> (205, 'Dr. Karan Mehta', 'Cardiologist', 101);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '205, 'Dr. Karan Mehta', 'Cardiologist', 101)' at line 1
mysql> INSERT INTO docter (doctor_id, doctor_name, specialization, department_id)
    -> (201, 'Dr. Rajesh Sharma', 'Cardiologist', 101),
    -> (202, 'Dr. Neha Verma', 'Neurologist', 102),
    -> (203, 'Dr. Amit Jain', 'Orthopedic', 103),
    -> (204, 'Dr. Priya Singh', 'Dermatologist', 104),
    ->  (205, 'Dr. Karan Mehta', 'Cardiologist', 101);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '201, 'Dr. Rajesh Sharma', 'Cardiologist', 101),
(202, 'Dr. Neha Verma', 'Neurolo' at line 2
mysql> INSERT INTO docter (docter_id, docter_name, specialization, dep_id)
    -> VALUES
    -> (201, 'Dr. Rajesh Sharma', 'Cardiologist', 101),
    -> (202, 'Dr. Neha Verma', 'Neurologist', 102),
    -> (203, 'Dr. Amit Jain', 'Orthopedic', 103),
    -> (204, 'Dr. Priya Singh', 'Dermatologist', 104),
    -> (205, 'Dr. Karan Mehta', 'Cardiologist', 101);
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select * from docter;
+-----------+-------------------+----------------+--------+
| docter_id | docter_name       | specialization | dep_id |
+-----------+-------------------+----------------+--------+
|       201 | Dr. Rajesh Sharma | Cardiologist   |    101 |
|       202 | Dr. Neha Verma    | Neurologist    |    102 |
|       203 | Dr. Amit Jain     | Orthopedic     |    103 |
|       204 | Dr. Priya Singh   | Dermatologist  |    104 |
|       205 | Dr. Karan Mehta   | Cardiologist   |    101 |
+-----------+-------------------+----------------+--------+
5 rows in set (0.00 sec)

mysql> create table appointment(appoint_id int primary key, appoint_date date,appoint_time time, patient_id int,foreign key(patient_id) references patient(patient_id), docter_id int, foreign key(docter_id) references docter(docter_id), dep_id int, foreign key(dep_id) references department(dep_id), status varchar(30));
Query OK, 0 rows affected (0.18 sec)

mysql> select * from appointment ;
Empty set (0.29 sec)

mysql> desc appointment;
+--------------+-------------+------+-----+---------+-------+
| Field        | Type        | Null | Key | Default | Extra |
+--------------+-------------+------+-----+---------+-------+
| appoint_id   | int         | NO   | PRI | NULL    |       |
| appoint_date | date        | YES  |     | NULL    |       |
| appoint_time | time        | YES  |     | NULL    |       |
| patient_id   | int         | YES  | MUL | NULL    |       |
| docter_id    | int         | YES  | MUL | NULL    |       |
| dep_id       | int         | YES  | MUL | NULL    |       |
| status       | varchar(30) | YES  |     | NULL    |       |
+--------------+-------------+------+-----+---------+-------+
7 rows in set (0.14 sec)

mysql> alter table appointment add constraint foreign key(patient_id) references patient(patient_id) ON DELETE CASCADE,  foreign key(docter_id) references docter(docter_id) ON DELETE SET NULL,  foreign key(dep_id) references department(dep_id), status varchar(30) ON UPDATE CASCADE;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'foreign key(docter_id) references docter(docter_id) ON DELETE SET NULL,  foreign' at line 1
mysql> alter table appointment add constraint foreign key(patient_id) references patient(patient_id) ON DELETE CASCADE, add constraint  foreign key(docter_id) references docter(docter_id) ON DELETE SET NULL, add constraint foreign key(dep_id) references department(dep_id) ON UPDATE CASCADE;
Query OK, 0 rows affected (0.36 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc appointment;
+--------------+-------------+------+-----+---------+-------+
| Field        | Type        | Null | Key | Default | Extra |
+--------------+-------------+------+-----+---------+-------+
| appoint_id   | int         | NO   | PRI | NULL    |       |
| appoint_date | date        | YES  |     | NULL    |       |
| appoint_time | time        | YES  |     | NULL    |       |
| patient_id   | int         | YES  | MUL | NULL    |       |
| docter_id    | int         | YES  | MUL | NULL    |       |
| dep_id       | int         | YES  | MUL | NULL    |       |
| status       | varchar(30) | YES  |     | NULL    |       |
+--------------+-------------+------+-----+---------+-------+
7 rows in set (0.09 sec)

mysql> create table prescription(prescription_id int primary key, prescription_date date, appointment_id int,foreign key(appointment_id) references appointment(appoint_id) on delete cascade, doctor_id int, foreign key(doctor_id) references docter(doctor_id) on update set null,  patient_id int, foreign key(patient_id) references patient(patient_id) on update set null, remarks varchar(30);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
mysql> create table prescription(prescription_id int primary key, prescription_date date, appointment_id int,foreign key(appointment_id) references appointment(appoint_id) on delete cascade, doctor_id int, foreign key(doctor_id) references docter(doctor_id) on update set null,  patient_id int, foreign key(patient_id) references patient(patient_id) on update set null, remarks varchar(30));
ERROR 3734 (HY000): Failed to add the foreign key constraint. Missing column 'doctor_id' for constraint 'prescription_ibfk_2' in the referenced table 'docter'
mysql> create table prescription(prescription_id int primary key, prescription_date date, appointment_id int,foreign key(appointment_id) references appointment(appoint_id) on delete cascade, docter_id int, foreign key(docter_id) references docter(docter_id) on update set null,  patient_id int, foreign key(patient_id) references patient(patient_id) on update set null, remarks varchar(30));
Query OK, 0 rows affected (0.15 sec)

mysql> select * medicine;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'medicine' at line 1
mysql> select * from medicine;
+---------+--------------+-------------------+-------+
| medi_id | medi_name    | manufacture       | price |
+---------+--------------+-------------------+-------+
|     401 | Paracetamol  | ABC Pharma        |    30 |
|     402 | Azithromycin | XYZ Pharma        |   120 |
|     403 | Pantoprazole | MedLife           |    80 |
|     404 | Amoxicillin  | HealthCare Pharma |   150 |
|     405 | Ibuprofen    | ABC Pharma        |    60 |
|     406 | Cetirizine   | MedLife           |    45 |
+---------+--------------+-------------------+-------+
6 rows in set (0.03 sec)

mysql> create table PRESCRIPTION_MEDICINE(prescription_id int,medi_id, primary key(prescription_id,medi_id) , foreign key(prescription_id) references prescription(prescription_id), foreign key(medi_id) references medicine(medi_id), dosage int, duration_days date, quantity int);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ', primary key(prescription_id,medi_id) , foreign key(prescription_id) references' at line 1
mysql> create table PRESCRIPTION_MEDICINE(prescription_id int,medi_id primary key(prescription_id,medi_id) , foreign key(prescription_id) references prescription(prescription_id), foreign key(medi_id) references medicine(medi_id), dosage int, duration_days date, quantity int);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'primary key(prescription_id,medi_id) , foreign key(prescription_id) references p' at line 1
mysql>
mysql> create table prescription(prescription_id int primary key, prescription_date date, appointment_id int,foreign key(appointment_id) references appointment(appoint_id) on delete cascade, doctor_id int, foreign key(doctor_id) references docter(doctor_id) on update set null,  patient_id int, foreign key(patient_id) references patient(patient_id) on update set null, remarks varchar(30);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
mysql> create table prescription(prescription_id int primary key, prescription_date date, appointment_id int,foreign key(appointment_id) references appointment(appoint_id) on delete cascade, doctor_id int, foreign key(doctor_id) references docter(doctor_id) on update set null,  patient_id int, foreign key(patient_id) references patient(patient_id) on update set null, remarks varchar(30));
ERROR 3734 (HY000): Failed to add the foreign key constraint. Missing column 'doctor_id' for constraint 'prescription_ibfk_2' in the referenced table 'docter'
mysql> create table prescription(prescription_id int primary key, prescription_date date, appointment_id int,foreign key(appointment_id) references appointment(appoint_id) on delete cascade, docter_id int, foreign key(docter_id) references docter(docter_id) on update set null,  patient_id int, foreign key(patient_id) references patient(patient_id) on update set null, remarks varchar(30));
Query OK, 0 rows affected (0.15 sec)

mysql> select * medicine;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'medicine' at line 1
mysql> select * from medicine;
+---------+--------------+-------------------+-------+
| medi_id | medi_name    | manufacture       | price |
+---------+--------------+-------------------+-------+
|     401 | Paracetamol  | ABC Pharma        |    30 |
|     402 | Azithromycin | XYZ Pharma        |   120 |
|     403 | Pantoprazole | MedLife           |    80 |
|     404 | Amoxicillin  | HealthCare Pharma |   150 |
|     405 | Ibuprofen    | ABC Pharma        |    60 |
|     406 | Cetirizine   | MedLife           |    45 |
+---------+--------------+-------------------+-------+
6 rows in set (0.03 sec)

mysql> create table PRESCRIPTION_MEDICINE(prescription_id int,medi_id, primary key(prescription_id,medi_id) , foreign key(prescription_id) references prescription(prescription_id), foreign key(medi_id) references medicine(medi_id), dosage int, duration_days date, quantity int);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ', primary key(prescription_id,medi_id) , foreign key(prescription_id) references' at line 1
mysql> create table PRESCRIPTION_MEDICINE(prescription_id int,medi_id primary key(prescription_id,medi_id) , foreign key(prescription_id) references prescription(prescription_id), foreign key(medi_id) references medicine(medi_id), dosage int, duration_days date, quantity int);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'primary key(prescription_id,medi_id) , foreign key(prescription_id) references p' at line 1
mysql> create table PRESCRIPTION_MEDICINE(prescription_id int,medi_id intprimary key(prescription_id,medi_id) , foreign key(prescription_id) references prescription(prescription_id), foreign key(medi_id) references medicine(medi_id), dosage int, duration_days , quantity int);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'intprimary key(prescription_id,medi_id) , foreign key(prescription_id) reference' at line 1
mysql> create table PRESCRIPTION_MEDICINE(prescription_id int,medi_id int primary key(prescription_id,medi_id) , foreign key(prescription_id) references prescription(prescription_id), foreign key(medi_id) references medicine(medi_id), dosage int, duration_days int, quantity int);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(prescription_id,medi_id) , foreign key(prescription_id) references prescription' at line 1
mysql> create table PRESCRIPTION_MEDICINE(prescription_id int,medi_id int, primary key(prescription_id,medi_id) , foreign key(prescription_id) references prescription(prescription_id), foreign key(medi_id) references medicine(medi_id), dosage int, duration_days int, quantity int);
Query OK, 0 rows affected (0.19 sec)

mysql> alter table PRESCRIPTION_MEDICINE add constraint  foreign key(medi_id) references medicine(medi_id) on delete restrict, add constraint  foreign key(prescription_id) references prescription(prescription_id) ON UPDATE SET NULL;
ERROR 1830 (HY000): Column 'prescription_id' cannot be NOT NULL: needed in a foreign key constraint 'prescription_medicine_ibfk_4' SET NULL
mysql> alter table PRESCRIPTION_MEDICINE add constraint  foreign key(medi_id) references medicine(medi_id) on delete restrict, add constraint  foreign key(prescription_id) references prescription(prescription_id) ON UPDATE SET NULL;
ERROR 1830 (HY000): Column 'prescription_id' cannot be NOT NULL: needed in a foreign key constraint 'prescription_medicine_ibfk_4' SET NULL
mysql> alter table PRESCRIPTION_MEDICINE add constraint  foreign key(medi_id) references medicine(medi_id) on delete restrict, add constraint  foreign key(prescription_id) references prescription(prescription_id) ON UPDATE cascade;
Query OK, 0 rows affected (0.16 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> SHOW CREATE TABLE PRESCRIPTION_MEDICINE;
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table                 | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PRESCRIPTION_MEDICINE | CREATE TABLE `prescription_medicine` (
  `prescription_id` int NOT NULL,
  `medi_id` int NOT NULL,
  `dosage` int DEFAULT NULL,
  `duration_days` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`prescription_id`,`medi_id`),
  KEY `medi_id` (`medi_id`),
  CONSTRAINT `prescription_medicine_ibfk_1` FOREIGN KEY (`prescription_id`) REFERENCES `prescription` (`prescription_id`),
  CONSTRAINT `prescription_medicine_ibfk_2` FOREIGN KEY (`medi_id`) REFERENCES `medicine` (`medi_id`),
  CONSTRAINT `prescription_medicine_ibfk_3` FOREIGN KEY (`medi_id`) REFERENCES `medicine` (`medi_id`) ON DELETE RESTRICT,
  CONSTRAINT `prescription_medicine_ibfk_4` FOREIGN KEY (`prescription_id`) REFERENCES `prescription` (`prescription_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.05 sec)

mysql> alter table PRESCRIPTION_MEDICINE drop  FOREIGN KEY prescription_medicine_ibfk_1;
Query OK, 0 rows affected (0.07 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> alter table  PRESCRIPTION_MEDICINE add constraint  foreign key(prescription_id) references prescription(prescription_id) on delete cascade;
Query OK, 0 rows affected (0.15 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> SHOW CREATE TABLE appointment;
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table       | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| appointment | CREATE TABLE `appointment` (
  `appoint_id` int NOT NULL,
  `appoint_date` date DEFAULT NULL,
  `appoint_time` time DEFAULT NULL,
  `patient_id` int DEFAULT NULL,
  `docter_id` int DEFAULT NULL,
  `dep_id` int DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`appoint_id`),
  KEY `patient_id` (`patient_id`),
  KEY `docter_id` (`docter_id`),
  KEY `dep_id` (`dep_id`),
  CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`patient_id`),
  CONSTRAINT `appointment_ibfk_2` FOREIGN KEY (`docter_id`) REFERENCES `docter` (`docter_id`),
  CONSTRAINT `appointment_ibfk_3` FOREIGN KEY (`dep_id`) REFERENCES `department` (`dep_id`),
  CONSTRAINT `appointment_ibfk_4` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`patient_id`) ON DELETE CASCADE,
  CONSTRAINT `appointment_ibfk_5` FOREIGN KEY (`docter_id`) REFERENCES `docter` (`docter_id`) ON DELETE SET NULL,
  CONSTRAINT `appointment_ibfk_6` FOREIGN KEY (`dep_id`) REFERENCES `department` (`dep_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.03 sec)

mysql> ALTER TABLE appointment
    -> DROP FOREIGN KEY appointment_ibfk_1,
    -> DROP FOREIGN KEY appointment_ibfk_2,
    -> DROP FOREIGN KEY appointment_ibfk_3;
Query OK, 0 rows affected (0.05 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> SHOW CREATE TABLE appointment;
+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table       | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| appointment | CREATE TABLE `appointment` (
  `appoint_id` int NOT NULL,
  `appoint_date` date DEFAULT NULL,
  `appoint_time` time DEFAULT NULL,
  `patient_id` int DEFAULT NULL,
  `docter_id` int DEFAULT NULL,
  `dep_id` int DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`appoint_id`),
  KEY `patient_id` (`patient_id`),
  KEY `docter_id` (`docter_id`),
  KEY `dep_id` (`dep_id`),
  CONSTRAINT `appointment_ibfk_4` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`patient_id`) ON DELETE CASCADE,
  CONSTRAINT `appointment_ibfk_5` FOREIGN KEY (`docter_id`) REFERENCES `docter` (`docter_id`) ON DELETE SET NULL,
  CONSTRAINT `appointment_ibfk_6` FOREIGN KEY (`dep_id`) REFERENCES `department` (`dep_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |
+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)

mysql> SHOW CREATE TABLE prescription;
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table        | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| prescription | CREATE TABLE `prescription` (
  `prescription_id` int NOT NULL,
  `prescription_date` date DEFAULT NULL,
  `appointment_id` int DEFAULT NULL,
  `docter_id` int DEFAULT NULL,
  `patient_id` int DEFAULT NULL,
  `remarks` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`prescription_id`),
  KEY `appointment_id` (`appointment_id`),
  KEY `docter_id` (`docter_id`),
  KEY `patient_id` (`patient_id`),
  CONSTRAINT `prescription_ibfk_1` FOREIGN KEY (`appointment_id`) REFERENCES `appointment` (`appoint_id`) ON DELETE CASCADE,
  CONSTRAINT `prescription_ibfk_2` FOREIGN KEY (`docter_id`) REFERENCES `docter` (`docter_id`) ON UPDATE SET NULL,
  CONSTRAINT `prescription_ibfk_3` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`patient_id`) ON UPDATE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.03 sec)

mysql> SHOW CREATE TABLE prescription_medicine;
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table                 | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| prescription_medicine | CREATE TABLE `prescription_medicine` (
  `prescription_id` int NOT NULL,
  `medi_id` int NOT NULL,
  `dosage` int DEFAULT NULL,
  `duration_days` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`prescription_id`,`medi_id`),
  KEY `medi_id` (`medi_id`),
  CONSTRAINT `prescription_medicine_ibfk_2` FOREIGN KEY (`medi_id`) REFERENCES `medicine` (`medi_id`),
  CONSTRAINT `prescription_medicine_ibfk_3` FOREIGN KEY (`medi_id`) REFERENCES `medicine` (`medi_id`) ON DELETE RESTRICT,
  CONSTRAINT `prescription_medicine_ibfk_4` FOREIGN KEY (`prescription_id`) REFERENCES `prescription` (`prescription_id`) ON UPDATE CASCADE,
  CONSTRAINT `prescription_medicine_ibfk_5` FOREIGN KEY (`prescription_id`) REFERENCES `prescription` (`prescription_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)

mysql> ALTER TABLE prescription_medicine
    -> DROP FOREIGN KEY prescription_medicine_ibfk_2;
Query OK, 0 rows affected (0.05 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> ALTER TABLE prescription_medicine
    -> DROP FOREIGN KEY prescription_medicine_ibfk_4;
Query OK, 0 rows affected (0.05 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> SHOW CREATE TABLE prescription_medicine;
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table                 | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| prescription_medicine | CREATE TABLE `prescription_medicine` (
  `prescription_id` int NOT NULL,
  `medi_id` int NOT NULL,
  `dosage` int DEFAULT NULL,
  `duration_days` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`prescription_id`,`medi_id`),
  KEY `medi_id` (`medi_id`),
  CONSTRAINT `prescription_medicine_ibfk_3` FOREIGN KEY (`medi_id`) REFERENCES `medicine` (`medi_id`) ON DELETE RESTRICT,
  CONSTRAINT `prescription_medicine_ibfk_5` FOREIGN KEY (`prescription_id`) REFERENCES `prescription` (`prescription_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)

mysql> INSERT INTO prescription
    -> (prescription_id, prescription_date, appointment_id, docter_id, patient_id, remarks)
    -> VALUES
    -> (601, '2026-09-01', 501, 201, 301, 'BP observation'),
    -> (602, '2026-09-01', 502, 202, 302, 'Migraine treatment'),
    -> (603, '2026-09-02', 503, 203, 303, 'Knee pain'),
    -> (604, '2026-09-03', 505, 205, 301, 'Heart checkup'),
    -> (605, '2026-09-03', 506, 203, 305, 'Back pain');
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`a-10 (case study)`.`prescription`, CONSTRAINT `prescription_ibfk_1` FOREIGN KEY (`appointment_id`) REFERENCES `appointment` (`appoint_id`) ON DELETE CASCADE)
