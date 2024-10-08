class DoctorNotFoundException(Exception):
    def __init__(self, message="Doctor not found"):
        self.message = message
        super().__init__(self.message)
