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
    Aadhaar CHAR(12) UNIQUE NOT NULL,
    Name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS rooms (
    RoomNo INT PRIMARY KEY,
    Type VARCHAR(10),
    Occupied BOOLEAN DEFAULT 0
);

CREATE TABLE IF NOT EXISTS payment (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,
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


INSERT INTO admin (username, password_hash) VALUES('srishti','bangtan');
INSERT INTO admin (username, password_hash) VALUES('arav','qwerty');

-- Floor 1
INSERT INTO rooms (RoomNo, Type) VALUES (101, 'Suite');
INSERT INTO rooms (RoomNo, Type) VALUES (102, 'Double');
INSERT INTO rooms (RoomNo, Type) VALUES (103, 'Double');
INSERT INTO rooms (RoomNo, Type) VALUES (104, 'Single');
INSERT INTO rooms (RoomNo, Type) VALUES (105, 'Single');

-- Floor 2
INSERT INTO rooms (RoomNo, Type) VALUES (201, 'Single');
INSERT INTO rooms (RoomNo, Type) VALUES (202, 'Suite');
INSERT INTO rooms (RoomNo, Type) VALUES (203, 'Double');
INSERT INTO rooms (RoomNo, Type) VALUES (204, 'Double');
INSERT INTO rooms (RoomNo, Type) VALUES (205, 'Single');

-- Floor 3
INSERT INTO rooms (RoomNo, Type) VALUES (301, 'Single');
INSERT INTO rooms (RoomNo, Type) VALUES (302, 'Single');
INSERT INTO rooms (RoomNo, Type) VALUES (303, 'Suite');
INSERT INTO rooms (RoomNo, Type) VALUES (304, 'Double');
INSERT INTO rooms (RoomNo, Type) VALUES (305, 'Double');

-- Floor 4
INSERT INTO rooms (RoomNo, Type) VALUES (401, 'Double');
INSERT INTO rooms (RoomNo, Type) VALUES (402, 'Single');
INSERT INTO rooms (RoomNo, Type) VALUES (403, 'Single');
INSERT INTO rooms (RoomNo, Type) VALUES (404, 'Suite');
INSERT INTO rooms (RoomNo, Type) VALUES (405, 'Double');

-- Floor 5
INSERT INTO rooms (RoomNo, Type) VALUES (501, 'Single');
INSERT INTO rooms (RoomNo, Type) VALUES (502, 'Double');
INSERT INTO rooms (RoomNo, Type) VALUES (503, 'Double');
INSERT INTO rooms (RoomNo, Type) VALUES (504, 'Single');
INSERT INTO rooms (RoomNo, Type) VALUES (505, 'Suite');

delimiter $$
CREATE TRIGGER IF NOT EXISTS ins_sum
BEFORE DELETE ON reservation FOR EACH ROW
begin
    INSERT INTO old_reservation VALUES (OLD.user_ID, OLD.RoomNo, OLD.PaymentID, OLD.date_from, OLD.date_to);
end;
$$


DELIMITER $$

CREATE TRIGGER IF NOT EXISTS  trg_before_insert_services
BEFORE INSERT ON services FOR EACH ROW
BEGIN
    INSERT INTO payment (user_id, Dateofpayment, amount)
    VALUES (NEW.user_ID, NOW(), 0);
END$$
