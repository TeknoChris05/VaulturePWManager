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
#mycursor.execute("CREATE TABLE Archive_Data_Password (data_id INT AUTO_INCREMENT PRIMARY KEY, AccountID INT NOT NULL, Username VARCHAR(100), Email VARCHAR(100), Password VARCHAR(60),FOREIGN KEY (AccountID) REFERENCES Account(AccountID))")
#mycursor.execute("CREATE TABLE Deleted_Passwords (data_id INT AUTO_INCREMENT PRIMARY KEY, AccountID INT NOT NULL, Username VARCHAR(100), Email VARCHAR(100), Password VARCHAR(60),FOREIGN KEY (AccountID) REFERENCES Account(AccountID))")
#mycursor.execute("CREATE TABLE Banking_Card (data_id INT AUTO_INCREMENT PRIMARY KEY, AccountID INT NOT NULL, Card_Title VARCHAR(100), Card_Number INT, Expire_Date VARCHAR(10), CVV INT, FOREIGN KEY (AccountID) REFERENCES Account(AccountID))")
#mycursor.execute("CREATE TABLE Network_Data (data_id INT AUTO_INCREMENT PRIMARY KEY, AccountID INT NOT NULL, Network_Title VARCHAR(100), Network VARCHAR(50), IP_Address VARCHAR(20), Password VARCHAR(50), FOREIGN KEY (AccountID) REFERENCES Account(AccountID))")
#mycursor.execute("CREATE TABLE Notes_Data (data_id INT AUTO_INCREMENT PRIMARY KEY, AccountID INT NOT NULL, Notes_title VARCHAR(50), Notes_body VARCHAR(200), FOREIGN KEY (AccountID) REFERENCES Account(AccountID))")
# mycursor.execute("SELECT * FROM Account")
#
# for x in mycursor:
#     print(x)










