/*
Database schema for car dealership
*/

--User table--
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    name  TEXT NOT NULL,
    mail TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL
);

--Cars table--
CREATE TABLE cars (
    car_id INTEGER PRIMARY KEY,
    car_brand TEXT NOT NULL,
    car_model TEXT NOT NULL,
    car_year INTEGER NOT NULL,
    car_mileage INTEGER NOT NULL,
    fuel_type TEXT NOT NULL,
    price  FLOAT NOT NULL,
    car_status BOOLEAN NOT NULL
);

--Reservations table--
CREATE TABLE reservations (
    reservation_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    car_id INTEGER NOT NULL,
    reservation_date DATE,
    status TEXT,

    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (car_id) REFERENCES cars(car_id)
);

