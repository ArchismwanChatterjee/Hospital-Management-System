import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('online_hospital_management_system.db')
cursor = conn.cursor()

# Create Medications table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Medications (
    medication_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category VARCHAR(255),
    price DECIMAL
)
''')

# Create Suppliers table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    contact_info VARCHAR(255),
    address VARCHAR(255),
    email VARCHAR(255)
)
''')

# Create Inventory table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Inventory (
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    medication_id INTEGER,
    quantity INTEGER,
    expiration_date DATE,
    FOREIGN KEY (medication_id) REFERENCES Medications(medication_id)
)
''')

# Create Orders table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    medication_id INTEGER,
    supplier_id INTEGER,
    order_date DATE,
    quantity INTEGER,
    total_price DECIMAL,
    FOREIGN KEY (medication_id) REFERENCES Medications(medication_id),
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
)
''')

# Insert dummy data
cursor.execute("INSERT INTO Medications (name, description, category, price) VALUES ('Paracetamol', 'Pain relief', 'Analgesic', 0.50)")
cursor.execute("INSERT INTO Suppliers (name, contact_info, address, email) VALUES ('Pharma Supplier Inc.', '123456789', '456 Main St', 'supplier@example.com')")
cursor.execute("INSERT INTO Inventory (medication_id, quantity, expiration_date) VALUES (1, 100, '2025-12-31')")
cursor.execute("INSERT INTO Orders (medication_id, supplier_id, order_date, quantity, total_price) VALUES (1, 1, '2024-07-31', 100, 50.00)")

# Commit the changes and close the connection
conn.commit()
conn.close()
