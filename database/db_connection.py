import mysql.connector

def get_connection():
    return mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "root" 
    )

db_connection = get_connection()

