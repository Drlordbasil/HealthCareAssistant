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


class HospitalManagement:
    def __init__(self, name, address):
        self.hospital = Hospital(name, address)
        self.health_ai = HealthAI(self.hospital.doctors)

    def add_doctor(self, name, specialty, contact):
        doctor = Doctor(name, specialty, contact)
        self.hospital.add_doctor(doctor)

    def add_patient(self, name, age, gender, address, contact):
        patient = Patient(name, age, gender, address, contact)
        self.hospital.add_patient(patient)

    def schedule_appointment(self, patient_name, date, time, specialty):
        return self.hospital.schedule_appointment(patient_name, date, time, specialty)

    def prescribe_medication(self, doctor_name, patient_name, medication, dosage, instructions):
        return self.hospital.prescribe_medication(
            doctor_name, patient_name, medication, dosage, instructions
        )

    def make_payment(self, amount, payment_method):
        date = datetime.date.today()
        payment = Payment(amount, payment_method, date)
        return payment.get_payment_details()

    def run(self):
        doctor1 = Doctor("Dr. John", "Cardiologist", "1234567890")
        doctor2 = Doctor("Dr. Sarah", "Dermatologist", "9876543210")
        doctor3 = Doctor("Dr. Mark", "Pediatrician", "6543210987")
        self.hospital.add_doctor(doctor1)
        self.hospital.add_doctor(doctor2)
        self.hospital.add_doctor(doctor3)

        patient = Patient("Laura", 30, "Female",
                          "123 Main St, City", "555-1234")
        self.hospital.add_patient(patient)

        appointment = self.schedule_appointment(
            "Laura", datetime.date.today(), "10:00 AM", "Cardiology"
        )
        if isinstance(appointment, str):
            print(appointment)
        else:
            print(appointment.get_appointment_details())

        prescription = self.prescribe_medication(
            "Dr. John",
            "Laura",
            "Medicine ABC",
            "1 tablet daily",
            "Take after meals.",
        )
        if isinstance(prescription, str):
            print(prescription)
        else:
            print(prescription.get_prescription_details())

        payment = self.make_payment(100, "Credit Card")
        print(payment)


if __name__ == "__main__":
    hospital_management = HospitalManagement(
        "ABC Hospital", "123 Main St, City")
    hospital_management.run()

# In this enhanced code, I have added a new class called "HospitalManagement" which represents the management of a hospital. This class encapsulates the functionalities of adding doctors, patients, scheduling appointments, prescribing medications, and making payments.

# The HospitalManagement class acts as a cohesive class that integrates the existing classes (Hospital, HealthAI) and provides a more streamlined interface for interacting with the hospital system.

# The main logic of the program has been moved into the HospitalManagement class, which is instantiated and run in the if __name__ == "__main__" block.

# The main() function has been removed and its functionality has been integrated into the run() method of the HospitalManagement class.

# This enhancement improves the code structure and readability, as well as makes it more extensible and maintainable.
