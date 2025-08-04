
#first install ** pip install mysql-connector-python **
# Second go to **  MYSQL workbench and setup new connection  **
# including ( create local host name , password , and root name (not mendatory ))

#/ ** create a Database in MYsql ** 

# CREATE DATABASE testdb; (your database name)
# USE testdb;
# CREATE TABLE students (
#     id INT PRIMARY KEY,
#     name VARCHAR(100)
# );



import mysql.connector

conn = mysql.connector.connect(
    host = "local host",
    user = "root name or username ",
    password ="your Mysql password",
    database ="Data base name"
)

cursor = conn.cursor()




n = int(input("How many students do you want to enter? "))

for _ in range(n):
    student_id = int(input("enter Student ID: "))
    student_name = input("Enter student name: ")


    try:
        cursor.execute("INSERT INTO students (id, name) VALUES (%s, %s)",(student_id , student_name))

        print("Data inserted Successfully!" )
    except mysql.connector.Error as err:
        print(f"Error: {err}")

conn.commit()
cursor.close()

conn.close()
