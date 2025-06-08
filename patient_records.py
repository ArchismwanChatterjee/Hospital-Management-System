import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('online_hospital_management_system.db')
cursor = conn.cursor()


# Create MedicalHistory table
cursor.execute('''
CREATE TABLE IF NOT EXISTS MedicalHistory (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    description TEXT,
    date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
)
''')

# Create LabReports table
cursor.execute('''
CREATE TABLE IF NOT EXISTS LabReports (
    report_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    report_date DATE,
    report_description TEXT,
    report_file BLOB,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
)
''')

# Create Prescriptions table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Prescriptions (
    prescription_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    doctor_id INTEGER,
    prescription_date DATE,
    medications TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
)
''')

# Create TreatmentPlans table
cursor.execute('''
CREATE TABLE IF NOT EXISTS TreatmentPlans (
    treatment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    doctor_id INTEGER,
    start_date DATE,
    end_date DATE,
    treatment_description TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
)
''')

# Create ProgressTracking table
cursor.execute('''
CREATE TABLE IF NOT EXISTS ProgressTracking (
    progress_id INTEGER PRIMARY KEY AUTOINCREMENT,
    treatment_id INTEGER,
    date DATE,
    progress_notes TEXT,
    FOREIGN KEY (treatment_id) REFERENCES TreatmentPlans(treatment_id)
)
''')

# Create Billing table with doctor_name and patient_name
cursor.execute('''
CREATE TABLE IF NOT EXISTS Billing (
    billing_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    doctor_id INTEGER,
    doctor_name TEXT,
    patient_name TEXT,
    amount DECIMAL(10, 2),
    date DATE NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
)
''')

# with open('Database Schema Python.pdf', 'rb') as file:
#     pdf_data = file.read()

# Insert dummy data
cursor.execute("INSERT INTO MedicalHistory (patient_id, description, date) VALUES (1, 'History of hypertension', '2023-01-01')")
cursor.execute("INSERT INTO LabReports (patient_id, report_date, report_description, report_file) VALUES (1, '2023-02-01', 'Blood test report', NULL)")
cursor.execute("INSERT INTO Prescriptions (patient_id, doctor_id, prescription_date, medications) VALUES (1, 1, '2023-03-01', 'Medication A, Medication B')")
cursor.execute("INSERT INTO TreatmentPlans (patient_id, doctor_id, start_date, end_date, treatment_description) VALUES (1, 1, '2023-04-01', '2023-06-01', 'Treatment plan for hypertension')")
cursor.execute("INSERT INTO ProgressTracking (treatment_id, date, progress_notes) VALUES (1, '2023-05-01', 'Blood pressure improved')")
cursor.execute('INSERT INTO Billing (patient_id, doctor_id, doctor_name, patient_name, amount, date) VALUES (1, 1, "Dr. Smith", "John Doe", 100.00, "2024-08-01")')

# Commit the changes and close the connection
conn.commit()
conn.close()
