-- Create new user holberton_user and grant all privileges
-- Create a new db with a table with a single row, grant select privilege
-- Add replica user

CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,

	PRIMARY KEY(id)
);
INSERT INTO
nexus6(name)
VALUES
('Leon');
GRANT SELECT ON `tyrell_corp`.`nexus6` TO 'holberton_user'@'localhost';

CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'replica@mysql!pass';
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'replica_user'@'%' IDENTIFIED BY 'replica@mysql!pass';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
