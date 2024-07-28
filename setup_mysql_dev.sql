-- prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant privleges on the databases hbnb_dev_db and performance_schema
GRANT ALL ON hbnb_dev_db.* to 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* to 'hbnb_dev'@'localhost';
