-- prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant privleges on the databases hbnb_test_db and performance_schema
GRANT ALL ON hbnb_test_db.* to 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* to 'hbnb_test'@'localhost';
