# University Management System (UMS)

A web-based University Management System for managing students, faculty, courses, departments, and academic records.

# Project Description

A simple Python + Streamlit application that demonstrates Python OOP concepts through a University Management System. It allows users to create colleges, add students and teachers, and display records associated with each college.

# Features

- Create a college.
- Add students to a selected college.
- Add teachers to a selected college.
- Display students and teachers by college.
- Display the list of colleges.

# Technologies

Python
Streamlit
Installation
Install the required dependency:
pip install -r requirements.txt Or install Streamlit directly: pip install streamlit

# Run the Application

From the project directory, run:
streamlit run main.py
Alternatively:
python -m streamlit run main.py

To stop the local Streamlit server in PowerShell, press Ctrl + C.

# Data Storage

College, student, and teacher records are stored in st.session_state for the current session. 
This version does not use a database, so records are not permanently saved.

# Project Files

UMS/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore