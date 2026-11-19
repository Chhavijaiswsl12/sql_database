QNO  5: TRUNCATE Table
Task:

Truncate all data from students table----------------------------------------------------------------------
mysql> use book_db;

mysql> create table book1 (book_id int auto_increment primary key,title varchar(150),author varchar(100),genre varchar(50),publication_year int,price decimal(6,2),publisher varchar(100));

mysql> insert into book1 select * from book;

mysql> desc book1;
+------------------+--------------+------+-----+---------+----------------+
| Field            | Type         | Null | Key | Default | Extra          |
+------------------+--------------+------+-----+---------+----------------+
| book_id          | int          | NO   | PRI | NULL    | auto_increment |
| title            | varchar(150) | YES  |     | NULL    |                |
| author           | varchar(100) | YES  |     | NULL    |                |
| genre            | varchar(50)  | YES  |     | NULL    |                |
| publication_year | int          | YES  |     | NULL    |                |
| price            | decimal(6,2) | YES  |     | NULL    |                |
| publisher        | varchar(100) | YES  |     | NULL    |                |
+------------------+--------------+------+-----+---------+----------------+

mysql> select * from book1;
+---------+------------------+----------------------+---------------+------------------+--------+----------------------+
| book_id | title            | author               | genre         | publication_year | price  | publisher            |
+---------+------------------+----------------------+---------------+------------------+--------+----------------------+
|       1 | The Alchemist    | Paulo Coelho         | Fiction       |             1988 | 299.00 | HarperCollins        |
|       2 | Wings of Fire    | A. P. J. Abdul Kalam | Autobiography |             1999 | 350.00 | Universities Press   |
|       3 | Atomic Habits    | James Clear          | Self-Help     |             2018 | 499.00 | Penguin Random House |
|       4 | The Great Gatsby | F. Scott Fitzgerald  | Classic       |             1925 | 250.00 | Scribner             |
+---------+------------------+----------------------+---------------+------------------+--------+----------------------+
4 rows in set (0.00 sec)


mysql> truncate table book1;
Query OK, 0 rows affected (0.03 sec)

mysql> select * from book1;
Empty set (0.00 sec)

mysql> desc book1;
+------------------+--------------+------+-----+---------+----------------+
| Field            | Type         | Null | Key | Default | Extra          |
+------------------+--------------+------+-----+---------+----------------+
| book_id          | int          | NO   | PRI | NULL    | auto_increment |
| title            | varchar(150) | YES  |     | NULL    |                |
| author           | varchar(100) | YES  |     | NULL    |                |
| genre            | varchar(50)  | YES  |     | NULL    |                |
| publication_year | int          | YES  |     | NULL    |                |
| price            | decimal(6,2) | YES  |     | NULL    |                |
| publisher        | varchar(100) | YES  |     | NULL    |                |
+------------------+--------------+------+-----+---------+----------------+
7 rows in set (0.00 sec)
--------------------------------------------------------------------------------------------------


QNO  4: RENAME Table
Task:

Rename books table to library_books

mysql> alter table book rename to library_books;
Query OK, 0 rows affected (0.03 sec)

mysql> show tables;
+-------------------+
| Tables_in_book_db |
+-------------------+
| book1             |
| library_books     |
+-------------------+
2 rows in set (0.02 sec)