CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100),
    role VARCHAR(20) -- 'admin' or 'customer'
);

CREATE TABLE IF NOT EXISTS cars (
    id SERIAL PRIMARY KEY,
    make VARCHAR(100),
    model VARCHAR(100),
    year INT,
    mileage INT,
    available BOOLEAN DEFAULT TRUE,
    min_days INT,
    max_days INT
);

CREATE TABLE IF NOT EXISTS bookings (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    car_id INT REFERENCES cars(id),
    start_date DATE,
    end_date DATE,
    status VARCHAR(20) DEFAULT 'pending', -- 'pending', 'approved', 'rejected'
    total_amount NUMERIC
);
