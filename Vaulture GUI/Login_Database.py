import mysql.connector

# Connect to MySQL
login_database = mysql.connector.connect(
    host="db-mysql-nyc3-37387-do-user-15222509-0.l.db.ondigitalocean.com",
    user="doadmin",
    passwd='AVNS_AK8FErb1DuSyVpZeMZR',
    port='25060',
    database="Vaulturedb"
)

mycursor = login_database.cursor()

# Create tables with 2FA support
mycursor.execute("""
CREATE TABLE IF NOT EXISTS Account (
    AccountID INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Password VARCHAR(100) NOT NULL,
    TwoFA_Secret VARCHAR(64)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Account_Data_Password (
    data_id INT AUTO_INCREMENT PRIMARY KEY,
    AccountID INT NOT NULL,
    Title VARCHAR(100),
    Username VARCHAR(100),
    Email VARCHAR(100),
    Password VARCHAR(100),
    FOREIGN KEY (AccountID) REFERENCES Account(AccountID)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Archive_Data_Password (
    data_id INT AUTO_INCREMENT PRIMARY KEY,
    AccountID INT NOT NULL,
    Title VARCHAR(100),
    Username VARCHAR(100),
    Email VARCHAR(100),
    Password VARCHAR(100),
    FOREIGN KEY (AccountID) REFERENCES Account(AccountID)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Deleted_Passwords (
    data_id INT AUTO_INCREMENT PRIMARY KEY,
    AccountID INT NOT NULL,
    Title VARCHAR(100),
    Username VARCHAR(100),
    Email VARCHAR(100),
    Password VARCHAR(100),
    FOREIGN KEY (AccountID) REFERENCES Account(AccountID)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Banking_Card (
    data_id INT AUTO_INCREMENT PRIMARY KEY,
    AccountID INT NOT NULL,
    Card_Title VARCHAR(100),
    Card_Number VARCHAR(24),
    Expire_Date VARCHAR(10),
    CVV INT,
    FOREIGN KEY (AccountID) REFERENCES Account(AccountID)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Network_Data (
    data_id INT AUTO_INCREMENT PRIMARY KEY,
    AccountID INT NOT NULL,
    Network_Title VARCHAR(100),
    Network VARCHAR(50),
    IP_Address VARCHAR(20),
    Password VARCHAR(50),
    FOREIGN KEY (AccountID) REFERENCES Account(AccountID)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Notes_Data (
    data_id INT AUTO_INCREMENT PRIMARY KEY,
    AccountID INT NOT NULL,
    Notes_title VARCHAR(50),
    Notes_body VARCHAR(200),
    FOREIGN KEY (AccountID) REFERENCES Account(AccountID)
)
""")

login_database.commit()