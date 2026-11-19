mysql> create database MOVIE_REVIEW_SYSTEM;
Query OK, 1 row affected (0.00 sec)

mysql> use MOVIE_REVIEW_SYSTEM;
Database changed
mysql> create table movie_reviews(review_id INT,movie_title VARCHAR(150),reviewer_name VARCHAR(100),rating DECIMAL(2,1),review_text TEXT);
Query OK, 0 rows affected (0.01 sec)

mysql> desc movie_reviews;
+---------------+--------------+------+-----+---------+-------+
| Field         | Type         | Null | Key | Default | Extra |
+---------------+--------------+------+-----+---------+-------+
| review_id     | int          | YES  |     | NULL    |       |
| movie_title   | varchar(150) | YES  |     | NULL    |       |
| reviewer_name | varchar(100) | YES  |     | NULL    |       |
| rating        | decimal(2,1) | YES  |     | NULL    |       |
| review_text   | text         | YES  |     | NULL    |       |
+---------------+--------------+------+-----+---------+-------+
5 rows in set (0.00 sec)

mysql> INSERT INTO movie_reviews
    -> (review_id, movie_title, reviewer_name, rating, review_text)
    -> VALUES
    -> (1, '3 Idiots', 'Rahul Sharma', 9.0, 'An inspiring movie about education and friendship.'),
    -> (2, 'Dangal', 'Priya Verma', 8.5, 'A great movie about determination and sports.'),
    -> (3, 'Taare Zameen Par', 'Amit Patel', 9.5, 'An emotional movie about children and learning.');
Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from movie_reviews;
+-----------+------------------+---------------+--------+----------------------------------------------------+
| review_id | movie_title      | reviewer_name | rating | review_text                                        |
+-----------+------------------+---------------+--------+----------------------------------------------------+
|         1 | 3 Idiots         | Rahul Sharma  |    9.0 | An inspiring movie about education and friendship. |
|         2 | Dangal           | Priya Verma   |    8.5 | A great movie about determination and sports.      |
|         3 | Taare Zameen Par | Amit Patel    |    9.5 | An emotional movie about children and learning.    |
+-----------+------------------+---------------+--------+----------------------------------------------------+

mysql> alter table movie_reviews add column review_date DATE,add column platform VARCHAR(50);
Query OK, 0 rows affected (0.01 sec)