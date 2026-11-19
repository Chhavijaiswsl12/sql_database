mysql> create table employees(employee_id int unsigned auto_increment primary key,
    -> employee_code char(4) not null unique,
    -> employee_name varchar(30) not null,
    -> employee_age tinyint unsigned,
    -> number_of_children smallint unsigned default 0,
    -> experience_months mediumint unsigned default 0,
    -> employee_salary decimal(10,2) not null,
    -> performance_score float,
    -> productivity_score double,
    -> department_id bigint unsigned,
    -> emp_status enum('Active','Inactive','Resigned','On Leave') default 'Active',
    -> skills set('python','java','C++','MongoDB','Pandas'),
    -> gender enum('FEMALE','MALE','OTHER'),
    -> date_of_birth date,
    -> joinig_date date,
    -> login_time time,
    -> interview_datetime datetime,
    -> emp_birth_year year,
    -> is_active boolean default true,
    -> short_note tinytext,
    -> emp_description text,
    -> traning_history mediumtext,
    -> employee_profile longtext,
    -> created_at timestamp default current_timestamp,
    -> updated_at timestamp default current_timestamp on update current_timestamp);
Query OK, 0 rows affected (0.04 sec)

mysql> desc employees;
+--------------------+-------------------------------------------------+------+-----+-------------------+-----------------------------------------------+
| Field              | Type                                            | Null | Key | Default           | Extra                                         |
+--------------------+-------------------------------------------------+------+-----+-------------------+-----------------------------------------------+
| employee_id        | int unsigned                                    | NO   | PRI | NULL              | auto_increment                                |
| employee_code      | char(4)                                         | NO   | UNI | NULL              |                                               |
| employee_name      | varchar(30)                                     | NO   |     | NULL              |                                               |
| employee_age       | tinyint unsigned                                | YES  |     | NULL              |                                               |
| number_of_children | smallint unsigned                               | YES  |     | 0                 |                                               |
| experience_months  | mediumint unsigned                              | YES  |     | 0                 |                                               |
| employee_salary    | decimal(10,2)                                   | NO   |     | NULL              |                                               |
| performance_score  | float                                           | YES  |     | NULL              |                                               |
| productivity_score | double                                          | YES  |     | NULL              |                                               |
| department_id      | bigint unsigned                                 | YES  |     | NULL              |                                               |
| emp_status         | enum('Active','Inactive','Resigned','On Leave') | YES  |     | Active            |                                               |
| skills             | set('python','java','C++','MongoDB','Pandas')   | YES  |     | NULL              |                                               |
| gender             | enum('FEMALE','MALE','OTHER')                   | YES  |     | NULL              |                                               |
| date_of_birth      | date                                            | YES  |     | NULL              |                                               |
| joinig_date        | date                                            | YES  |     | NULL              |                                               |
| login_time         | time                                            | YES  |     | NULL              |                                               |
| interview_datetime | datetime                                        | YES  |     | NULL              |                                               |
| emp_birth_year     | year                                            | YES  |     | NULL              |                                               |
| is_active          | tinyint(1)                                      | YES  |     | 1                 |                                               |
| short_note         | tinytext                                        | YES  |     | NULL              |                                               |
| emp_description    | text                                            | YES  |     | NULL              |                                               |
| traning_history    | mediumtext                                      | YES  |     | NULL              |                                               |
| employee_profile   | longtext                                        | YES  |     | NULL              |                                               |
| created_at         | timestamp                                       | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
| updated_at         | timestamp                                       | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
+--------------------+-------------------------------------------------+------+-----+-------------------+-----------------------------------------------+

mysql> INSERT INTO employees (
    ->     employee_code, employee_name, employee_age, number_of_children,
    ->     experience_months, employee_salary, performance_score,
    ->     productivity_score, department_id, emp_status, skills, gender,
    ->     date_of_birth, joinig_date, login_time, interview_datetime,
    ->     emp_birth_year, is_active, short_note, emp_description,
    ->     traning_history, employee_profile
    -> )
    -> VALUES
    -> ('E001','Amit Sharma',28,1,48,45000.00,85.5,88.75,101,'Active','python,java','MALE','1998-03-12','2022-10-10','09:00:00','2022-09-25 10:30:00',1998,TRUE,'Hardworking','Software developer','Python and Java training','Experienced software developer'),
    -> ('E002','Priya Verma',26,0,36,52000.00,92.3,94.65,102,'Active','python,Pandas','FEMALE','2000-06-18','2023-01-15','09:15:00','2022-12-20 11:00:00',2000,TRUE,'Team player','Data analyst','Python training','Data analyst skilled in Python'),
    -> ('E003','Rahul Patel',32,2,96,68000.00,78.6,81.25,103,'Active','java,MongoDB','MALE','1994-01-25','2018-05-01','08:45:00','2018-04-15 09:30:00',1994,TRUE,'Experienced','Backend developer','Java training','Backend developer with database experience'),
    -> ('E004','Sneha Gupta',25,0,24,38000.00,88.9,90.40,101,'Active','python,C++','FEMALE','2001-08-09','2024-03-11','09:30:00','2024-02-25 14:00:00',2001,TRUE,'Quick learner','Junior developer','C++ training','Junior software developer'),
    -> ('E005','Vikas Singh',35,2,120,75000.00,81.2,83.60,104,'Inactive','java,MongoDB','MALE','1991-11-05','2016-07-18','10:00:00','2016-07-01 10:00:00',1991,FALSE,'On leave','Senior developer','Java training','Senior developer with extensive experience'),
    -> ('E006','Neha Jain',29,1,60,58000.00,95.4,96.80,102,'Active','python,Pandas,MongoDB','FEMALE','1997-02-14','2021-04-05','09:00:00','2021-03-20 12:00:00',1997,TRUE,'Top performer','Data specialist','Data science training','Data specialist focused on analytics'),
    -> ('E007','Karan Mehta',24,0,12,32000.00,72.5,75.90,103,'Active','C++,java','MALE','2002-04-22','2025-06-02','09:45:00','2025-05-20 11:30:00',2002,TRUE,'New employee','Trainee developer','Java training','Entry-level developer'),
    -> ('E008','Anjali Rao',31,1,84,62000.00,89.7,91.20,105,'On Leave','python,MongoDB','FEMALE','1995-09-16','2019-08-12','08:30:00','2019-07-25 10:15:00',1995,FALSE,'On leave','Database specialist','MongoDB training','Database specialist'),
    -> ('E009','Rohit Joshi',27,0,36,47000.00,83.8,86.45,101,'Active','java,python','MALE','1999-12-03','2023-02-20','09:10:00','2023-02-05 13:00:00',1999,TRUE,'Reliable','Software engineer','Java training','Application developer'),
    -> ('E010','Pooja Nair',30,1,72,61000.00,91.6,93.25,102,'Active','python,Pandas','FEMALE','1996-07-27','2020-09-14','09:20:00','2020-08-28 11:45:00',1996,TRUE,'Analytical','Business analyst','Data analysis training','Data reporting specialist'),
    -> ('E011','Manish Yadav',33,2,108,72000.00,76.9,79.35,104,'Resigned','java,C++','MALE','1993-05-11','2017-03-06','08:50:00','2017-02-18 09:45:00',1993,FALSE,'Former employee','Senior programmer','C++ training','Experienced programmer'),
    -> ('E012','Kavya Shah',23,0,6,28000.00,87.2,89.10,105,'Active','python','FEMALE','2003-10-19','2026-04-01','10:15:00','2026-03-15 10:30:00',2003,TRUE,'Fresh graduate','Junior analyst','Python basics','Junior data analyst'),
    -> ('E013','Deepak Mishra',36,3,144,85000.00,94.1,95.70,103,'Active','java,MongoDB,C++','MALE','1990-02-08','2014-01-13','08:40:00','2013-12-20 14:30:00',1990,TRUE,'Senior expert','Technical lead','Advanced programming','Backend technical lead'),
    -> ('E014','Riya Soni',28,1,48,50000.00,90.5,92.15,101,'Active','python,Pandas,java','FEMALE','1998-12-21','2022-06-20','09:05:00','2022-06-05 12:15:00',1998,TRUE,'Dedicated','Software developer','Python and Java training','Developer with data skills'),
    -> ('E015','Arjun Desai',34,2,120,78000.00,84.7,87.30,104,'Active','java,MongoDB,Pandas','MALE','1992-06-30','2016-11-07','09:25:00','2016-10-22 10:45:00',1992,TRUE,'Experienced','Senior engineer','Database training','Senior software engineer');
Query OK, 15 rows affected (0.07 sec)
Records: 15  Duplicates: 0  Warnings: 0

mysql> select * from employees;
+-------------+---------------+---------------+--------------+--------------------+-------------------+-----------------+-------------------+--------------------+---------------+------------+-----------------------+--------+---------------+-------------+------------+---------------------+----------------+-----------+-----------------+---------------------+--------------------------+--------------------------------------------+---------------------+---------------------+
| employee_id | employee_code | employee_name | employee_age | number_of_children | experience_months | employee_salary | performance_score | productivity_score | department_id | emp_status | skills                | gender | date_of_birth | joinig_date | login_time | interview_datetime  | emp_birth_year | is_active | short_note      | emp_description     | traning_history          | employee_profile                           | created_at          | updated_at          |
+-------------+---------------+---------------+--------------+--------------------+-------------------+-----------------+-------------------+--------------------+---------------+------------+-----------------------+--------+---------------+-------------+------------+---------------------+----------------+-----------+-----------------+---------------------+--------------------------+--------------------------------------------+---------------------+---------------------+
|           1 | E001          | Amit Sharma   |           28 |                  1 |                48 |        45000.00 |              85.5 |              88.75 |           101 | Active     | python,java           | MALE   | 1998-03-12    | 2022-10-10  | 09:00:00   | 2022-09-25 10:30:00 |           1998 |         1 | Hardworking     | Software developer  | Python and Java training | Experienced software developer             | 2026-10-15 11:45:34 | 2026-10-15 11:45:34 |
|           2 | E002          | Priya Verma   |           26 |                  0 |                36 |        52000.00 |              92.3 |              94.65 |           102 | Active     | python,Pandas         | FEMALE | 2000-06-18    | 2023-01-15  | 09:15:00   | 2022-12-20 11:00:00 |           2000 |         1 | Team player     | Data analyst        | Python training          | Data analyst skilled in Python             | 2026-10-15 11:45:34 | 2026-10-15 11:45:34 |
|           3 | E003          | Rahul Patel   |           32 |                  2 |                96 |        68000.00 |              78.6 |              81.25 |           103 | Active     | java,MongoDB          | MALE   | 1994-01-25    | 2018-05-01  | 08:45:00   | 2018-04-15 09:30:00 |           1994 |         1 | Experienced     | Backend developer   | Java training            | Backend developer with database experience | 2026-10-15 11:45:34 | 2026-10-15 11:45:34 |
|           4 | E004          | Sneha Gupta   |           25 |                  0 |                24 |        38000.00 |              88.9 |               90.4 |           101 | Active     | python,C++            | FEMALE | 2001-08-09    | 2024-03-11  | 09:30:00   | 2024-02-25 14:00:00 |           2001 |         1 | Quick learner   | Junior developer    | C++ training             | Junior software developer                  | 2026-10-15 11:45:34 | 2026-10-15 11:45:34 |
|           5 | E005          | Vikas Singh   |           35 |                  2 |               120 |        75000.00 |              81.2 |               83.6 |           104 | Inactive   | java,MongoDB          | MALE   | 1991-11-05    | 2016-07-18  | 10:00:00   | 2016-07-01 10:00:00 |           1991 |         0 | On leave        | Senior developer    | Java training            | Senior developer with extensive experience | 2026-10-15 11:45:34 | 2026-10-15 11:45:34 |
|           6 | E006          | Neha Jain     |           29 |                  1 |                60 |        58000.00 |              95.4 |               96.8 |           102 | Active     | python,MongoDB,Pandas | FEMALE | 1997-02-14    | 2021-04-05  | 09:00:00   | 2021-03-20 12:00:00 |           1997 |         1 | Top performer   | Data specialist     | Data science training    | Data specialist focused on analytics       | 2026-10-15 11:45:34 | 2026-10-15 11:45:34 |
|           7 | E007          | Karan Mehta   |           24 |                  0 |                12 |        32000.00 |              72.5 |               75.9 |           103 | Active     | java,C++              | MALE   | 2002-04-22    | 2025-06-02  | 09:45:00   | 2025-05-20 11:30:00 |           2002 |         1 | New employee    | Trainee developer   | Java training            | Entry-level developer                      | 2026-10-15 11:45:34 | 2026-10-15 11:45:34 |
|           8 | E008          | Anjali Rao    |           31 |                  1 |                84 |        62000.00 |              89.7 |               91.2 |           105 | On Leave   | python,MongoDB        | FEMALE | 1995-09-16    | 2019-08-12  | 08:30:00   | 2019-07-25 10:15:00 |           1995 |         0 | On leave        | Database specialist | MongoDB training         | Database specialist                        | 2026-10-15 11:45:34 | 2026-10-15 11:45:34 |
|           9 | E009          | Rohit Joshi   |           27 |                  0 |                36 |        47000.00 |              83.8 |              86.45 |           101 | Active     | python,java           | MALE   | 1999-12-03    | 2023-02-20  | 09:10:00   | 2023-02-05 13:00:00 |           1999 |         1 | Reliable        | Software engineer   | Java training            | Application developer                      | 2026-10-15 11:45:34 | 2026-10-15 11:45:34 |
|          10 | E010          | Pooja Nair    |           30 |                  1 |                72 |        61000.00 |              91.6 |              93.25 |           102 | Active     | python,Pandas         | FEMALE | 1996-07-27    | 2020-09-14  | 09:20:00   | 2020-08-28 11:45:00 |           1996 |         1 | Analytical      | Business analyst    | Data analysis training   | Data reporting specialist                  | 2026-10-15 11:45:34 | 2026-10-15 11:45:34 |
|          11 | E011          | Manish Yadav  |           33 |                  2 |               108 |        72000.00 |              76.9 |              79.35 |           104 | Resigned   | java,C++              | MALE   | 1993-05-11    | 2017-03-06  | 08:50:00   | 2017-02-18 09:45:00 |           1993 |         0 | Former employee | Senior programmer   | C++ training             | Experienced programmer                     | 2026-10-15 11:45:34 | 2026-10-15 11:45:34 |
|          12 | E012          | Kavya Shah    |           23 |                  0 |                 6 |        28000.00 |              87.2 |               89.1 |           105 | Active     | python                | FEMALE | 2003-10-19    | 2026-04-01  | 10:15:00   | 2026-03-15 10:30:00 |           2003 |         1 | Fresh graduate  | Junior analyst      | Python basics            | Junior data analyst                        | 2026-10-15 11:45:34 | 2026-10-15 11:45:34 |
|          13 | E013          | Deepak Mishra |           36 |                  3 |               144 |        85000.00 |              94.1 |               95.7 |           103 | Active     | java,C++,MongoDB      | MALE   | 1990-02-08    | 2014-01-13  | 08:40:00   | 2013-12-20 14:30:00 |           1990 |         1 | Senior expert   | Technical lead      | Advanced programming     | Backend technical lead                     | 2026-10-15 11:45:34 | 2026-10-15 11:45:34 |
|          14 | E014          | Riya Soni     |           28 |                  1 |                48 |        50000.00 |              90.5 |              92.15 |           101 | Active     | python,java,Pandas    | FEMALE | 1998-12-21    | 2022-06-20  | 09:05:00   | 2022-06-05 12:15:00 |           1998 |         1 | Dedicated       | Software developer  | Python and Java training | Developer with data skills                 | 2026-10-15 11:45:34 | 2026-10-15 11:45:34 |
|          15 | E015          | Arjun Desai   |           34 |                  2 |               120 |        78000.00 |              84.7 |               87.3 |           104 | Active     | java,MongoDB,Pandas   | MALE   | 1992-06-30    | 2016-11-07  | 09:25:00   | 2016-10-22 10:45:00 |           1992 |         1 | Experienced     | Senior engineer     | Database training        | Senior software engineer                   | 2026-10-15 11:45:34 | 2026-10-15 11:45:34 |
+-------------+---------------+---------------+--------------+--------------------+-------------------+-----------------+-------------------+--------------------+---------------+------------+-----------------------+--------+---------------+-------------+------------+---------------------+----------------+-----------+-----------------+---------------------+--------------------------+--------------------------------------------+---------------------+---------------------+

mysql> alter table employees add column phone_number varchar(15),add column email varchar(20);

mysql> alter table employees modify employee_name varchar(32),modify employee_code char(6);


mysql> alter table employees rename column short_note to employee_note;
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> alter table employees drop column email,drop column phone_number;
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc employees;
+--------------------+-------------------------------------------------+------+-----+-------------------+-----------------------------------------------+
| Field              | Type                                            | Null | Key | Default           | Extra                                         |
+--------------------+-------------------------------------------------+------+-----+-------------------+-----------------------------------------------+
| employee_id        | int unsigned                                    | NO   | PRI | NULL              | auto_increment                                |
| employee_code      | char(6)                                         | YES  | UNI | NULL              |                                               |
| employee_name      | varchar(32)                                     | YES  |     | NULL              |                                               |
| employee_age       | tinyint unsigned                                | YES  |     | NULL              |                                               |
| number_of_children | smallint unsigned                               | YES  |     | 0                 |                                               |
| experience_months  | mediumint unsigned                              | YES  |     | 0                 |                                               |
| employee_salary    | decimal(10,2)                                   | NO   |     | NULL              |                                               |
| performance_score  | float                                           | YES  |     | NULL              |                                               |
| productivity_score | double                                          | YES  |     | NULL              |                                               |
| department_id      | bigint unsigned                                 | YES  |     | NULL              |                                               |
| emp_status         | enum('Active','Inactive','Resigned','On Leave') | YES  |     | Active            |                                               |
| skills             | set('python','java','C++','MongoDB','Pandas')   | YES  |     | NULL              |                                               |
| gender             | enum('FEMALE','MALE','OTHER')                   | YES  |     | NULL              |                                               |
| date_of_birth      | date                                            | YES  |     | NULL              |                                               |
| joinig_date        | date                                            | YES  |     | NULL              |                                               |
| login_time         | time                                            | YES  |     | NULL              |                                               |
| interview_datetime | datetime                                        | YES  |     | NULL              |                                               |
| emp_birth_year     | year                                            | YES  |     | NULL              |                                               |
| is_active          | tinyint(1)                                      | YES  |     | 1                 |                                               |
| employee_note      | tinytext                                        | YES  |     | NULL              |                                               |
| emp_description    | text                                            | YES  |     | NULL              |                                               |
| traning_history    | mediumtext                                      | YES  |     | NULL              |                                               |
| employee_profile   | longtext                                        | YES  |     | NULL              |                                               |
| created_at         | timestamp                                       | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
| updated_at         | timestamp                                       | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
+--------------------+-------------------------------------------------+------+-----+-------------------+-----------------------------------------------+
