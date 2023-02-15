from sqlalchemy import create_engine
import json
import sqlite3


SQLALCHEMY_DATABASE_URL = "sqlite:///personal_data.sqlite3"
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=5, max_overflow=0, connect_args={"check_same_thread": False},echo=True)

def create_database():

    # Connect to the database
    conn = sqlite3.connect("personal_data.sqlite3")

    # Create a cursor
    cursor = conn.cursor()

    # Create the table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            gender TEXT NOT NULL,
            ip_address TEXT NOT NULL,
            country_code TEXT NOT NULL
            
        )
    """)

    # Parse the JSON file
    with open('data.json', 'r') as file:
            data = json.load(file)
    # Load the data into the database
    for record in data:
        print(record["email"])
        cursor.execute("""
            INSERT INTO users (id, first_name, last_name, email, gender, ip_address, country_code)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (record["id"],record["first_name"], record["last_name"], 
              record["email"], record["gender"],
              record["ip_address"], record["country_code"]))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()
    
    
if __name__ == "__main__":
    create_database()








        