import mysql.connector
pa=input("Enter MySql root password")
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
print(a[1])
f.close()
mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE todo")
except Exception:
    pass