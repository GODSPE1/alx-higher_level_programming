-- script that creates the MySQL server user user_0d_1

CREATE USER IF EXISTS user_0d_1@localhost IDENTIFIED WITH user_0d_1_pwd;
GRANT ALL PRIVILEDGES ON *.* TO 'user_0d_'@'localhost';
