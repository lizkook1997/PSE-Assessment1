# Car Rental System

A command-line Car Rental System built with Python and PostgreSQL, applying object-oriented principles. Users can register, log in, view available cars, make bookings, and manage rentals. Admins can manage car inventory and approve or reject bookings.

## How to Configure, Install & Run

### 1. Prerequisites

- Python 3.12+
- PostgreSQL (v13+ recommended)
- PostgreSQL adapter for Python:
  ```bash
  pip install psycopg2
  ```

### 2. Setup Instructions

- Download or clone the repository:
  ```bash
  git clone https://github.com/lizkook1997/PSE-Assessment1.git
  cd car-rental-system
  ```

### 3. Set Up the PostgreSQL Database

- Download PostgreSQL: [https://www.postgresql.org/download/](https://www.postgresql.org/download/)
- Create the database:
  ```sql
  CREATE DATABASE car_rental_system;
  ```
- Update credentials in `db/db_config.py`:
  ```python
  return psycopg2.connect(
      host="localhost",
      database="car_rental_system",
      user="your_username",
      password="your_password"
  )
  ```

### 4. Run the Schema

- Execute the schema SQL:
  ```bash
  psql -U your_username -d car_rental_system -f db/schema.sql
  ```

> **Note:** SQLite is not supported — this system is built for PostgreSQL.

### 5. Run the Application

Start the main script:
```bash
python main.py
```

## Project Structure

```
car-rental-system/
├── db/
│   ├── db_config.py       # PostgreSQL connection config
│   └── schema.sql         # Database schema
├── models/
│   ├── booking.py         # Booking logic and rental fee calculation
│   ├── car.py             # Car CRUD operations
│   └── user.py            # User registration, login, and roles
└── main.py                # CLI entry point
```

- `db/db_config.py`: Connects to PostgreSQL using psycopg2.
- `db/schema.sql`: Creates the database tables.
- `models/booking.py`: Booking management and rental fee logic.
- `models/car.py`: Car management (add, update, delete, list).
- `models/user.py`: User registration and login.
- `main.py`: Command-line interface and coordination.

## License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute it with appropriate credit.

## Known Bugs / Issues

- No email/SMS notification system implemented
- Admin approval logic is basic and not linked to a GUI
- No password encryption (not production-ready)
- Data is not backed up automatically

## Credits

- **Developer:** Sonali Sharma
- **Course:** Master of Software Engineering
- **Institute:** Yoobee College of Creative Innovation
- **Assignment:** MSE800 – Assessment 1
- **Date:** 1 June 2025
