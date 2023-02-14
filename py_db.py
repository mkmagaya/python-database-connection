# import mysql.connector

# cnx = mysql.connector.connect(user='mkmagaya', password='61251998',
#                               host='localhost', #host='127.0.0.1',
#                               database='school_db')
# cnx.close()


"""To handle connection errors, use the try statement and catch all errors using the errors.Error exception:
"""
# import mysql.connector
# from mysql.connector import errorcode

# try:
#     cnx = mysql.connector.connect(user='mkmagaya', password='61251998', host='localhost',
#                                 database='school_db')
#     print("Successiful Connection!!!")
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Something is wrong with your user name or password")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("Database does not exist")
#   else:
#     print(err)
# else:
#   cnx.close()


"""Defining connection arguments in a dictionary and using the ** operator is another option:
"""

# import mysql.connector

# config = {
#     'user': 'mkmagaya',
#     'password': '61251998',
#     'host': '127.0.0.1',
#     'database': 'school_db',
#     'raise_on_warnings': True,
#     'use_pure': False,
# }
# """Setting use_pure=False causes the connection to use the C Extension 
# if your Connector/Python installation includes it, 
# while use_pure=True to False means the Python implementation 
# is used if available.
# """
# cnx = mysql.connector.connect(**config)

# cnx.close()


"""The first step in interacting with a MySQL server is to establish a connection. 
To do this, you need connect() from the mysql.connector module. 
This function takes in parameters like host, user, and password and returns a MySQLConnection object.
You can receive these credentials as input from the user and pass them to connect():
"""

from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        print(f"MySQLConnection object: {connection} means successiful connection")
except Error as e:
    print(e)