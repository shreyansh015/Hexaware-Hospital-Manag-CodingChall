

class Doctor:
    def __init__(self, firstName, lastName, specialization, contactNumber, doctorId=None):
        self.doctorId = doctorId  # Set the doctorId if provided
        self.firstName = firstName
        self.lastName = lastName
        self.specialization = specialization
        self.contactNumber = contactNumber

    def __repr__(self):
        return f"Doctor(ID={self.doctorId}, Name={self.firstName} {self.lastName}, Specialization={self.specialization}, Contact={self.contactNumber})"



