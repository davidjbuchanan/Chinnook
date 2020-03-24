import os
import pymysql

import env

print(os.environ.get("EMAIL"))
print(os.environ.get("PASSWORD"))

# Connect to the database
connection = pymysql.connect(host=os.environ.get("EXAMPLE"),
                             
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()

