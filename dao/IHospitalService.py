from abc import ABC, abstractmethod
from entity.Patient import Patient
from entity.Doctor import Doctor
from entity.Appointment import Appointment


class IHospitalService(ABC):
    """
    This interface defines the abstract methods that must be implemented
    by any service handling hospital operations, such as adding patients,
    scheduling appointments, retrieving records, etc.
    """

    @abstractmethod
    def addPatient(self, patient: Patient):
        """
        Adds a new patient to the database.
        """
        pass

    @abstractmethod
    def getPatientById(self, patientId: int):
        """
        Retrieves a patient by their ID.
        """
        pass

    @abstractmethod
    def scheduleAppointment(self, appointment: Appointment):
        """
        Schedules a new appointment.
        """
        pass

    @abstractmethod
    def addDoctor(self, doctor: Doctor):
        """
        Adds a new doctor to the database.
        """
        pass

    @abstractmethod
    def getDoctorById(self, doctorId: int):
        """
        Retrieves a doctor by their ID from the database.
        """
        pass

    @abstractmethod
    def updateAppointment(self, appointment: Appointment):
        """
        Updates an existing appointment.
        """
        pass

    @abstractmethod
    def cancelAppointment(self, appointmentId: int):
        """
        Cancels an appointment by its ID.
        """
        pass

    @abstractmethod
    def getAppointmentsForPatient(self, patientId: int):
        """
        Retrieves all appointments for a specific patient.
        """
        pass

    @abstractmethod
    def getAppointmentsForDoctor(self, doctorId: int):
        """
        Retrieves all appointments for a specific doctor.
        """
        pass

    @abstractmethod
    def getAppointmentById(self, appointmentId: int):
        """
        Retrieves an appointment by its ID.
        """
        pass

    @abstractmethod
    def getAllPatients(self):
        """
        Retrieves all patients from the database.
        """
        pass

    @abstractmethod
    def getAllDoctors(self):
        """
        Retrieves all doctors from the database.
        """
        pass

    @abstractmethod
    def getAllAppointments(self):
        """
        Retrieves all appointments from the database.
        """
        pass
