-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.

SELECT name FROM cities WHERE name='california' ORDER BY cities.id DESC
