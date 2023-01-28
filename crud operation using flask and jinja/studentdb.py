import sqlite3

con = sqlite3.connect("student.db")

con.execute("create table students(rollno INTEGER primary key, name text Not null, email text not null, clg text not null, fees Integer)")

con.close()