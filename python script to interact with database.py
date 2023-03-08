#!/usr/bin/python3

import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="192.168.1.154",
  user="dan",
  password="dan",
  database="dvwa"
)

# Get a cursor object
mycursor = mydb.cursor()

# Define the new user's information
username = "dan"
password = "dan"

# Execute the SQL query to insert the new user into the database
sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
val = (dan, dan)
mycursor.execute(sql, val)

# Commit the changes to the database
mydb.commit()

# Print a message indicating that the user has been added
print(mycursor.rowcount, "user inserted.")
