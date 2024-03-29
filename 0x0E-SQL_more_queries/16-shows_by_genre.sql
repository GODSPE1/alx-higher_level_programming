-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 15-comedy_only.sql)
-- Write a script that lists all shows, and all genres linked to that show, from the databasehbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != "" ORDER BY score DESC;
