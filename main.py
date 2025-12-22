import os
os.system("cls")

# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
# )
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='dars_data'
)

cursor = mydb.cursor()
# query = """SELECT * FROM people 
#             WHERE FirstName LIKE 'A%';
#         """

# first = input("Ism:")
# last = input("Familya:")
# gen = input("Jins:")
# email = input("Email:")
# phone = input("Phone:")
# birth = input("Birth day: ")
# job = input("Job: ")
# add = input("Address: ")
# query = f"""INSERT INTO people ( FirstName, LastName, Gender, Email, Phone, BirthDay, JobTitle, Address)
#             VALUES
#             ('{first}', '{last}', '{gen}', '{email}', '{phone}', '{birth}', '{job}', '{add}');
#         """
# cursor.execute(query)
# mydb.commit()










query = """
    UPDATE people SET `Index` = 102, Address='Qashqadaryo'
    WHERE FirstName = 'Bekzod'; 
"""
cursor.execute(query)
mydb.commit()

print(cursor.rowcount, "ta qator o'zgardi!")
















# app = QApplication([])
# app.exec_()