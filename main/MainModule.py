import pyodbc
from dao.HospitalServiceImpl import HospitalServiceImpl
from entity.Patient import Patient
from entity.Doctor import Doctor
from entity.Appointment import Appointment
from exception.PatientNumberNotFoundException import PatientNumberNotFoundException
from exception.DoctorNotFoundException import DoctorNotFoundException
import datetime


class MainModule:
    def __init__(self):
        self.hospitalService = HospitalServiceImpl()

    def displayMenu(self):
        """
        Displays the main menu and prompts the user for an action.
        """
        while True:
            print("\n===== Hospital Management System Menu =====")
            print("1. Schedule an Appointment")
            print("2. Update an Appointment")
            print("3. Cancel an Appointment")
            print("4. View Appointment by ID")
            print("5. View Appointments for a Patient")
            print("6. View Appointments for a Doctor")
            print("7. Add a Patient")
            print("8. Add a Doctor")
            print("9. View All Patients")
            print("10. View All Doctors")
            print("11. View All Appointments")  # Add new option here
            print("12. Exit")
            choice = input("Please choose an option (1-12): ")

            if choice == '1':
                self.scheduleAppointment()
            elif choice == '2':
                self.updateAppointment()
            elif choice == '3':
                self.cancelAppointment()
            elif choice == '4':
                self.viewAppointmentById()
            elif choice == '5':
                self.viewAppointmentsForPatient()
            elif choice == '6':
                self.viewAppointmentsForDoctor()
            elif choice == '7':
                self.addPatient()
            elif choice == '8':
                self.addDoctor()
            elif choice == '9':
                self.viewAllPatients()
            elif choice == '10':
                self.viewAllDoctors()
            elif choice == '11':
                self.viewAllAppointments()  # Call the new function
            elif choice == '12':
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

    def viewAllAppointments(self):
            """
            Displays all appointments.
            """
            try:
                appointments = self.hospitalService.getAllAppointments()
                if appointments:
                    print("\nAll Appointments:")
                    for appointment in appointments:
                        print(appointment)
                else:
                    print("No appointments found.")
            except pyodbc.Error as e:
                print(f"Database error occurred: {e}")

    def viewAllPatients(self):
        """
        Displays all patients with their complete information.
        """
        try:
            patients = self.hospitalService.getAllPatients()
            if patients:
                print("\n===== All Patients =====")
                for patient in patients:
                    print(patient)
            else:
                print("No patients found.")
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")

    def viewAllDoctors(self):
        """
        Displays all doctors with their complete information.
        """
        try:
            doctors = self.hospitalService.getAllDoctors()
            if doctors:
                print("\n===== All Doctors =====")
                for doctor in doctors:
                    print(doctor)
            else:
                print("No doctors found.")
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")
    def addPatient(self):
        """
        Prompts the user for patient details and adds a new patient.
        """
        try:
            firstName = input("Enter First Name: ")
            lastName = input("Enter Last Name: ")
            dateOfBirthStr = input("Enter Date of Birth (YYYY-MM-DD): ")
            dateOfBirth = datetime.datetime.strptime(dateOfBirthStr, "%Y-%m-%d").date()
            gender = input("Enter Gender (M/F): ")
            contactNumber = input("Enter Contact Number: ")
            address = input("Enter Address: ")

            patient = Patient(firstName=firstName, lastName=lastName, dateOfBirth=dateOfBirth, gender=gender,
                              contactNumber=contactNumber, address=address)
            success = self.hospitalService.addPatient(patient)

            if success:
                print("Patient added successfully!")
            else:
                print("Failed to add the patient.")
        except ValueError:
            print("Invalid input format. Please try again.")
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")

    def addDoctor(self):
        """
        Prompts the user for doctor details and adds a new doctor.
        """
        try:
            firstName = input("Enter First Name: ")
            lastName = input("Enter Last Name: ")
            specialization = input("Enter Specialization: ")
            contactNumber = input("Enter Contact Number: ")

            # Create a Doctor object without doctorId
            doctor = Doctor(firstName=firstName, lastName=lastName, specialization=specialization,
                            contactNumber=contactNumber)
            success = self.hospitalService.addDoctor(doctor)

            if success:
                print("Doctor added successfully!")
            else:
                print("Failed to add the doctor.")
        except ValueError:
            print("Invalid input format. Please try again.")
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")

    def scheduleAppointment(self):
        """
        Prompts the user for details and schedules a new appointment.
        """
        try:
            patientId = int(input("Enter Patient ID: "))
            # Check if the patient exists before scheduling the appointment
            if not self.hospitalService.getPatientById(patientId):
                print(f"Patient with ID {patientId} does not exist.")
                return

            doctorId = int(input("Enter Doctor ID: "))
            # Check if the doctor exists before scheduling the appointment
            if not self.hospitalService.getDoctorById(doctorId):
                print(f"Doctor with ID {doctorId} does not exist.")
                return

            appointmentDateStr = input("Enter Appointment Date (YYYY-MM-DD HH:MM): ")
            appointmentDate = datetime.datetime.strptime(appointmentDateStr, "%Y-%m-%d %H:%M")
            description = input("Enter Appointment Description: ")

            appointment = Appointment(patientId=patientId, doctorId=doctorId, appointmentDate=appointmentDate,
                                      description=description)
            success = self.hospitalService.scheduleAppointment(appointment)

            if success:
                print("Appointment successfully scheduled!")
            else:
                print("Failed to schedule the appointment.")
        except ValueError:
            print("Invalid input format. Please try again.")
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")

    def updateAppointment(self):
        """
        Updates an existing appointment.
        """
        try:
            appointmentId = int(input("Enter Appointment ID to update: "))
            patientId = int(input("Enter new Patient ID: "))
            # Check if the patient exists before updating
            if not self.hospitalService.getPatientById(patientId):
                print(f"Patient with ID {patientId} does not exist.")
                return

            doctorId = int(input("Enter new Doctor ID: "))
            # Check if the doctor exists before updating
            if not self.hospitalService.getDoctorById(doctorId):
                print(f"Doctor with ID {doctorId} does not exist.")
                return

            appointmentDateStr = input("Enter new Appointment Date (YYYY-MM-DD HH:MM): ")
            appointmentDate = datetime.datetime.strptime(appointmentDateStr, "%Y-%m-%d %H:%M")
            description = input("Enter new Appointment Description: ")

            appointment = Appointment(appointmentId=appointmentId, patientId=patientId, doctorId=doctorId,
                                      appointmentDate=appointmentDate, description=description)
            success = self.hospitalService.updateAppointment(appointment)

            if success:
                print("Appointment updated successfully!")
            else:
                print("Failed to update the appointment.")
        except ValueError:
            print("Invalid input format. Please try again.")
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")

    def cancelAppointment(self):
        """
        Cancels an appointment by its ID.
        """
        try:
            appointmentId = int(input("Enter Appointment ID to cancel: "))
            success = self.hospitalService.cancelAppointment(appointmentId)

            if success:
                print("Appointment successfully canceled!")
            else:
                print("Failed to cancel the appointment.")
        except ValueError:
            print("Invalid input format. Please try again.")
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")

    def viewAppointmentById(self):
        """
        Displays an appointment by its ID.
        """
        try:
            appointmentId = int(input("Enter Appointment ID: "))
            appointment = self.hospitalService.getAppointmentById(appointmentId)

            if appointment:
                print(f"\nAppointment Details:\n{appointment}")
            else:
                print("Appointment not found.")
        except ValueError:
            print("Invalid input format. Please try again.")
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")

    def viewAppointmentsForPatient(self):
        """
        Displays all appointments for a specific patient.
        """
        try:
            patientId = int(input("Enter Patient ID: "))
            appointments = self.hospitalService.getAppointmentsForPatient(patientId)

            if appointments:
                print("\nAppointments for Patient:")
                for appointment in appointments:
                    print(appointment)
            else:
                print("No appointments found for this patient.")
        except PatientNumberNotFoundException:
            print(f"Patient with ID {patientId} not found.")
        except ValueError:
            print("Invalid input format. Please try again.")
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")

    def viewAppointmentsForDoctor(self):
        """
        Displays all appointments for a specific doctor.
        """
        try:
            doctorId = int(input("Enter Doctor ID: "))
            appointments = self.hospitalService.getAppointmentsForDoctor(doctorId)

            if appointments:
                print("\nAppointments for Doctor:")
                for appointment in appointments:
                    print(appointment)
            else:
                print("No appointments found for this doctor.")
        except ValueError:
            print("Invalid input format. Please try again.")
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")


if __name__ == "__main__":
    mainMenu = MainModule()
    mainMenu.displayMenu()
