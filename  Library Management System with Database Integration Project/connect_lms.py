import mysql.connector
from mysql.connector import Error

def connect_db():
    # connecting to OUR database - e_commerce_db
    db_name = "library_management_system"
    user = "root"
    password = "Hammond45!"
    host = "localhost" #127.0.0.1

    try:
        # attempting to establish a connection
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )

        # checking if the connection is succesful
        if conn.is_connected(): #returns True if a connection was successfully made
            print("(*￣3￣)╭")
            return conn
            
        # handling any connection errors
    except Error as e:
        print(f"Error: {e}")

connect_db()