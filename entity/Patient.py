



class Patient:
    def __init__(self, patientId=None, firstName=None, lastName=None, dateOfBirth=None, gender=None, contactNumber=None, address=None):
        self.patientId = patientId
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.gender = gender
        self.contactNumber = contactNumber
        self.address = address

    def __str__(self):
        return f"Patient({self.patientId}, {self.firstName}, {self.lastName}, {self.dateOfBirth}, {self.gender}, {self.contactNumber}, {self.address})"


