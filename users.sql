CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE if not exists admin (
    admin_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL
);


INSERT INTO admin (username, password_hash) VALUES('srishti','bangtan');
INSERT INTO admin (username, password_hash) VALUES('arav','qwerty');

CREATE TABLE IF NOT EXISTS guest (
    user_ID INT PRIMARY KEY,
    Aadhaar CHAR(12) NOT NULL,
    Name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS rooms (
    RoomNo INT PRIMARY KEY,
    Capacity INT,
    Cost INT,
    Type VARCHAR(5)
);

CREATE TABLE IF NOT EXISTS payment (
    PaymentID INT PRIMARY KEY,
    user_ID INT REFERENCES guest(user_ID),
    Dateofpayment DATE,
    amount INT
);

CREATE TABLE IF NOT EXISTS reservation (
    user_ID INT REFERENCES guest(user_ID),
    RoomNo INT REFERENCES rooms(RoomNo),
    PaymentID INT REFERENCES payment(PaymentID),
    date_from DATE,
    date_to DATE,
    PRIMARY KEY (user_ID, RoomNo, date_from)
);

CREATE TABLE IF NOT EXISTS employee (
    empID INT PRIMARY KEY,
    dept VARCHAR(20),
    salary INT,
    position VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS services (
    user_ID INT REFERENCES guest(user_ID),
    PaymentID INT REFERENCES payment(PaymentID),
    Service VARCHAR(20) NOT NULL CHECK (Service IN ('Massage', 'Sauna', 'Laundry', 'GymTrainer')),
    Service_date DATE NOT NULL,
    PRIMARY KEY (user_ID, PaymentID)
);

CREATE TABLE IF NOT EXISTS event (
    user_ID INT REFERENCES guest(user_ID),
    Payment_ID INT REFERENCES payment(PaymentID),
    Event_type VARCHAR(20),
    total_ppl INT
);
