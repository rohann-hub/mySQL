
✅ Requirements: 

Python installed (python --version)
MySQL server installed and running.
mysql-connector-python installed. You can install it using:

**  pip install mysql-connector-python  **


✅ MySQL Setup (Run these in MySQL):

CREATE DATABASE testdb;
USE testdb;
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);
