import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="test",
    password="test",
    port=3306,
    database="test"
)

# Print connection object to ensure connection is successful
print("Connected to:", mydb)

# Create a cursor object
cur = mydb.cursor()

# Use the database (not necessary since you already specified it in the connection)
try:
    cur.execute("USE test")  # This line is optional since the database is specified in the connection
    print("Database 'test' is in use.")
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Example query to verify the connection and database
cur.execute("SHOW TABLES")  # Replace with a query that makes sense for your database
tables = cur.fetchall()

print("Tables in database:")
for table in tables:
    print(table)