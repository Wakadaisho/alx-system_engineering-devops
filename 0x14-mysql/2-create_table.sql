-- Create new user holberton_user and grant all privileges
-- Create a new db with a table with a single row, grant select privilege

CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

CREATE DATABASE IF NOT EXISTS tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,

	PRIMARY KEY(id)
);
INSERT INTO
tyrell_corp(name)
VALUES
('Leon');
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
