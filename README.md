# Hexaware-Hospital-Manag-CodingChall
This repository contains the coding challenges for Hospital Management Project.

Here are the steps How to run this project on your IDE
step1- First make a sql file inside MSSQL server name database as "HospitalDatabase" .for reference use sql file given in this project.
step2- Now download the raw file and extract the Project code .
step3- Connect the Project with Database using file DBConnection.py and Run the MainModule.py file in the terminal of IDE.
step4- you will get 11 options like following
 ===== Hospital Management System Menu =====
1. Schedule an Appointment
2. Update an Appointment
3. Cancel an Appointment
4. View Appointment by ID
5. View Appointments for a Patient
6. View Appointments for a Doctor
7. Add a Patient
8. Add a Doctor
9. View All Patients
10. View All Doctors
11. View All Appointments
12. Exit

1-6 options are the main Functionalities that we have to execute.
7-11 options are the Prerequisites of 1-6,

step5- use option 7 Add Patients.
Step6-use option 8 Add Doctors.
Step7- use option 9 to view all patients (to get patientid).
step8- use option 10 to view all doctors (to get doctorsid).

 ===== Now we can use option1 (Schedule Appointment) =====
step9- (Schedule Appointment) - use PatientId and use DoctorsId to schedule the appointment.

step10-use option 11 (View All Appointments) -to get the Appointmentid

 ===== Now we can use option2 (Update an Appointment) =====
step11- we can use AppointmentId to update the appointment that we can get from option11 View All Appointments

 ===== Now we can use option3 (Cancel an Appointment) =====
step12- we can use AppointmentId to cancel the appointment.

===== Now we can use option4 (View Appointment By Id) =====
step13- we can use AppointmentId to view the respective appointment information 

===== Now we can use option5 (View Appointment for Patient) =====
step14- we can use PatientId to view the respective appointments for that particular patient.

===== Now we can use option6 (View Appointment for Doctor) =====
step14- we can use DoctorId to view the respective appointments for that particular Doctor.


Now all the functions will run properly . 

