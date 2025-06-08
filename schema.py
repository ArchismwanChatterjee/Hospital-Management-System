# hospital_management.py

from sqlalchemy import create_engine, Column, String, Integer, Date, Time, Text, ForeignKey, BLOB, DECIMAL, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Day(Base):
    __tablename__ = 'days'
    day_id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)

class Department(Base):
    __tablename__ = 'departments'
    department_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Doctor(Base):
    __tablename__ = 'doctors'
    doctor_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)
    address = Column(String)
    date_of_birth = Column(Date)
    gender = Column(String(50))
    email = Column(String)
    department_id = Column(Integer, ForeignKey('departments.department_id'), nullable=False)

    department = relationship("Department", back_populates="doctors")

Department.doctors = relationship("Doctor", order_by=Doctor.doctor_id, back_populates="department")

class Patient(Base):
    __tablename__ = 'patients'
    patient_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)
    address = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    email = Column(String, nullable=False)

    medical_histories = relationship("MedicalHistory", order_by="MedicalHistory.history_id", back_populates="patient")
    lab_reports = relationship("LabReport", order_by="LabReport.report_id", back_populates="patient")
    prescriptions = relationship("Prescription", order_by="Prescription.prescription_id", back_populates="patient")
    treatment_plans = relationship("TreatmentPlan", order_by="TreatmentPlan.treatment_id", back_populates="patient")
    billings = relationship("Billing", order_by="Billing.billing_id", back_populates="patient")
    appointments = relationship("Appointment", order_by="Appointment.appointment_id", back_populates="patient")

class Appointment(Base):
    __tablename__ = 'appointments'
    appointment_id = Column(Integer, primary_key=True)
    day_id = Column(Integer, ForeignKey('days.day_id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.doctor_id'), nullable=False)
    patient_id = Column(Integer, ForeignKey('patients.patient_id'), nullable=False)
    time = Column(Time, nullable=False)

    day = relationship("Day", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")
    patient = relationship("Patient", back_populates="appointments")

Day.appointments = relationship("Appointment", order_by=Appointment.appointment_id, back_populates="day")
Doctor.appointments = relationship("Appointment", order_by=Appointment.appointment_id, back_populates="doctor")

class MedicalHistory(Base):
    __tablename__ = 'medical_history'
    history_id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.patient_id'), nullable=False)
    description = Column(Text, nullable=False)
    date = Column(Date, nullable=False)

    patient = relationship("Patient", back_populates="medical_histories")

class LabReport(Base):
    __tablename__ = 'lab_reports'
    report_id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.patient_id'), nullable=False)
    report_date = Column(Date, nullable=False)
    report_description = Column(Text, nullable=False)
    report_file = Column(BLOB, nullable=False)

    patient = relationship("Patient", back_populates="lab_reports")

class Prescription(Base):
    __tablename__ = 'prescriptions'
    prescription_id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.patient_id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.doctor_id'), nullable=False)
    prescription_date = Column(Date, nullable=False)
    medications = Column(Text, nullable=False)

    patient = relationship("Patient", back_populates="prescriptions")

class TreatmentPlan(Base):
    __tablename__ = 'treatment_plans'
    treatment_id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.patient_id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.doctor_id'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    treatment_description = Column(Text, nullable=False)

    patient = relationship("Patient", back_populates="treatment_plans")

class ProgressTracking(Base):
    __tablename__ = 'progress_tracking'
    progress_id = Column(Integer, primary_key=True)
    treatment_id = Column(Integer, ForeignKey('treatment_plans.treatment_id'), nullable=False)
    date = Column(Date, nullable=False)
    progress_notes = Column(Text, nullable=False)

    treatment_plan = relationship("TreatmentPlan", back_populates="progress_trackings")

TreatmentPlan.progress_trackings = relationship("ProgressTracking", order_by=ProgressTracking.progress_id, back_populates="treatment_plan")

class Billing(Base):
    __tablename__ = 'billing'
    billing_id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.patient_id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.doctor_id'), nullable=True)
    doctor_name = Column(String)
    patient_name = Column(String)
    amount = Column(DECIMAL(10, 2), nullable=False)
    date = Column(Date, nullable=False)
    paid = Column(Boolean, default=False)

    patient = relationship("Patient", back_populates="billings")
    doctor = relationship("Doctor")

# New Tables for Staff and Payroll Management
class Staff(Base):
    __tablename__ = 'staff'
    staff_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)  # e.g., Doctor, Nurse, Admin
    department_id = Column(Integer, ForeignKey('departments.department_id'), nullable=False)
    contact_info = Column(String, nullable=False)
    address = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hire_date = Column(Date, nullable=False)

    department = relationship("Department", back_populates="staff_members")
    schedules = relationship("Schedule", order_by="Schedule.schedule_id", back_populates="staff")
    payrolls = relationship("Payroll", order_by="Payroll.payroll_id", back_populates="staff")

Department.staff_members = relationship("Staff", order_by=Staff.staff_id, back_populates="department")

class Schedule(Base):
    __tablename__ = 'schedules'
    schedule_id = Column(Integer, primary_key=True)
    staff_id = Column(Integer, ForeignKey('staff.staff_id'), nullable=False)
    date = Column(Date, nullable=False)
    shift = Column(String, nullable=False)  # e.g., Morning, Evening, Night

    staff = relationship("Staff", back_populates="schedules")

class Payroll(Base):
    __tablename__ = 'payroll'
    payroll_id = Column(Integer, primary_key=True)
    staff_id = Column(Integer, ForeignKey('staff.staff_id'), nullable=False)
    salary = Column(DECIMAL, nullable=False)
    pay_date = Column(Date, nullable=False)
    bonus = Column(DECIMAL, nullable=True)

    staff = relationship("Staff", back_populates="payrolls")


class Medication(Base):
    __tablename__ = 'medications'
    medication_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    category = Column(String, nullable=False)  # e.g., Antibiotic, Analgesic
    price = Column(DECIMAL, nullable=False)

class Supplier(Base):
    __tablename__ = 'suppliers'
    supplier_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, nullable=False)

class Inventory(Base):
    __tablename__ = 'inventory'
    inventory_id = Column(Integer, primary_key=True)
    medication_id = Column(Integer, ForeignKey('medications.medication_id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    expiration_date = Column(Date, nullable=False)

    medication = relationship("Medication", back_populates="inventories")

Medication.inventories = relationship("Inventory", order_by=Inventory.inventory_id, back_populates="medication")

class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    medication_id = Column(Integer, ForeignKey('medications.medication_id'), nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id'), nullable=False)
    order_date = Column(Date, nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(DECIMAL, nullable=False)

    medication = relationship("Medication", back_populates="orders")
    supplier = relationship("Supplier", back_populates="orders")

Medication.orders = relationship("Order", order_by=Order.order_id, back_populates="medication")
Supplier.orders = relationship("Order", order_by=Order.order_id, back_populates="supplier")


engine = create_engine('sqlite:///online_hospital_system.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
