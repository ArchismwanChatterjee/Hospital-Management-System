import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('online_hospital_management_system.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS Days (
    day_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE NOT NULL
)
''')

# Create Doctors table with additional fields
cursor.execute('''
CREATE TABLE IF NOT EXISTS Doctors (
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    contact_info VARCHAR(255),
    address VARCHAR(255),
    date_of_birth DATE,
    gender VARCHAR(50),
    email VARCHAR(255),
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
)
''')

# Create Patients table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    contact_info VARCHAR(255),
    address VARCHAR(255),
    date_of_birth DATE,
    gender VARCHAR(50),
    email VARCHAR(255)
)
''')

# Create Appointments table with doctor_name and patient_name
cursor.execute('''
CREATE TABLE IF NOT EXISTS Appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    day_id INTEGER,
    doctor_id INTEGER,
    patient_id INTEGER,
    doctor_name VARCHAR(255),
    patient_name VARCHAR(255),
    time TIME NOT NULL,
    FOREIGN KEY (day_id) REFERENCES Days(day_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
)
''')

# Insert dummy data
cursor.execute("INSERT INTO Days (date) VALUES ('2024-08-01')")
cursor.execute("INSERT INTO Doctors (name, contact_info, address, date_of_birth, gender, email, department_id) VALUES ('Dr. Smith', '555-1234', '123 Elm St', '1980-01-01', 'Male', 'dr.smith@example.com', 1)")
cursor.execute("INSERT INTO Patients (name, contact_info, address, date_of_birth, gender, email) VALUES ('John Doe', '123456789', '456 Oak St', '1990-05-15', 'Male', 'john.doe@example.com')")
cursor.execute("INSERT INTO Appointments (day_id, doctor_id, patient_id, doctor_name, patient_name, time) VALUES (1, 1, 1, 'Dr. Smith', 'John Doe', '10:00')")

# Commit the changes and close the connection
conn.commit()
conn.close()
