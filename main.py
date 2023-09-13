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
        prescription = Prescription(doctor, patient, medication, dosage, instructions)
        return prescription


def main():
    # Dummy data
    doctors = [
        Doctor("Dr. John", "Cardiologist", "1234567890"),
        Doctor("Dr. Sarah", "Dermatologist", "9876543210"),
        Doctor("Dr. Mark", "Pediatrician", "6543210987")
    ]

    patient = Patient("Laura", 30, "Female", "123 Main St, City", "555-1234")

    health_ai = HealthAI(doctors)

    appointment = health_ai.schedule_appointment(patient, datetime.date.today(), "10:00 AM", "Cardiology")
    if appointment:
        print(appointment.get_appointment_details())
    else:
        print("No doctors available for the requested specialty.")

    prescription = health_ai.prescribe_medication(
        appointment.doctor, appointment.patient, "Medicine ABC", "1 tablet daily", "Take after meals."
    )
    print(prescription.get_prescription_details())


if __name__ == "__main__":
    main()