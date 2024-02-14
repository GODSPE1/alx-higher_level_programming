#0x0E. SQL - More queries

##Resources
##Read or watch:

1. How To Create a New User and Grant Permissions in MySQL
1. How To Use MySQL GRANT Statement To Grant Privileges To a User
1. MySQL constraints
1. SQL technique: subqueries
1. Basic query operation: the join
1. SQL technique: multiple joins and the distinct keyword
1. SQL technique: join types
1. SQL technique: union and minus
1. MySQL Cheat Sheet
1. The Seven Types of SQL Joins
1. MySQL Tutorial
1. SQL Style Guide
1. MySQL 8.0 SQL Statement Syntax
### Extra resources around relational database model design:

1. Design
1. Normalization
1. ER Modeling

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a PRIMARY KEY
- What’s a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are JOIN and UNION

**How to import a SQL dump**
```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```
