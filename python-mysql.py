import os
import pymysql

# Get your databse username
username = os.getenv('C9_USER')

# connect to the database
connection = pymysql.connect(host='localhost', user=username, password='', db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        rows = cursor.execute("delete from Friends where name = %s;", 'Mike')
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()