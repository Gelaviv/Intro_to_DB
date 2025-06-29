import mysql.connector
import os

from dotenv import load_dotenv

load_dotenv()

def my_db_connector():
    try:
        connected = mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_NAME")
        )
        print ("Mysql is connected")
        return connected

    except Exception as e:
        print(f"except mysql.connector.Error{e}")
        return None
    

def create_database():
    try:
        # Connect without specifying a database to create a new one
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            connection.commit()
            
            print("Database 'alx_book_store' created successfully!")
            
    except Exception as e:
        print(f"except mysql.connector.Error{e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
if __name__ == "__main__":
    
    create_database()

my_db_connector()


