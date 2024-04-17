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
    emp_name VARCHAR(30) NOT NULL,
    dept VARCHAR(20),
    salary INT,
    position VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS services (
    user_id VARCHAR(50) REFERENCES guest(user_ID),
    PaymentID INT REFERENCES payment(PaymentID),
    Service VARCHAR(20) NOT NULL,
    Service_date DATE NOT NULL,
    PRIMARY KEY (user_ID, PaymentID)
);

CREATE TABLE IF NOT EXISTS event (
    user_id VARCHAR(50) REFERENCES guest(user_ID),
    Payment_ID INT REFERENCES payment(PaymentID),
    Event_type VARCHAR(20) ,
    event_date DATE,
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

INSERT INTO employee VALUES (1, 'John Smith', 'Housekeeping', 30000, 'Housekeeper');
INSERT INTO employee VALUES (2, 'Emma Johnson', 'Front Desk', 35000, 'Receptionist');
INSERT INTO employee VALUES (3, 'Michael Brown', 'Housekeeping', 32000, 'Room Attendant');
INSERT INTO employee VALUES (4, 'Jennifer Lee', 'Front Desk', 38000, 'Front Desk Manager');
INSERT INTO employee VALUES (5, 'David Davis', 'Kitchen', 40000, 'Chef');
INSERT INTO employee VALUES (6, 'Emily Wilson', 'Kitchen', 35000, 'Cook');
INSERT INTO employee VALUES (8, 'James Anderson', 'Housekeeping', 31000, 'Laundry Attendant');
INSERT INTO employee VALUES (9, 'Jessica Martinez', 'Kitchen', 32000, 'Dishwasher');
INSERT INTO employee VALUES (11, 'Olivia Thompson', 'Housekeeping', 31000, 'Laundry Attendant');
INSERT INTO employee VALUES (12, 'William Garcia', 'Kitchen', 38000, 'Sous Chef');
INSERT INTO employee VALUES (13, 'Sophia Hernandez', 'Kitchen', 36000, 'Pastry Chef');
INSERT INTO employee VALUES (14, 'Alexander Allen', 'Massage', 40000, 'Massouse');
INSERT INTO employee VALUES (15, 'Victoria Hill', 'Massage ', 35000, 'Spa Manager');
INSERT INTO employee VALUES (16, 'Gabriel Green', 'Gym Trainer', 33000, 'Gym Trainer');
INSERT INTO employee VALUES (17, 'Natalie King', 'Gym Trainer', 30000, 'Gym Instructor');
INSERT INTO employee VALUES (18, 'Robert Wright', 'Housekeeping', 31000, 'Housekeeper');
INSERT INTO employee VALUES (19, 'Hannah Scott', 'Housekeeping', 32000, 'Housekeeper');
INSERT INTO employee VALUES (27, 'Samantha Lopez', 'Kitchen', 34000, 'Cook');
INSERT INTO employee VALUES (28, 'Mason Hill', 'Gym Trainer', 35000, 'Gym Trainer');
INSERT INTO employee VALUES (29, 'Ava Adams', 'Massage', 36000, 'Massouse');
INSERT INTO employee VALUES (30, 'Christopher Young', 'Sauna', 37000, 'Spa Receptionist');
INSERT INTO employee VALUES (31, 'Sophie Allen', 'Massage', 37000, 'Massouse');
INSERT INTO employee VALUES (32, 'Ella Martinez', 'Gym Trainer', 33000, 'Gym Trainer');
INSERT INTO employee VALUES (33, 'Jackson Rodriguez', 'Housekeeping', 32000, 'Housekeeper');
INSERT INTO employee VALUES (34, 'Leah Carter', 'Kitchen', 37000, 'Cook');
INSERT INTO employee VALUES (35, 'Lucas Parker', 'Suana', 36000, 'Spa Receptionist');
INSERT INTO employee VALUES (36, 'Madison Baker', 'Massage', 40000, 'Massouse');
INSERT INTO employee VALUES (37, 'Liam Morris', 'Massage', 35000, 'Massouse');
INSERT INTO employee VALUES (38, 'Zoe Perez', 'Gym Trainer', 33000, 'Gym Trainer');
INSERT INTO employee VALUES (39, 'Aiden Turner', 'Housekeeping', 31000, 'Laundry Attendant');


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
