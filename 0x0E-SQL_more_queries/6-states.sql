-- script that creates the database hbtn_0d_2 and the user user_0d_2.

CREATE DATABASE IF NOT EXIST hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS user_0d_usa.states (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
