import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='todo',
                                         user='root',
                                         password='root')

    sql_select_Query = "select * from home_data where uname='Vidush'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)
    print(records)
    print("\nPrinting each row")
    for row in records:
        print("id=", row[0])
        print("Uname = ", row[1])
        print("email = ", row[2])
        print("passw = ", row[3])

except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")