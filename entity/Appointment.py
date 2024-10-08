

class Appointment:
    def __init__(self, appointmentId=None, patientId=None, doctorId=None, appointmentDate=None, description=None):
        self.appointmentId = appointmentId
        self.patientId = patientId
        self.doctorId = doctorId
        self.appointmentDate = appointmentDate
        self.description = description

    def __str__(self):
        return f"Appointment({self.appointmentId}, {self.patientId}, {self.doctorId}, {self.appointmentDate}, {self.description})"


