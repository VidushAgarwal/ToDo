import mysql.connector
pa=input("Enter MySql root password")
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pa"
)

mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE todo")
except Exception:
    pass