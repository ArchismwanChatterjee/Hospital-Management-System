import streamlit as st
import sqlite3
import pandas as pd

# Connect to SQLite database
def get_connection(db_name):
    return sqlite3.connect(db_name)

def fetch_data(query, conn):
    return pd.read_sql_query(query, conn)

# Streamlit application
def main():

    # Center the logo using st.image
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.write("")
    with col2:
        st.image('logo1.png', width=200)
    with col3:
        st.write("")
    
    
    st.markdown("<h1 style='text-align: center;'>Online Hospital Management System</h1>", unsafe_allow_html=True)
    
    st.subheader('Admin Dashboard')    
    # Create buttons for each table
    option = st.sidebar.selectbox(
        'Select a table to view',
        ['Select', 'Days', 'Appointments','Departments', 'Doctors', 'Patients', 'MedicalHistory', 'LabReports', 
         'Prescriptions', 'TreatmentPlans', 'ProgressTracking', 'Billing', 
         'Staff', 'Schedules', 'Payroll', 'Medications', 'Suppliers', 'Inventory', 'Orders']
    )
    
    conn = get_connection('online_hospital_management_system.db')
    
    if option == 'Days':
        query = 'SELECT * FROM Days'
    elif option == 'Appointments':
        query = 'SELECT * FROM Appointments'
    elif option == 'Departments':
        query = 'SELECT * FROM Departments'
    elif option == 'Doctors':
        query = 'SELECT * FROM Doctors'
    elif option == 'Patients':
        query = 'SELECT * FROM Patients'
    elif option == 'MedicalHistory':
        query = 'SELECT * FROM MedicalHistory'
    elif option == 'LabReports':
        query = 'SELECT * FROM LabReports'
    elif option == 'Prescriptions':
        query = 'SELECT * FROM Prescriptions'
    elif option == 'TreatmentPlans':
        query = 'SELECT * FROM TreatmentPlans'
    elif option == 'ProgressTracking':
        query = 'SELECT * FROM ProgressTracking'
    elif option == 'Billing':
        query = 'SELECT * FROM Billing'
    elif option == 'Staff':
        query = 'SELECT * FROM Staff'
    elif option == 'Schedules':
        query = 'SELECT * FROM Schedules'
    elif option == 'Payroll':
        query = 'SELECT * FROM Payroll'
    elif option == 'Medications':
        query = 'SELECT * FROM Medications'
    elif option == 'Suppliers':
        query = 'SELECT * FROM Suppliers'
    elif option == 'Inventory':
        query = 'SELECT * FROM Inventory'
    elif option == 'Orders':
        query = 'SELECT * FROM Orders'
    else:
        st.write('Please select a table from the sidebar.')
        return

    if conn:
        data = fetch_data(query, conn)
        conn.close()
        # Custom CSS for styling the table
        st.markdown("""
            <style>
            .dataframe {
                border-collapse: collapse;
                width: 100%;
            }
            .dataframe th, .dataframe td {
                border: 1px solid #ddd;
                padding: 8px;
            }
            .dataframe th {
                padding-top: 12px;
                padding-bottom: 12px;
                text-align: left;
                background-color: #4CAF50;
                color: white;
            }
            </style>
            """, unsafe_allow_html=True)

        # Display the styled table
        st.write(data.to_html(classes='dataframe'), unsafe_allow_html=True)
    else:
        st.write('No database connection available.')

if __name__ == '__main__':
    main()
