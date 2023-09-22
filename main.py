import random
import datetime


class Person:
    def __init__(self, name, age, gender, address, contact):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.contact = contact

    def get_person_details(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nAddress: {self.address}\nContact: {self.contact}"


class Patient(Person):
    def __init__(self, name, age, gender, address, contact):
        super().__init__(name, age, gender, address, contact)


class Doctor(Person):
    def __init__(self, name, specialty, contact):
        super().__init__(name, None, None, None, contact)
        self.specialty = specialty


class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def get_appointment_details(self):
        return f"Appointment Details:\n{self.patient.get_person_details()}\n{self.doctor.get_person_details()}\nDate: {self.date}\nTime: {self.time}"


class Prescription:
    def __init__(self, doctor, patient, medication, dosage, instructions):
        self.doctor = doctor
        self.patient = patient
        self.medication = medication
        self.dosage = dosage
        self.instructions = instructions

    def get_prescription_details(self):
        return f"Prescription Details:\n{self.patient.get_person_details()}\n{self.doctor.get_person_details()}\nMedication: {self.medication}\nDosage: {self.dosage}\nInstructions: {self.instructions}"


class HealthAI:
    def __init__(self, doctors):
        self.doctors = doctors

    def find_doctor_by_specialty(self, specialty):
        matching_doctors = []
        for doctor in self.doctors:
            if doctor.specialty.lower() == specialty.lower():
                matching_doctors.append(doctor)
        return matching_doctors

    def schedule_appointment(self, patient, date, time, specialty):
        available_doctors = self.find_doctor_by_specialty(specialty)
        if available_doctors:
            doctor = random.choice(available_doctors)
            appointment = Appointment(patient, doctor, date, time)
            return appointment
        else:
            return None

    def prescribe_medication(self, doctor, patient, medication, dosage, instructions):
        prescription = Prescription(
            doctor, patient, medication, dosage, instructions)
        return prescription


class Hospital:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.doctors = []
        self.patients = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_doctor(self, name):
        for doctor in self.doctors:
            if doctor.name == name:
                return doctor
        return None

    def get_patient(self, name):
        for patient in self.patients:
            if patient.name == name:
                return patient
        return None

    def schedule_appointment(self, patient_name, date, time, specialty):
        patient = self.get_patient(patient_name)
        if patient:
            health_ai = HealthAI(self.doctors)
            appointment = health_ai.schedule_appointment(
                patient, date, time, specialty)
            if appointment:
                return appointment
            else:
                return "No doctors available for the requested specialty."
        else:
            return "Invalid patient name."

    def prescribe_medication(self, doctor_name, patient_name, medication, dosage, instructions):
        doctor = self.get_doctor(doctor_name)
        patient = self.get_patient(patient_name)
        if doctor and patient:
            health_ai = HealthAI(self.doctors)
            prescription = health_ai.prescribe_medication(
                doctor, patient, medication, dosage, instructions)
            return prescription
        else:
            return "Invalid doctor or patient name."


class Payment:
    def __init__(self, amount, payment_method, date):
        self.amount = amount
        self.payment_method = payment_method
        self.date = date

    def get_payment_details(self):
        return f"Payment Details:\nAmount: {self.amount}\nPayment Method: {self.payment_method}\nDate: {self.date}"

    """"""


Runs the main execution logic of the application.

This function serves as the entry point for the program. It executes the core functionality
required for the application, such as initiating the necessary resources, processing input,
performing calculations, and displaying output.

Parameters:
- None

Returns:
- None

Example:
    main()
""""""


def main():
    # Dummy data
    hospital = Hospital("ABC Hospital", "123 Main St, City")

    doctor1 = Doctor("Dr. John", "Cardiologist", "1234567890")
    doctor2 = Doctor("Dr. Sarah", "Dermatologist", "9876543210")
    doctor3 = Doctor("Dr. Mark", "Pediatrician", "6543210987")
    hospital.add_doctor(doctor1)
    hospital.add_doctor(doctor2)
    hospital.add_doctor(doctor3)

    patient = Patient("Laura", 30, "Female", "123 Main St, City", "555-1234")
    hospital.add_patient(patient)

    appointment = hospital.schedule_appointment(
        "Laura", datetime.date.today(), "10:00 AM", "Cardiology")
    if isinstance(appointment, str):
        print(appointment)
    else:
        print(appointment.get_appointment_details())

    prescription = hospital.prescribe_medication(
        "Dr. John", "Laura", "Medicine ABC", "1 tablet daily", "Take after meals."
    )
    if isinstance(prescription, str):
        print(prescription)
    else:
        print(prescription.get_prescription_details())

    payment = Payment(100, "Credit Card", datetime.date.today())
    print(payment.get_payment_details())


if __name__ == "__main__":
    main()

In this enhanced code, I have added a new class called "Payment" which represents a payment made for any medical services. The Payment class has attributes like amount, payment method, and date. It also has a method get_payment_details() which returns the details of the payment.

In the main() function, I have created a Payment object and printed its details using the get_payment_details() method.

This addition of the Payment class and its usage in the main() function adds a new real-world logic to the code, allowing for the handling of payments in a hospital setting.
