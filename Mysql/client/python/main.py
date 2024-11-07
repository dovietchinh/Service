import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="test",
    password="test",
    port=3306,
)

# Print connection object to ensure connection is successful
print("Connected to:", mydb)

# Create a cursor object
cur = mydb.cursor(buffered=True)

# Use the database (not necessary since you already specified it in the connection)
# List all databases

cur.execute("USE test")
cur.execute("SHOW DATABASES")
print(cur.fetchall())
cur.execute("SELECT * FROM employees")
a = cur.fetchone()
print(a)

cur.close()

cur = mydb.cursor()
cur.execute("SELECT * FROM employees")
a = cur.fetchall()
print(a)

