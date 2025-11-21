# Student-Administration-Database-System
**Overview**

This project is a simple desktop-based Student Administration System built using Python (Tkinter) for the GUI and MariaDB/MySQL for data storage.
It provides two modules:
Admin Module – add/manage student records, export data
Student Module – login and update profile information
The entire system runs locally using XAMPP for the database server.

**Features**

**Admin Panel**
Login authentication
Add new student records (Reg No, Name, Year, Department, Contact, etc.)
View all students
Export student data to CSV/Excel
Simple and clean Tkinter interface
**Student Panel**
Login using Registration Number and password
View their profile
Update allowed fields like name, contact, etc.

**Tech Stack**
Python 3.x
Tkinter (GUI)
MariaDB/MySQL (via XAMPP)
mysql-connector-python or PyMySQL
csv / pandas (for exporting)

**Database Setup**
Open phpMyAdmin.
Create a database named student_admin.
Create:
one table for admin credentials
one table for student information
Insert at least one admin account so you can log in to the Admin Panel.
Note: Use secure hashed passwords in real deployments.

**Security Notes**
Replace plain passwords with bcrypt / scrypt hashing
Use parameterized SQL queries to prevent SQL injection
Avoid placing database credentials directly in public code
Consider environment variables or config files for sensitive information

**Future Improvements**
Role-based access
Password reset system
Logging & reporting
Web-based version

