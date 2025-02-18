import mysql.connector

# Replace these values with your MySQL server details
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'your_database'
}

def create_connection():
    return mysql.connector.connect(**db_config)

def create_employee_table():
    conn = create_connection()
    cursor = conn.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employee (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        sex VARCHAR(10),
        class VARCHAR(50)
    );
    """
    cursor.execute(create_table_query)
    print("Employee table created successfully.")
    cursor.close()
    conn.close()

def insert_employee(name, age, sex, class_name):
    conn = create_connection()
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO employee (name, age, sex, class)
    VALUES (%s, %d, %s, %s)
    """
    cursor.execute(insert_query, (name, age, sex, class_name))
    conn.commit()
    print("Employee inserted successfully.")
    cursor.close()
    conn.close()

def update_employee(employee_id, name=None, age=None, sex=None, class_name=None):
    conn = create_connection()
    cursor = conn.cursor()
    update_query = "UPDATE employee SET "
    update_values = []
    if name:
        update_query += "name = %s, "
        update_values.append(name)
    if age:
        update_query += "age = %s, "
        update_values.append(age)
    if sex:
        update_query += "sex = %s, "
        update_values.append(sex)
    if class_name:
        update_query += "class = %s, "
        update_values.append(class_name)
    update_query = update_query.rstrip(", ") + " WHERE id = %s"
    update_values.append(employee_id)
    cursor.execute(update_query, tuple(update_values))
    conn.commit()
    print("Employee updated successfully.")
    cursor.close()
    conn.close()

def delete_employee(employee_id):
    conn = create_connection()
    cursor = conn.cursor()
    delete_query = "DELETE FROM employee WHERE id = %s"
    cursor.execute(delete_query, (employee_id,))
    conn.commit()
    print("Employee deleted successfully.")
    cursor.close()
    conn.close()

# Example usage
if __name__ == "__main__":
    create_employee_table()
    insert_employee("John Doe", 30, "Male", "Engineering")
    update_employee(1, age=31)
    delete_employee(1)