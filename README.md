CLI Authentication & User Management System

A modular Python CLI-based authentication and user management system built using JSON storage and multi-file architecture.


Features

User Registration
- User Login Authentication
- Logout System
- Session Management
- Role-Based Permissions
- Admin Control Panel
- View All Users
- Delete Users
- Update User Password
- Search Users
- Login Retry Limit
- Validation System
- Logging System
- JSON File Persistence
- File Error Handling
- Infinite Runtime Menu Loop

Project Structure

project/
│
├── core/
│   ├── auth.py
│   ├── permissions.py
│   ├── session.py
│   └── user_manager.py
│
├── storage/
│   ├── loader.py
│   └── saver.py
│
├── utils/
│   ├── validators.py
│   ├── helpers.py
│   └── logger.py
│
├── interface/
│   ├── menu.py
│   └── messages.py
│
├── data/
│   └── users.json
│
├── main.py
├── .gitignore
└── README.md



Technologies Used

Python
JSON Storage
CLI (Command Line Interface)


Concepts Practiced

Modular Architecture
Authentication Systems
Session Handling
CRUD Operations
File Handling
Error Handling
Role-Based Access Control
Runtime Loops
Logging
Validation



Run The Project

python main.py


Future Improvements

Password Hashing
Database Integration
GUI Version
API Version
Session Expiration
Advanced Logging
User Activity Tracking
