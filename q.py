import pymysql
# Define a method to create a database connection
def getDatabaseConnection(ipaddress, usr, passwd, charset, curtype):
    sqlCon  = pymysql.connect(host=ipaddress, user=usr, password=passwd, charset=charset, cursorclass=curtype);
    return sqlCon

# Define a method to create MySQL users
def createUser(cursor, userName, password,
               querynum=0, 
               updatenum=0, 
               connection_num=0):
    try:
        sqlCreateUser = "CREATE USER '%s'@'localhost' IDENTIFIED BY '%s';"%(userName, password)
        cursor.execute(sqlCreateUser)
    except Exception as Ex:
        print("Error creating MySQL User: %s"%(Ex))
passwd=input("Enter root password")
# Connection parameters and access credentials
ipaddress   = "127.0.0.1"  # MySQL server is running on local machine
usr         = "root"       
charset     = "utf8mb4"     
curtype    = pymysql.cursors.DictCursor    

mySQLConnection = getDatabaseConnection(ipaddress, usr, passwd, charset, curtype)
mySQLCursor     = mySQLConnection.cursor()

createUser(mySQLCursor, "todou","todolist")