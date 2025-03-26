import string

import mysql.connector
import customtkinter


login_database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='Mufeed2004-',
    database= "Login_information"
)

mycursor = login_database.cursor()

#mycursor.execute("CREATE TABLE Account (Username VARCHAR(100), Email VARCHAR(100), Password VARCHAR(100), AccountID int PRIMARY KEY AUTO_INCREMENT)")
mycursor.execute("SELECT * FROM Account")

for x in mycursor:
    print(x)

