CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(50) PRIMARY KEY,
    password_hash VARCHAR(128) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE if NOT EXISTS admin (
    admin_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS guest (
    user_id VARCHAR(50) REFERENCES users(user_id),
    Aadhaar CHAR(12) NOT NULL,
    Name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS rooms (
    RoomNo INT PRIMARY KEY,
    Capacity INT,
    Cost INT,
    Type VARCHAR(10),
    Occupied BOOLEAN DEFAULT 0
);

CREATE TABLE IF NOT EXISTS payment (
    PaymentID INT PRIMARY KEY,
    user_id VARCHAR(50) REFERENCES guest(user_id),
    Dateofpayment DATE,
    amount INT
);

CREATE TABLE IF NOT EXISTS reservation (
    user_id VARCHAR(50) REFERENCES guest(user_ID),
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
    user_id VARCHAR(50) REFERENCES guest(user_ID),
    PaymentID INT REFERENCES payment(PaymentID),
    Service VARCHAR(20) NOT NULL CHECK (Service IN ('Massage', 'Sauna', 'Laundry', 'GymTrainer')),
    Service_date DATE NOT NULL,
    PRIMARY KEY (user_ID, PaymentID)
);

CREATE TABLE IF NOT EXISTS event (
    user_id VARCHAR(50) REFERENCES guest(user_ID),
    Payment_ID INT REFERENCES payment(PaymentID),
    Event_type VARCHAR(20)  CHECK(Event_type IN('Board Room', 'Banquet Hall')),
    total_ppl INT,
    Booked BOOLEAN DEFAULT 0
);

create table if not exists old_reservation(
    user_id VARCHAR(50) REFERENCES guest(user_ID),
    RoomNo int,
    PaymentID INT REFERENCES Payment(PaymentID),
    date_from date,
    date_to date,
    primary key(user_ID,RoomNo,date_from));

DELIMITER $$
CREATE TRIGGER ins_sum
BEFORE DELETE ON reservation FOR EACH ROW
BEGIN
    INSERT INTO old_reservation(user_id, RoomNo, PaymentID, date_from, date_to)
    VALUES (OLD.user_ID, OLD.RoomNo, OLD.PaymentID, OLD.date_from, OLD.date_to);
END$$
DELIMITER ;


INSERT INTO admin (username, password_hash) VALUES('srishti','bangtan');
INSERT INTO admin (username, password_hash) VALUES('arav','qwerty');


-- Floor 1
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (101, 4, 8000, 'Suite');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (102, 2, 2000, 'Double');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (103, 2, 4000, 'Double');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (104, 1, 3000, 'Single');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (105, 1, 3000, 'Single');

-- Floor 2
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (201, 1, 3000, 'Single');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (202, 4, 8000, 'Suite');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (203, 2, 4000, 'Double');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (204, 2, 4000, 'Double');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (205, 1, 3000, 'Single');

-- Floor 3
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (301, 1, 3000, 'Single');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (302, 1, 3000, 'Single');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (303, 4, 8000, 'Suite');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (304, 2, 4000, 'Double');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (305, 2, 4000, 'Double');

-- Floor 4
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (401, 2, 4000, 'Double');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (402, 1, 3000, 'Single');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (403, 1, 3000, 'Single');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (404, 4, 8000, 'Suite');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (405, 2, 4000, 'Double');

-- Floor 5
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (501, 1, 3000, 'Single');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (502, 2, 4000, 'Double');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (503, 2, 4000, 'Double');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (504, 1, 3000, 'Single');
INSERT INTO rooms (RoomNo, Capacity, Cost, Type) VALUES (505, 4, 8000, 'Suite');


