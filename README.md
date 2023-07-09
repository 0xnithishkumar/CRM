# Django CRUD Project
Welcome to the Django CRUD project repository! This project is a simple web application built using the Django framework, offering CRUD (Create, Read, Update, Delete) functionality for managing records.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)

### Introduction
This Django CRUD project was developed as part of my learning journey in web development. It allows users to register, log in, create new records, view record details, update existing records, and even delete them. The project demonstrates the fundamentals of Django and provides a solid foundation for building similar applications.

### Features
+ User registration and authentication system
+ Create new records with customizable fields
+ View details of individual records
+ Update existing records
+ Delete records

### Installation
To run this project locally, please follow these steps:
1. Clone this repository to your local machine using the following command: `git clone https://github.com/0xnithishkumar/CRM.git`
2. Navigate to the project directory: `cd CRM`
3. Create a virtual environment to isolate project dependencies: `python3 -m venv env`
4. Activate the virtual environment:
   + For macOS/Linux: `source env/bin/activate`
   + For Windows: `env\Scripts\activate`
5. Install the project dependencies: `pip install -r requirements.txt`
6. Perform database migrations: `python manage.py migrate`
7. Start the local development server: `python manage.py runserver`
8. Open your web browser and visit `http://localhost:8000` to access the application.

## Usage

Once the project is up and running, you can explore and interact with the application through the following steps:

1. Register a new user account by providing the required information.
2. Login using your registered credentials.
3. From the dashboard, you can navigate to the "Records" section.
4. Create a new record by clicking the "Add Record" button and filling in the necessary details.
5. View the list of existing records and click on a record to view its details.
6. Edit the record by clicking the "Edit" button and updating the fields as desired.
7. Delete a record by clicking the "Delete" button on the record details page.

If you prefer to access the deployed version of the project, you can visit [https://django-crm-zk46.onrender.com/](https://django-crm-zk46.onrender.com/).

Feel free to customize and enhance the project to suit your specific needs!
