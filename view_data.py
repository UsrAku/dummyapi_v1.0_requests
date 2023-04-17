"""
view_data_v1.0 - a simple python script meant for viewing the data in the MySql DB
 - Connects to the MySql DB running in docker and executes a select sql statement for the User_Profiles table
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@uthenticateUser13"
)

cur = mydb.cursor()
cur.execute("USE USER_DB")

sql_stmt = f"SELECT * FROM User_Profiles"

cur.execute(sql_stmt)
response = cur.fetchall()

for row in response:
    print(row[0], row[1], row[2], row[3], row[4])

cur.close()
mydb.close()