import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('online_hospital_management_system.db')
cursor = conn.cursor()


# Insert dummy data into Days
cursor.execute("your_query")

# Commit the changes and close the connection
conn.commit()
conn.close()