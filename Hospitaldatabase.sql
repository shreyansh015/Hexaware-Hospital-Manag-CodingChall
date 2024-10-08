CREATE DATABASE HospitalDataBase;
GO

-- Use the HospitalDB database
USE HospitalDataBase;
GO

CREATE TABLE Patient (
    patientId INT PRIMARY KEY IDENTITY(1,1),
    firstName NVARCHAR(50) NOT NULL,
    lastName NVARCHAR(50) NOT NULL,
    dateOfBirth DATE NOT NULL,
    gender NVARCHAR(10) NOT NULL,
    contactNumber NVARCHAR(15) NOT NULL,
    address NVARCHAR(255)
);

CREATE TABLE Doctor (
    doctorId INT PRIMARY KEY IDENTITY(1,1),
    firstName NVARCHAR(50) NOT NULL,
    lastName NVARCHAR(50) NOT NULL,
    specialization NVARCHAR(100) NOT NULL,
    contactNumber NVARCHAR(15) NOT NULL
);

CREATE TABLE Appointment (
    appointmentId INT PRIMARY KEY IDENTITY(1,1),
    patientId INT NOT NULL,
    doctorId INT NOT NULL,
    appointmentDate DATETIME NOT NULL,
    description NVARCHAR(255),
    CONSTRAINT FK_Patient FOREIGN KEY (patientId) REFERENCES Patient(patientId),
    CONSTRAINT FK_Doctor FOREIGN KEY (doctorId) REFERENCES Doctor(doctorId)
);


SELECT * FROM Patient;
SELECT * FROM Doctor;
SELECT * FROM Appointment;

