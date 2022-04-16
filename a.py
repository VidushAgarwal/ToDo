from distutils.util import execute
import mysql.connector
def abc():
  pa=input("Enter MySql root password : ")
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=pa
  )
  f=open("first.ch","w")
  f.write('1\n')
  f.write(pa)
  f.close()
  f=open("first.ch","r")
  a=f.readlines()
  f.close()
  mycursor = mydb.cursor()
  try:
      mycursor.execute("CREATE DATABASE todo")
      mycursor.execute("USE DATABASE todo")
      mycursor.execute("CREATE TABLE data(uname varchar(20))")
  except Exception:
      pass