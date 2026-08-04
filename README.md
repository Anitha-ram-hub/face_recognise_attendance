# face_recognise_attendance
ATTENDANCE SYSTEM BY FACE RECOGNITION USING RASPERRY PI
1. Introduction
The Face Recognition Attendance System is an automated attendance management solution that uses facial recognition technology to identify registered users and record their attendance. The system is built using a Raspberry Pi 3 Model B+, a Raspberry Pi Camera Module, and an LED flash to ensure clear image capture even in low-light environments.
When a registered user stands in front of the camera, the system detects the face, compares it with the stored database, and records the person's name along with the current date and in-time. If the face is not recognized, the attendance is not recorded.
________________________________________
2. Objectives
•	Automate attendance recording. 
•	Eliminate proxy attendance. 
•	Reduce manual work. 
•	Improve attendance accuracy. 
•	Record attendance with date and time.
3. Hardware Components
Components	Purpose
Raspberry Pi 3 Model B+	
Main processing unit

Raspberry Pi Camera Module	
Captures face images

MicroSD Card	
Stores operating system and project files

4. Software Requirements
Operating System
•	Raspberry Pi OS (64-bit or 32-bit) 
Programming Language
•	Python 3.11 (or the installed version) 
Development Environment
•	Thonny IDE / Visual Studio Code 
•	Terminal (for running Python scripts) 
Python Libraries
Library/Module	Purpose
OpenCV (cv2)	Captures images from the camera and performs face detection and image processing.
face_recognition	Generates face encodings and recognizes registered faces using dlib.
NumPy	Performs numerical operations and handles image data as arrays.
Pandas	Reads, writes, and manages attendance records in CSV format.
dlib	Provides the face detection and face encoding algorithms used by the face_recognition library.
6. System Workflow
The working process of the system consists of two phases:
Phase 1: User Registration
During registration, the user stands in front of the camera, and multiple face images are captured from different angles. These images are stored in the dataset folder. The face recognition library extracts unique facial features from these images and generates a face encoding, which is stored in the database for future recognition.
Phase 2: Attendance Recognition
After registration, the system continuously monitors the live camera feed. When a face is detected, the LED flash turns on briefly to improve image quality. The system extracts the facial features from the captured image and compares them with the stored face encodings.
If a match is found, the person's identity is confirmed, and the attendance is recorded with the current date and in-time. If the person has already been marked present for the day, the system ignores the duplicate entry. If no match is found, the face is classified as an unknown person.

7. System Flowchart
 


8. Working Principle
1.	The Raspberry Pi initializes the camera and loads all registered face encodings. 
2.	The camera continuously captures live video frames. 
3.	When a face is detected, the LED flash turns on to improve image quality. 
4.	The detected face is converted into a numerical face encoding. 
5.	The generated encoding is compared with the stored face database. 
6.	If the face matches a registered user, the system retrieves the user's name. 
7.	The attendance file is checked to avoid duplicate entries. 
8.	If attendance has not been recorded for the day, the system stores the user's name, current date, and in-time. 
9.	The LED flash turns off, and the system resumes monitoring. 
________________________________________
9. Attendance Database
Attendance is stored in a CSV file.
Name	Date	In-Time
John	04-08-2026	09:05:12
Priya	04-08-2026	09:18:45
________________________________________
