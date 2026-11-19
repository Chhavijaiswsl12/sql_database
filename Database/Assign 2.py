QNO  2: Create and Populate books Table
Columns:

book_id INT

title VARCHAR(150)

author VARCHAR(100)

genre VARCHAR(50)

publication_year INT

price DECIMAL(6,2)

publisher VARCHAR(100)

Task:

Insert 4 book records.

mysql> create database Book_db;
mysql> use book_db;
mysql> create table book (book_id int auto_increment primary key,title varchar(150),author varchar(100),genre varchar(50),publication_year int,price decimal(6,2),publisher varchar(100));

mysql> insert into book (title, author, genre, publication_year, price, publisher)
    -> values
    -> ('The Alchemist', 'Paulo Coelho', 'Fiction', 1988, 299.00, 'HarperCollins'),
    -> ('Wings of Fire', 'A. P. J. Abdul Kalam', 'Autobiography', 1999, 350.00, 'Universities Press'),
    -> ('Atomic Habits', 'James Clear', 'Self-Help', 2018, 499.00, 'Penguin Random House'),
    -> ('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', 1925, 250.00, 'Scribner');

mysql> select * from book;
+---------+------------------+----------------------+---------------+------------------+--------+----------------------+
| book_id | title            | author               | genre         | publication_year | price  | publisher            |
+---------+------------------+----------------------+---------------+------------------+--------+----------------------+
|       1 | The Alchemist    | Paulo Coelho         | Fiction       |             1988 | 299.00 | HarperCollins        |
|       2 | Wings of Fire    | A. P. J. Abdul Kalam | Autobiography |             1999 | 350.00 | Universities Press   |
|       3 | Atomic Habits    | James Clear          | Self-Help     |             2018 | 499.00 | Penguin Random House |
|       4 | The Great Gatsby | F. Scott Fitzgerald  | Classic       |             1925 | 250.00 | Scribner             |
+---------+------------------+----------------------+---------------+------------------+--------+----------------------+
4 rows in set (0.00 sec)