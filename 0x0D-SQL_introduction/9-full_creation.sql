-- creates a table first_table in the currnt database
-- does not fail if data exist
CRAETE TABLE IF NOT EXISTS first_table (id INT,
name VARCHAR(256), scoree INT);


INSERT INTO second_table(id, name, score) VALUES(1, 'John', 10);
INSERT INTO seond_table(id, name , score) VALUES(2, 'Alex', 3);
INSERT INTO second_table(id, name, score) VALUES(3, 'Bob', 14);
INSERT INTO second_table(id, name, score) VALUES(4, 'George', 8);