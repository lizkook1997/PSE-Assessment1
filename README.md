# Car Rental System

A command-line Car Rental System built using Python and PostgreSQL, applying object-oriented principles. It allows users to register, log in, view available cars, make bookings, and manage rentals. Admin users can manage car inventory and approve or reject bookings.

# How to Configure, Install & Run

1. Prerequisites
- Python 3.12+
- PostgreSQL (v13+ recommended)
- Install the PostgreSQL adapter for Python:
  ```bash
  pip install psycopg2

2. Setup Instructions
- Download or Clone the Repository
- git clone https://github.com/lizkook1997/PSE-Assessment1.git
  cd car-rental-system

3. Set Up the PostgreSQL Database**
- Download PostgreSQL: https://www.postgresql.org/download/
- Create the database:
- CREATE DATABASE car_rental_system;
- Update credentials in db/db_config.py

return psycopg2.connect(
    host="localhost",
    database="car_rental_system",

    user="your_username",
    password="your_password"
)

4. Run the schema:
- psql -U your_username -d car_rental_system -f db/schema.sql

NOTE `SQLite is not supported — this system is built for PostgreSQL.`

5. Run the Application
Project Structure

Start the main script: python main.py

car-rental-system/
|__db/
|   |-- db_config.py       # Connects to the pgAdmin 4 database
│   |--schema.sql          # SQL script to create the DB schema
|
|__models/
|   |-- booking.py         # Handles bookings, rental fee calculation
|   |-- car.py             # Manages car records (add, update, delete, list)
│   |-- user.py            # Handles user registration, login, and role management  
|
|__ main.py                # Entry point for the CLI application

`db/db_config.py`: Establishes a connection to the PostgreSQL database using the psycopg2 library.

`db/schema.sql`: SQL script that creates the database tables.

`models/booking.py`: Booking management and rental fee logic.

`models/car.py`: CRUD operations for car management.

`models/user.py`: Functions for user registration and login.

`main.py`: Handles user interaction through a command-line interface and coordinates actions between the user, car, and booking modules.



**License**
This project is licensed under the MIT License.
You are free to use, modify, and distribute it with appropriate credit.



**Known Bugs / Issues**

No email/SMS notification system implemented

Admin approval logic is basic and not linked to a GUI

No password encryption (not production-ready)

Data is not backed up automatically

**Credits**

Developer: Sonali Sharma
Course: Master of Software Engineering
Institute: Yoobee College of Creative Innovation
Assignment: MSE800 – Assessment 1
Date: 1 June 2025
