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
#mycursor.execute("CREATE TABLE Account_Data_Password (data_id INT AUTO_INCREMENT PRIMARY KEY, AccountID INT NOT NULL, Username VARCHAR(100), Email VARCHAR(100), Password VARCHAR(60),FOREIGN KEY (AccountID) REFERENCES Account(AccountID))")
# mycursor.execute("SELECT * FROM Account")
#
# for x in mycursor:
#     print(x)


