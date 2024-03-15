#!/usr/bin/python3
"""
This Module list all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

db = MySQLdb.connect(user="godspe", password="finish", database="hbtn_0e_0_usa"
)

cur = db.cursor()
query = "SELECT * FROM hbtn_0e_0_usa ORDER BY states_id ASC;"

cur.execute(query)
results = cur.fetchall()

for row in results:
    print(row)

db.close()

if __name__ == "__main__":
    pass
