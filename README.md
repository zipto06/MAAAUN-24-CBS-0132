# Health-Clinic Queue Manager App

## Overview
The Health-Clinic Queue Manager is a Flask web application that helps healthcare clinics manage patient queues efficiently. It allows patients to register, view the current waiting list, and track the total number of patients seen today using a First-In-First-Out (FIFO) queue system.

## Features
- **Patient Registration**: Register new patients with their name and age
- **Real-time Queue Management**: View the current waiting list in order (FIFO)
- **Patient Counter**: Track the total number of patients seen today
- **Timestamped Records**: Automatic timestamps for patient registration using Python's datetime module

## Technology Stack
- **Backend**: Python, Flask
- **Data Structures**: Queue (FIFO) for managing patient order
- **Frontend**: HTML5, Jinja2 templates
- **Object-Oriented Programming**: Patient and Queue classes

## How to Run the App Locally (Beginner-Friendly Instructions)

### Step 1: Install Python
Make sure you have Python installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Clone the Repository
Open your terminal/command prompt and run:
```bash
git clone https://github.com/zipto06/MAAAUN-24-CBS-0132.git
cd MAAAUN-24-CBS-0132
```

### Step 3: Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
```

Then activate it:
- **Windows**: `venv\Scripts\activate`
- **Mac/Linux**: `source venv/bin/activate`

### Step 4: Install Flask
```bash
pip install Flask
```

### Step 5: Run the Application
```bash
python app.py
```

### Step 6: Open in Your Browser
Open your web browser and go to:
```
http://localhost:5000
```

You should now see the Health-Clinic Queue Manager homepage!

## Application Structure
- `app.py` - Main Flask application with routes
- `models.py` - Patient and Queue classes (OOP implementation)
- `templates/` - HTML templates for the web interface
  - `index.html` - Home page
  - `register.html` - Patient registration form
  - `waiting_list.html` - View current waiting list

## Requirements Met
✓ Object-Oriented Programming: Patient class with attributes and methods
✓ Data Structures: Queue (FIFO) implementation for patient management
✓ APIs: Uses Python's datetime module for timestamping
✓ Flask Implementation: Two functional routes (register and waiting_list)
✓ Version Control: Multiple commits with clear descriptions
✓ Documentation: This README explains what the app does and how to run it

## Author
Created for COS 202 Assignment 4 - Building for the Web with Flask