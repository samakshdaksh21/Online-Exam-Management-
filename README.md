# 🧑‍🎓 Online Exam Management System

This is a simple **command-line based Python project** for managing an online exam system. It allows you to manage student records, subject details, and exam information using a MySQL database.

## 📁 Features

- **Student Management**
  - Search Student Records
  - Delete Student Records
  - Update Student Records

- **Subject Management**
  - Search Subject Records
  - Delete Subject Records
  - Update Subject Records

- **Exam Management**
  - View Exam Details
  - Delete Exam Records

## 🛠️ Tech Stack

- **Python** (Core logic and CLI)
- **MySQL** (Database backend)
- **mysql-connector-python** (for DB connection)

## 🗂️ File Structure

- `management.py`: Entry point for the application with main menu logic.
- `mlib.py`: Contains menu handling functions for students, subjects, and exams.
- `student.py`: Functions for CRUD operations on student data.
- `exam.py`: Functions for CRUD operations on exam data.
- `subject.py`: (Not included, but should contain subject-related logic.)

## 💾 Setup Instructions

1. **Install Requirements**
   ```bash
   pip install mysql-connector-python
