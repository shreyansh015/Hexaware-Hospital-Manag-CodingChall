import pyodbc
from dao.IHospitalService import IHospitalService
from entity.Patient import Patient
from entity.Doctor import Doctor
from entity.Appointment import Appointment
from exception.PatientNumberNotFoundException import PatientNumberNotFoundException
from exception.DoctorNotFoundException import DoctorNotFoundException


class HospitalServiceImpl(IHospitalService):

    def getConnection(self):
        conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\\SQLEXPRESS;Database=HospitalDataBase;Trusted_Connection=yes;'
        return pyodbc.connect(conn_string)

    def addPatient(self, patient: Patient):
        """
        Adds a new patient to the database.
        """
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            query = "INSERT INTO Patient (firstName, lastName, dateOfBirth, gender, contactNumber, address) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (
            patient.firstName, patient.lastName, patient.dateOfBirth, patient.gender, patient.contactNumber,
            patient.address))
            conn.commit()
            return True
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def getPatientById(self, patientId: int):
        """
        Retrieves a patient by their ID.
        """
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            query = "SELECT * FROM Patient WHERE patientId = ?"
            cursor.execute(query, (patientId,))
            result = cursor.fetchone()
            if result:
                return Patient(patientId=result[0], firstName=result[1], lastName=result[2], dateOfBirth=result[3])
            else:
                return None
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")
            return None
        finally:
            cursor.close()
            conn.close()

    def scheduleAppointment(self, appointment: Appointment):
        """
        Schedules a new appointment.
        """
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            query = "INSERT INTO Appointment (patientId, doctorId, appointmentDate, description) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (appointment.patientId, appointment.doctorId, appointment.appointmentDate, appointment.description))
            conn.commit()
            return True
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def addDoctor(self, doctor: Doctor):
        """
        Adds a new doctor to the database.
        """
        try:
            conn = self.getConnection()
            cursor = conn.cursor()

            # Exclude doctorId as it is an identity column
            query = "INSERT INTO Doctor (firstName, lastName, specialization, contactNumber) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (doctor.firstName, doctor.lastName, doctor.specialization, doctor.contactNumber))

            conn.commit()
            return True
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def getDoctorById(self, doctorId: int):
        """
        Retrieves a doctor by their ID from the database.
        """
        try:
            conn = self.getConnection()  # Get the connection
            cursor = conn.cursor()
            query = "SELECT doctorId, firstName, lastName, specialization, contactNumber FROM Doctor WHERE doctorId = ?"
            cursor.execute(query, (doctorId,))
            result = cursor.fetchone()

            if result:
                return Doctor(doctorId=result[0], firstName=result[1], lastName=result[2], specialization=result[3],
                              contactNumber=result[4])
            else:
                return None  # Or raise an exception if doctor not found
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")
            return None
        finally:
            cursor.close()
            conn.close()

    def updateAppointment(self, appointment: Appointment):
        """
        Updates an existing appointment.
        """
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            query = "UPDATE Appointment SET patientId = ?, doctorId = ?, appointmentDate = ?, description = ? WHERE appointmentId = ?"
            cursor.execute(query, (appointment.patientId, appointment.doctorId, appointment.appointmentDate, appointment.description, appointment.appointmentId))
            conn.commit()
            return True
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def cancelAppointment(self, appointmentId: int):
        """
        Cancels an appointment by its ID.
        """
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            query = "DELETE FROM Appointment WHERE appointmentId = ?"
            cursor.execute(query, (appointmentId,))
            conn.commit()
            return True
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def getAppointmentsForPatient(self, patientId: int):
        """
        Retrieves all appointments for a specific patient.
        """
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            query = "SELECT * FROM Appointment WHERE patientId = ?"
            cursor.execute(query, (patientId,))
            results = cursor.fetchall()
            return [Appointment(appointmentId=row[0], patientId=row[1], doctorId=row[2], appointmentDate=row[3], description=row[4]) for row in results]
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    def getAppointmentsForDoctor(self, doctorId: int):
        """
        Retrieves all appointments for a specific doctor.
        """
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            query = "SELECT * FROM Appointment WHERE doctorId = ?"
            cursor.execute(query, (doctorId,))
            results = cursor.fetchall()
            return [Appointment(appointmentId=row[0], patientId=row[1], doctorId=row[2], appointmentDate=row[3], description=row[4]) for row in results]
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    def getAppointmentById(self, appointmentId: int):
        """
        Retrieves an appointment by its ID.
        """
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            query = "SELECT * FROM Appointment WHERE appointmentId = ?"
            cursor.execute(query, (appointmentId,))
            result = cursor.fetchone()
            if result:
                return Appointment(appointmentId=result[0], patientId=result[1], doctorId=result[2], appointmentDate=result[3], description=result[4])
            else:
                return None
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")
            return None
        finally:
            cursor.close()
            conn.close()

    def getAllPatients(self):
        """
        Retrieves all patients from the database.
        """
        global conn, cursor
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            query = "SELECT patientId, firstName, lastName, dateOfBirth, gender, contactNumber, address FROM Patient"
            cursor.execute(query)
            result = cursor.fetchall()

            patients = []
            for row in result:
                patient = Patient(patientId=row[0], firstName=row[1], lastName=row[2], dateOfBirth=row[3],
                                  gender=row[4], contactNumber=row[5], address=row[6])
                patients.append(patient)
            return patients
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    def getAllDoctors(self):
        """
        Retrieves all doctors from the database.
        """
        global cursor, conn
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            query = "SELECT doctorId, firstName, lastName, specialization, contactNumber FROM Doctor"
            cursor.execute(query)
            result = cursor.fetchall()

            doctors = []
            for row in result:
                doctor = Doctor(doctorId=row[0], firstName=row[1], lastName=row[2], specialization=row[3],
                                contactNumber=row[4])
                doctors.append(doctor)
            return doctors
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    def getAllAppointments(self):
        """
        Retrieves all appointments from the database.
        """
        global cursor, conn
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            query = "SELECT appointmentId, patientId, doctorId, appointmentDate, description FROM Appointment"
            cursor.execute(query)
            results = cursor.fetchall()

            appointments = []
            for result in results:
                appointment = Appointment(appointmentId=result[0], patientId=result[1], doctorId=result[2],
                                          appointmentDate=result[3], description=result[4])
                appointments.append(appointment)
            return appointments
        except pyodbc.Error as e:
            print(f"Database error occurred: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
