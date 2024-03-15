import MySQLdb

db = MySQLdb.connect(user="godspe", password="finish", database="hbtn_0e_0_usa"
)

cur = db.cursor()
query = "SELECT * FROM hbtn_0e_0_usa ORDER BY states_id ASC;"

cur.execute(query)
results = cur.fetchall()

for row in results:
    print(row)  # Adjust this to format the output according to the example

db.close()

if __name__ == "__main__":
    pass  # Code to execute when the script is run directly
