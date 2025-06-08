import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('online_hospital_management_system.db')
cursor = conn.cursor()

# Create Departments table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL
)
''')

# Create Staff table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    role VARCHAR(255) NOT NULL,
    department_id INTEGER,
    contact_info VARCHAR(255),
    address VARCHAR(255),
    date_of_birth DATE,
    gender VARCHAR(50),
    email VARCHAR(255),
    hire_date DATE,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
)
''')

# Create Schedules table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Schedules (
    schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    staff_id INTEGER,
    date DATE,
    shift VARCHAR(50),
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id)
)
''')

# Create Payroll table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Payroll (
    payroll_id INTEGER PRIMARY KEY AUTOINCREMENT,
    staff_id INTEGER,
    salary DECIMAL,
    pay_date DATE,
    bonus DECIMAL,
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id)
)
''')

# Insert dummy data
cursor.execute("INSERT INTO Departments (name) VALUES ('Cardiology')")
cursor.execute("INSERT INTO Staff (name, role, department_id, contact_info, address, date_of_birth, gender, email, hire_date) VALUES ('Dr. Smith', 'Doctor', 1, '123456789', '123 Main St', '1970-01-01', 'Male', 'drsmith@example.com', '2000-01-01')")
cursor.execute("INSERT INTO Schedules (staff_id, date, shift) VALUES (1, '2024-08-01', 'Morning')")
cursor.execute("INSERT INTO Payroll (staff_id, salary, pay_date, bonus) VALUES (1, 100000.00, '2024-07-31', 5000.00)")

# Commit the changes and close the connection
conn.commit()
conn.close()
