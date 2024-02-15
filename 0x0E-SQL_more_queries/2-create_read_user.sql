-- script that creates the database hbtn_0d_2 and the user user_0d_2.

CREATE DATABASE IF EXIST hbtn_0d_2;
CREATE USER IF EXISTS user_0d_2@localhost IDENTIFIED WITH user_0d_2_pwd;
GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';
