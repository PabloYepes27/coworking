-- create BD "pruebaceiba" for development
CREATE DATABASE IF NOT EXISTS coworking_dev;

-- create a new user with full privileges on localhost
CREATE USER IF NOT EXISTS 'ceiba'@'localhost' IDENTIFIED BY 'ceiba';
GRANT ALL PRIVILEGES ON coworking_dev.* TO 'ceiba'@'localhost';

-- using databa base
USE coworking_dev;

-- delete all the records for no duplicate it 
DROP TABLE IF EXISTS spaces;

-- Create table in the MySQL
CREATE TABLE IF NOT EXISTS spaces (
    `space_id` INT(20) PRIMARY KEY AUTO_INCREMENT,
    `total_value` INT(8) NOT NULL,
    `payed_value` INT(8) NOT NULL,
    `status` BOOLEAN NOT NULL DEFAULT FALSE,
    `date_in` DATE NOT NULL,
    `date_out` DATE NOT NULL
);

-- Populate table as a Cafe Owner for creating the spaces
INSERT INTO spaces (total_value, payed_value, status, date_in, date_out) VALUES (350000, 0, FALSE, CURDATE(), CURDATE());
INSERT INTO spaces (total_value, payed_value, status, date_in, date_out) VALUES (400000, 0, FALSE, CURDATE(), CURDATE());
INSERT INTO spaces (total_value, payed_value, status, date_in, date_out) VALUES (270000, 0, FALSE, CURDATE(), CURDATE());
INSERT INTO spaces (total_value, payed_value, status, date_in, date_out) VALUES (550000, 0, FALSE, CURDATE(), CURDATE());
INSERT INTO spaces (total_value, payed_value, status, date_in, date_out) VALUES (700000, 0, FALSE, CURDATE(), CURDATE());
INSERT INTO spaces (total_value, payed_value, status, date_in, date_out) VALUES (420000, 0, FALSE, CURDATE(), CURDATE());
INSERT INTO spaces (total_value, payed_value, status, date_in, date_out) VALUES (370000, 0, FALSE, CURDATE(), CURDATE());



-- create BD "pruebaceiba" for test
CREATE DATABASE IF NOT EXISTS coworking_test;

-- create a new user with full privileges on localhost
CREATE USER IF NOT EXISTS 'ceiba'@'localhost' IDENTIFIED BY 'ceiba';
GRANT ALL PRIVILEGES ON coworking_test.* TO 'ceiba'@'localhost';

-- using databa base
USE coworking_test;

-- Create table in the MySQL
CREATE TABLE IF NOT EXISTS spaces (
    `space_id` INT(20) PRIMARY KEY AUTO_INCREMENT,
    `total_value` INT(8) NOT NULL,
    `payed_value` INT(8) NOT NULL,
    `status` BOOLEAN NOT NULL DEFAULT FALSE,
    `date_in` DATE NOT NULL,
    `date_out` DATE NOT NULL
);
