/*
Database schema for car dealership
*/
BEGIN TRANSACTION;

--User table--
CREATE TABLE  IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    firebase_uid TEXT UNIQUE NOT NULL,
    name  TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    role TEXT DEFAULT 'customer' NOT NULL
);

--Cars table--
CREATE TABLE IF NOT EXISTS cars (
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
CREATE TABLE IF NOT EXISTS reservations (
    reservation_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    car_id INTEGER NOT NULL,
    reservation_date DATE,
    reservation_status TEXT DEFAULT 'Pending' NOT NULL ,

    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (car_id) REFERENCES cars(car_id)
);

COMMIT;
