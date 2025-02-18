import mysql.connector

# Replace these values with your MySQL server details
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'your_database'
}

# Connect to the MySQL database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# SQL query to create the employee table
create_table_query = """
CREATE TABLE employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    sex VARCHAR(10),
    class VARCHAR(50)
);
"""

# Execute the query
cursor.execute(create_table_query)
print("Employee table created successfully.")

# Close the cursor and connection
cursor.close()
conn.close()