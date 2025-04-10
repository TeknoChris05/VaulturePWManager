from importlib.metadata import entry_points
import customtkinter
from PIL import Image
import tkinter
import acc2
import os
from customtkinter import CTkImage
from tkinter import filedialog
from PIL import Image, ImageTk
from pathlib import Path
import random
import string
import tkinter as tk
import mysql.connector
import sys

# AI GENERATED
# ********************************************************
account_id = sys.argv[1] if len(sys.argv) > 1 else None

if account_id:
    print(f"Logged in with Account ID: {account_id}")
else:
    print("Error: No account ID received!")
# ********************************************************

login_database = mysql.connector.connect(
    host="db-mysql-nyc3-37387-do-user-15222509-0.l.db.ondigitalocean.com",
    user="doadmin",
    passwd='AVNS_AK8FErb1DuSyVpZeMZR',
    port='25060',
    database="Vaulturedb"
)

mycursor = login_database.cursor()

window = customtkinter.CTk()
window.title("Vaulture")

# Screen width and height.
screen_dimension_width = window.winfo_screenwidth()
screen_dimension_height = window.winfo_screenheight()
window.geometry(f"{screen_dimension_width}x{screen_dimension_height}-10+0")
window.minsize(800, 600)
window.maxsize(1920, 1080)

# Sidebar
window.columnconfigure(0, weight=0)
# MainStuffC
window.columnconfigure(1, weight=2)
# MainstuffR
window.rowconfigure(1, weight=2)
# BottomBar
window.rowconfigure(3, weight=0)

# Main content frame
main_frame = customtkinter.CTkFrame(window, fg_color="#A9A9A9")
main_frame.grid(row=1, column=1, padx=0, pady=0, sticky="nsew")


#######################################################################################################################################
# AI -Assisted Code: Theme Color Update Feature - Marteno Romaya ,https://chatgpt.com/share/67f19bc3-4ab8-800a-bfaa-5ae77d2372a2
def load_saved_theme_color():
    try:
        with open("theme_settings.txt", "r") as file:
            saved_color = file.read().strip()
            if not saved_color or saved_color.lower() == "#2c2f33":
                return "#133f61"  # Force blue if empty or default gray
            return saved_color
    except FileNotFoundError:
        return "#133f61"  # Default if no file exists


saved_theme_color = load_saved_theme_color()
#######################################################################################################################################

# Left sidebar
sidebar = customtkinter.CTkFrame(window, width=200, corner_radius=20, fg_color=saved_theme_color, border_width=8, border_color="black")
sidebar.grid(row=0, column=0, rowspan=2, sticky="nsw")
sidebar.grid_forget()

# global sidebar
sidebar_open = False


def toggle_sidebar():
    global sidebar_open
    if sidebar_open:
        # Hide the sidebar
        sidebar.grid_forget()
    else:
        # Show the sidebar
        sidebar.grid(row=0, column=0, rowspan=3, sticky="nsw")
    sidebar_open = not sidebar_open


# White bottom bar
bottom_bar = customtkinter.CTkFrame(window, height=90, corner_radius=0, fg_color=saved_theme_color)
bottom_bar.grid(row=2, column=1, columnspan=2, sticky="ew")


#######################################################################################################################################
# AI -Assisted Code: Theme Color Update Feature - Marteno Romaya, https://chatgpt.com/share/67f19bc3-4ab8-800a-bfaa-5ae77d2372a2
def update_main_theme(new_color):
    # If the settings page is default gray, make sidebar and bottom_bar blue
    if new_color.lower() == "#2c2f33":
        actual_color = "#133f61"  # Vaulture default blue
    else:
        actual_color = new_color

    # Update sidebar and bottom bar color
    sidebar.configure(fg_color=actual_color)
    bottom_bar.configure(fg_color=actual_color)

    # Only update the Vaulture picture label and Storage Options label
    for widget in sidebar.winfo_children():
        if widget == vulture_label or widget == Title_Spot:
            widget.configure(fg_color=actual_color)

    for widget in bottom_bar.winfo_children():
        if isinstance(widget, customtkinter.CTkLabel):
            widget.configure(fg_color=actual_color)

    hamburger_button.configure(fg_color=actual_color)


#######################################################################################################################################

# Sidebar buttons (These will appear when the sidebar is toggled)
# Hamburger Icon
hamburger_button = customtkinter.CTkButton(main_frame, text="☰", width=60, height=60, corner_radius=10, fg_color="#0e3161", border_width=3, border_color="black", font=("Arial", 24),
                                           command=lambda: toggle_sidebar())
hamburger_button.grid(row=0, column=0, padx=20, pady=30)
hamburger_button.configure(fg_color=saved_theme_color)

Title_Spot = customtkinter.CTkLabel(sidebar, text="Storage Options", text_color="White", font=("Segoe UI", 28, "bold"),
                                    height=60)
Title_Spot.grid(row=0, column=0, padx=30, pady=10, sticky="nsew")

Passwords_button = customtkinter.CTkButton(sidebar, text="Passwords🔒", width=150, height=20, corner_radius=5, fg_color="#282929", border_width=3, border_color="#bbbdbf", command=lambda: open_passwordMaker_page())
Passwords_button.grid(row=1, column=0, padx=30, pady=10, sticky="nsew")

Notes_button = customtkinter.CTkButton(sidebar, text="Notes📝", width=150, height=20, corner_radius=5, fg_color="#282929", border_width=3, border_color="#bbbdbf", command=lambda: open_notes_page())
Notes_button.grid(row=2, column=0, padx=30, pady=10, sticky="nsew")

Banking_button = customtkinter.CTkButton(sidebar, text="Banking Cards💳", width=150, height=20, corner_radius=5,fg_color="#282929", border_width=3, border_color="#bbbdbf", command=lambda: open_banking_cards_page())
Banking_button.grid(row=3, column=0, padx=30, pady=10, sticky="nsew")

Network_button = customtkinter.CTkButton(sidebar, text="Network 🛜", width=150, height=20, corner_radius=5, fg_color="#282929", border_width=3, border_color="#bbbdbf", command=lambda: open_Network_page())
Network_button.grid(row=4, column=0, padx=30, pady=20, sticky="nsew")

script_dir = Path(__file__).parent
project_root = script_dir.parent
image_path = project_root / "images" / "Vaulture.png"
vulture_image = customtkinter.CTkImage(Image.open(image_path), size=(200, 200))
vulture_label = customtkinter.CTkLabel(sidebar, text="", image=vulture_image)
vulture_label.grid(row=5, column=0, padx=30, sticky="nsew")

# Assigning weights so that these buttons wont go offscreen
# Hamburger Button
sidebar.rowconfigure(0, weight=2)
# Passwords
sidebar.rowconfigure(1, weight=2)
# Notes
sidebar.rowconfigure(2, weight=2)
# Banking Card
sidebar.rowconfigure(3, weight=2)
# One-Time Passwords
sidebar.rowconfigure(4, weight=2)
# Archived
sidebar.rowconfigure(5, weight=2)
# Trash
sidebar.rowconfigure(6, weight=2)

# Bottom bar buttons
ValtureP_button = customtkinter.CTkButton(bottom_bar, text="Home 🏠", width=60, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray", command=lambda: go_to_home_page())
ValtureP_button.grid(row=0, column=0, pady=30)

# Function to go to home page
def go_to_home_page():
# Sidebar Frames
    if 'PasswordMaking_Frame' in globals() and PasswordMaking_Frame.winfo_exists():
        PasswordMaking_Frame.grid_forget()
    if 'Notes_Frame' in globals() and Notes_Frame.winfo_exists():
        Notes_Frame.grid_forget()
    if 'Banking_Cards_Frame' in globals() and Banking_Cards_Frame.winfo_exists():
        Banking_Cards_Frame.grid_forget()
    if 'Network_Frame' in globals() and Network_Frame.winfo_exists():
        Network_Frame.grid_forget()

# Bottom Bar Frames
    if 'MainPasswords_Frame' in globals() and MainPasswords_Frame.winfo_exists():
        MainPasswords_Frame.grid_forget()
    if 'MainNotes_Frame' in globals() and MainNotes_Frame.winfo_exists():
        MainNotes_Frame.grid_forget()
    if 'MainArchive_Frame' in globals() and MainArchive_Frame.winfo_exists():
        MainArchive_Frame.grid_forget()
    if 'Profile_Frame' in globals() and Profile_Frame.winfo_exists():
        Profile_Frame.grid_forget()

    # Bring back main home frame
    main_frame.grid(row=1, column=1, sticky="nsew")
ValtureP_button = customtkinter.CTkButton(bottom_bar, text="Passwords 🐦", width=60, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_passwords_page())
ValtureP_button.grid(row=0, column=1, pady=30)


# Passwords
def open_passwords_page():
    global MainPasswords_Frame
    if "MainPasswords_Fram" in globals() and MainPasswords_Frame.winfo_exists():
        MainPasswords_Frame.destroy()

    #  The creation of the frame and border
    MainPasswords_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    MainPasswords_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
    PasswordBorder_Frame = customtkinter.CTkFrame(MainPasswords_Frame, fg_color="#A9A9A9")
    PasswordBorder_Frame.pack(fill="both", expand=True, padx=5, pady=5)

    label = customtkinter.CTkLabel(PasswordBorder_Frame, text="Passwords", font=("Verdana", 20))
    label.pack(pady=20)

    scroll_frame = customtkinter.CTkScrollableFrame(PasswordBorder_Frame, fg_color="#A9A9A9")
    scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
    PasswordBorder_Frame = scroll_frame

    # Search Bar inside Passwords Page
    search_frame = customtkinter.CTkFrame(PasswordBorder_Frame, fg_color="#A9A9A9", height=50, width=480)
    search_frame.pack(pady=10)
    searching = customtkinter.CTkEntry(search_frame, placeholder_text="Search here...", width=450)
    searching.pack(pady=10)

    back_button = customtkinter.CTkButton(PasswordBorder_Frame, text="Back", command=close_passwords_page)
    back_button.pack(pady=20)

    main_frame.grid_forget()
    MainPasswords_Frame.grid(row=1, column=1, sticky="nsew")

    mycursor.execute("SELECT data_id, Title, Username, Email, Password FROM Account_Data_Password WHERE AccountID = %s", (account_id,))

    data = mycursor.fetchall()

    mycursor.execute("SELECT data_id, Card_Title, Card_Number, Expire_Date, CVV FROM Banking_Card WHERE AccountID = %s", (account_id,))
    banking_data = mycursor.fetchall()

    mycursor.execute(
        "SELECT data_id, Network_Title, Network, IP_Address, Password FROM Network_Data WHERE AccountID = %s", (account_id,))
    network_data = mycursor.fetchall()

# (AI GENERATED)
#********************************************************************************************************************
    if data:
        for index, row in enumerate(data):
            data_id, title, username, email, password = row

            entry_frame = customtkinter.CTkFrame(PasswordBorder_Frame, fg_color="#A9A9A9")
            entry_frame.pack(fill="x", padx=10, pady=5)

            entry_label = customtkinter.CTkLabel(entry_frame,
                                                 text=f"{index + 1}. Title: {title} | Username: {username} | Email: {email} | Password: {password}",
                                                 anchor="w", justify="left", font=("Courier", 14), text_color="black"
                                                 )
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))

            archive_button = customtkinter.CTkButton(entry_frame, text="Archive", width=60,
                                                  command=lambda d=data_id, frame = entry_frame: archive_row(d, frame))
            archive_button.pack(side="left", padx=5)

            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame = entry_frame: delete_row(d, frame))
            delete_button.pack(side="left", padx=5)
    else:
        no_data_label = customtkinter.CTkLabel(PasswordBorder_Frame, text="No password and account data found.")
        no_data_label.pack()
    # **********************************************************************************************

    if banking_data:
        for index, row in enumerate(banking_data, start=len(data) + 1):
            data_id, card_name, card_number, expiry_date, cvv = row

            entry_frame = customtkinter.CTkFrame(PasswordBorder_Frame, fg_color="#A9A9A9")
            entry_frame.pack(fill="x", padx=10, pady=5)

            entry_label = customtkinter.CTkLabel(entry_frame, text=f"{index}. Card Name: {card_name} | Card Number: {card_number} | Expiry: {expiry_date} | CVV: {cvv}", anchor="w", justify="left", font=("Courier", 14), text_color="black" )
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))

            archive_button = customtkinter.CTkButton(entry_frame, text="Archive", width=60, command=lambda d=data_id, frame = entry_frame: archive_banking_row(d, frame))
            archive_button.pack(side="left", padx=5)

            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame = entry_frame: delete_banking_row(d, frame))
            delete_button.pack(side="left", padx=5)
    else:
        no_data_label = customtkinter.CTkLabel(PasswordBorder_Frame, text="No banking card data found.")
        no_data_label.pack()

    if network_data:
        for index, row in enumerate(network_data, start=len(banking_data) + 1):
            data_id, network_name, network_type, ip_address, password = row

            entry_frame = customtkinter.CTkFrame(PasswordBorder_Frame, fg_color="#A9A9A9")
            entry_frame.pack(fill="x", padx=10, pady=5)

            entry_label = customtkinter.CTkLabel(entry_frame, text=f"{index}. Network Name: {network_name} | Network Type: {network_type} | IP Address: {ip_address} | Network Password: {password}", anchor="w", justify="left", font=("Courier", 14), text_color="black")
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))

            archive_button = customtkinter.CTkButton(entry_frame, text="Archive", width=60, command=lambda d=data_id, frame = entry_frame: archive_network_row(d, frame))
            archive_button.pack(side="left", padx=5)

            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame = entry_frame: delete_network_row(d, frame))
            delete_button.pack(side="left", padx=5)
    else:
        no_data_label = customtkinter.CTkLabel(PasswordBorder_Frame, text="No network data found.")
        no_data_label.pack()


def delete_row(data_id, destroyed_frame):
    mycursor.execute("SELECT * FROM Account_Data_Password WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        mycursor.execute("""
            INSERT INTO Deleted_Passwords (data_id, AccountID, Title, Username, Email, Password)
            VALUES (%s, %s, %s, %s, %s, %s)""", row)

        mycursor.execute("DELETE FROM Account_Data_Password WHERE data_id = %s", (data_id,))
        login_database.commit()

        destroyed_frame.destroy()

def archive_row(data_id, destroyed_frame):
    mycursor.execute("SELECT * FROM Account_Data_Password WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        mycursor.execute("""
            INSERT INTO Archive_Data_Password (data_id, AccountID, Title, Username, Email, Password)
            VALUES (%s, %s, %s, %s, %s, %s)""", row)

        mycursor.execute("DELETE FROM Account_Data_Password WHERE data_id = %s", (data_id,))
        login_database.commit()

        destroyed_frame.destroy()

def delete_banking_row(data_id, destroyed_frame):
    mycursor.execute("SELECT * FROM Banking_Card WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        mycursor.execute("DELETE FROM Banking_Card WHERE data_id = %s", (data_id,))
        login_database.commit()

        destroyed_frame.destroy()


def archive_banking_row(data_id, destroyed_frame):
#(AI GENERATED)
#****************************************************************************************************************
    # Check if it's already archived
    mycursor.execute("SELECT 1 FROM Archive_Banking_Card WHERE data_id = %s", (data_id,))
    if mycursor.fetchone():
        print(f"Data ID {data_id} is already archived.")
        return  # or optionally delete from Banking_Card anyway

    # Get the original data
    mycursor.execute("SELECT * FROM Banking_Card WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
#*************************************************************************************************************

    if row:
        # Insert into archive table
        mycursor.execute("""
            INSERT INTO Archive_Banking_Card (data_id, AccountID, Card_Title, Card_Number, Expire_Date, CVV)
            VALUES (%s, %s, %s, %s, %s, %s)""", row)

        # Delete from original
        mycursor.execute("DELETE FROM Banking_Card WHERE data_id = %s", (data_id,))
        login_database.commit()

        destroyed_frame.destroy()

def delete_network_row(data_id, destroyed_frame):
    mycursor.execute("SELECT * FROM Network_Data WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        mycursor.execute("DELETE FROM Network_Data WHERE data_id = %s", (data_id,))
        login_database.commit()

        destroyed_frame.destroy()

def archive_network_row(data_id, destroyed_frame):
    # Check if it's already archived
    mycursor.execute("SELECT 1 FROM Archive_Network_Data WHERE data_id = %s", (data_id,))
    if mycursor.fetchone():
        print(f"Data ID {data_id} is already archived.")
        return  # or optionally delete from Banking_Card anyway

    # Get the original data
    mycursor.execute("SELECT * FROM Network_Data WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        mycursor.execute("""
                INSERT INTO Archive_Network_Data (data_id, AccountID, Network_Title, Network, IP_Address, Password)
                VALUES (%s, %s, %s, %s, %s, %s)""", row)

        mycursor.execute("DELETE FROM Network_Data WHERE data_id = %s", (data_id,))
        login_database.commit()

        destroyed_frame.destroy()


# Closing the page
def close_passwords_page():
    MainPasswords_Frame.destroy()
    main_frame.grid(row=1, column=1, sticky="nsew")


# Notes button in bottom bar
Notes_button = customtkinter.CTkButton(bottom_bar, text="Notes 📝", width=60, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray",command=lambda: open_Notes_page())
Notes_button.grid(row=0, column=2, pady=30, )


# Notes Page
def open_Notes_page():
    global MainNotes_Frame
    if "MainNotes_Frame" in globals() and MainNotes_Frame.winfo_exists():
        MainNotes_Frame.destroy()

    #  The creation of the frame and border
    MainNotes_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    MainNotes_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
    NotesBorder_Frame = customtkinter.CTkFrame(MainNotes_Frame, fg_color="#A9A9A9")
    NotesBorder_Frame.pack(fill="both", expand=True, padx=5, pady=5)

    scroll_frame = customtkinter.CTkScrollableFrame(NotesBorder_Frame, fg_color="#A9A9A9")
    scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
    NotesBorder_Frame = scroll_frame

    label = customtkinter.CTkLabel(NotesBorder_Frame, text="Notes List", font=("Verdana", 20))
    label.pack(pady=20)

    # Search Bar inside Passwords Page
    search_frame = customtkinter.CTkFrame(NotesBorder_Frame, fg_color="#A9A9A9", height=50, width=480)
    search_frame.pack(pady=10)
    searching = customtkinter.CTkEntry(search_frame, placeholder_text="Search here...", width=450)
    searching.pack(pady=10)

    back_button = customtkinter.CTkButton(NotesBorder_Frame, text="Back", command=close_Notes_page)
    back_button.pack(pady=20)

    mycursor.execute(
        "SELECT data_id, Notes_title, Notes_body FROM Notes_Data WHERE AccountID = %s",
        (account_id,))
    notes_data = mycursor.fetchall()

    if notes_data:
        for index, row in enumerate(notes_data):
            data_id, notes_title, notes_body = row

            entry_frame = customtkinter.CTkFrame(NotesBorder_Frame, fg_color="#A9A9A9")
            entry_frame.pack(fill="x", padx=10, pady=5)

            entry_label = customtkinter.CTkLabel(entry_frame, text=f"{index}. Notes Title: {notes_title} | Notes Body: {notes_body}", anchor="w", justify="left", font=("Courier", 14), text_color="black")
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))

            archive_button = customtkinter.CTkButton(entry_frame, text="Archive", width=60,
                                                  command=lambda d=data_id, frame = entry_frame: archive_notes_row(d, frame))
            archive_button.pack(side="left", padx=5)

            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red",
                                                    command=lambda d=data_id, frame = entry_frame: delete_notes_row(d, frame))
            delete_button.pack(side="left", padx=5)
    else:
        no_data_label = customtkinter.CTkLabel(NotesBorder_Frame, text="No notes data found.")
        no_data_label.pack()

def archive_notes_row(data_id, destroyed_frame):
    mycursor.execute("SELECT * FROM Notes_Data WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        mycursor.execute("""
            INSERT INTO Archive_Notes_Data (data_id, AccountID, Notes_title, Notes_body)
            VALUES (%s, %s, %s, %s)""", row)

        mycursor.execute("DELETE FROM Notes_Data WHERE data_id = %s", (data_id,))
        login_database.commit()

        destroyed_frame.destroy()

def delete_notes_row(data_id, destroyed_frame):
    mycursor.execute("SELECT * FROM Notes_Data WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        mycursor.execute("DELETE FROM Notes_Data WHERE data_id = %s", (data_id,))
        login_database.commit()

        destroyed_frame.destroy()



def close_Notes_page():
    MainNotes_Frame.destroy()
    main_frame.grid(row=1, column=1, sticky="nsew")


Archive_button = customtkinter.CTkButton(bottom_bar, text="Archive 📦", width=60, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_archive_page())
Archive_button.grid(row=0, column=3, pady=30, )


# Open archive page
def open_archive_page():
    global MainArchive_Frame
    if "MainArchive_Frame" in globals() and MainArchive_Frame.winfo_exists():
        MainArchive_Frame.destroy()

    #  The creation of the frame and border
    MainArchive_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    MainArchive_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
    ArchiveBorder_Frame = customtkinter.CTkFrame(MainArchive_Frame, fg_color="#A9A9A9")
    ArchiveBorder_Frame.pack(fill="both", expand=True, padx=5, pady=5)

    scroll_frame = customtkinter.CTkScrollableFrame(ArchiveBorder_Frame, fg_color="#A9A9A9")
    scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
    ArchiveBorder_Frame = scroll_frame

    label = customtkinter.CTkLabel(ArchiveBorder_Frame, text="Archived Passwords", font=("Verdana", 20))
    label.pack(pady=20)

    # Search Bar inside Passwords Page
    search_frame = customtkinter.CTkFrame(ArchiveBorder_Frame, fg_color="#A9A9A9", height=50, width=480)
    search_frame.pack(pady=10)
    searching = customtkinter.CTkEntry(search_frame, placeholder_text="Search here...", width=450)
    searching.pack(pady=10)

    mycursor.execute(
        "SELECT data_id, Title, Username, Email, Password FROM Archive_Data_Password WHERE AccountID = %s",
        (account_id,))

    data = mycursor.fetchall()

    if data:
        for index, row in enumerate(data):
            data_id, title, username, email, password = row

            entry_frame = customtkinter.CTkFrame(ArchiveBorder_Frame, fg_color="#A9A9A9")
            entry_frame.pack(fill="x", padx=10, pady=5)

            entry_label = customtkinter.CTkLabel(entry_frame, text=f"{index + 1}. Title: {title} | Username: {username} | Email: {email} | Password: {password}", anchor="w", justify="left", font=("Courier", 14), text_color="black")
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))

            archive_button = customtkinter.CTkButton(entry_frame, text="Remove", width=60, command=lambda d=data_id, frame = entry_frame: remove_password_row(d, frame))
            archive_button.pack(side="left", padx=5)

            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame=entry_frame: delete_archive_password_row(d,frame))
            delete_button.pack(side="left", padx=5)
    else:
        no_data_label = customtkinter.CTkLabel(ArchiveBorder_Frame, text="No password and account data found.")
        no_data_label.pack()

    mycursor.execute(
        "SELECT data_id, Card_Title, Card_Number, Expire_Date, CVV FROM Archive_Banking_Card WHERE AccountID = %s",
        (account_id,))

    banking_data = mycursor.fetchall()

    if banking_data:
        for index, row in enumerate(banking_data, start=len(data) + 1):
            data_id, card_name, card_number, expiry_date, cvv = row

            entry_frame = customtkinter.CTkFrame(ArchiveBorder_Frame, fg_color="#A9A9A9")
            entry_frame.pack(fill="x", padx=10, pady=5)

            entry_label = customtkinter.CTkLabel(entry_frame, text=f"{index}. Card Name: {card_name} | Card Number: {card_number} | Expiry: {expiry_date} | CVV: {cvv}", anchor="w", justify="left", font=("Courier", 14), text_color="black")
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))

            archive_button = customtkinter.CTkButton(entry_frame, text="Remove", width=60, command=lambda d=data_id, frame = entry_frame: remove_banking_row(d, frame))
            archive_button.pack(side="left", padx=5)

            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame=entry_frame: delete_archive_banking_row(d,  frame))
            delete_button.pack(side="left", padx=5)
    else:
        no_data_label = customtkinter.CTkLabel(ArchiveBorder_Frame, text="No banking card data found.")
        no_data_label.pack()

    mycursor.execute(
        "SELECT data_id, Network_Title, Network, IP_Address, Password FROM Archive_Network_Data WHERE AccountID = %s",
        (account_id,))
    network_data = mycursor.fetchall()

    if network_data:
        for index, row in enumerate(network_data, start=len(banking_data) + 1):
            data_id, network_name, network_type, ip_address, password = row

            entry_frame = customtkinter.CTkFrame(ArchiveBorder_Frame, fg_color="#A9A9A9")
            entry_frame.pack(fill="x", padx=10, pady=5)

            entry_label = customtkinter.CTkLabel(entry_frame, text=f"{index}. Network Name: {network_name} | Network Type: {network_type} | IP Address: {ip_address} | Network Password: {password}", anchor="w", justify="left", font=("Courier", 14), text_color="black")
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))

            archive_button = customtkinter.CTkButton(entry_frame, text="Remove", width=60, command=lambda d=data_id, frame = entry_frame: remove_network_row(d, frame))
            archive_button.pack(side="left", padx=5)

            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame=entry_frame: delete_archive_network_row(d,  frame))
            delete_button.pack(side="left", padx=5)
    else:
        no_data_label = customtkinter.CTkLabel(ArchiveBorder_Frame, text="No network data found.")
        no_data_label.pack()

    mycursor.execute(
        "SELECT data_id, Notes_title, Notes_body FROM Archive_Notes_Data WHERE AccountID = %s",
        (account_id,))
    notes_data = mycursor.fetchall()

    if notes_data:
        for index, row in enumerate(notes_data, start=len(network_data) + 1):
            data_id, notes_title, notes_body = row

            entry_frame = customtkinter.CTkFrame(ArchiveBorder_Frame, fg_color="#A9A9A9")
            entry_frame.pack(fill="x", padx=10, pady=5)

            entry_label = customtkinter.CTkLabel(entry_frame, text=f"{index}. Notes Title: {notes_title} | Notes Body: {notes_body}", anchor="w", justify="left", font=("Courier", 14), text_color="black")
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))

            archive_button = customtkinter.CTkButton(entry_frame, text="Remove", width=60, command=lambda d=data_id, frame = entry_frame: remove_notes_row(d, frame))
            archive_button.pack(side="left", padx=5)

            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame = entry_frame: delete_archive_notes_row(d, frame))
            delete_button.pack(side="left", padx=5)
    else:
        no_data_label = customtkinter.CTkLabel(ArchiveBorder_Frame, text="No notes data found.")
        no_data_label.pack()

    back_button = customtkinter.CTkButton(ArchiveBorder_Frame, text="Back", command=close_archive_page)
    back_button.pack(pady=10)

    main_frame.grid_forget()
    MainArchive_Frame.grid(row=1, column=1, sticky="nsew")

    def remove_password_row(data_id, destroyed_frame):
        mycursor.execute("SELECT * FROM Archive_Data_Password WHERE data_id = %s", (data_id,))
        row = mycursor.fetchone()
        if row:
            mycursor.execute("""
                INSERT INTO Account_Data_Password (data_id, AccountID, Title, Username, Email, Password)
                VALUES (%s, %s, %s, %s, %s, %s)""", row)

            mycursor.execute("DELETE FROM Archive_Data_Password WHERE data_id = %s", (data_id,))
            login_database.commit()

            destroyed_frame.destroy()

    def remove_banking_row(data_id, destroyed_frame):
        mycursor.execute("SELECT * FROM Archive_Banking_Card WHERE data_id = %s", (data_id,))
        row = mycursor.fetchone()
        if row:
            mycursor.execute("""
                INSERT INTO Banking_Card (data_id, AccountID, Card_Title, Card_Number, Expire_Date, CVV)
                VALUES (%s, %s, %s, %s, %s, %s)""", row)

            mycursor.execute("DELETE FROM Archive_Banking_Card WHERE data_id = %s", (data_id,))
            login_database.commit()

            destroyed_frame.destroy()

    def remove_network_row(data_id, destroyed_frame):
        mycursor.execute("SELECT * FROM Archive_Network_Data WHERE data_id = %s", (data_id,))
        row = mycursor.fetchone()
        if row:
            mycursor.execute("""
                INSERT INTO Network_Data (data_id, AccountID, Network_Title, Network, IP_Address, Password)
                VALUES (%s, %s, %s, %s, %s, %s)""", row)

            mycursor.execute("DELETE FROM Archive_Network_Data WHERE data_id = %s", (data_id,))
            login_database.commit()

            destroyed_frame.destroy()

    def remove_notes_row(data_id, destroyed_frame):
        mycursor.execute("SELECT * FROM Archive_Notes_Data WHERE data_id = %s", (data_id,))
        row = mycursor.fetchone()
        if row:
            mycursor.execute("""
                INSERT INTO Notes_Data (data_id, AccountID, Notes_title, Notes_body)
                VALUES (%s, %s, %s, %s)""", row)

            mycursor.execute("DELETE FROM Archive_Notes_Data WHERE data_id = %s", (data_id,))
            login_database.commit()

            destroyed_frame.destroy()

    def delete_archive_password_row(data_id, destroyed_frame):
        mycursor.execute("SELECT * FROM Archive_Data_Password WHERE data_id = %s", (data_id,))
        row = mycursor.fetchone()
        if row:
            mycursor.execute("DELETE FROM Archive_Data_Password WHERE data_id = %s", (data_id,))
            login_database.commit()

            destroyed_frame.destroy()

    def delete_archive_banking_row(data_id, destroyed_frame):
        mycursor.execute("SELECT * FROM Archive_Banking_Card WHERE data_id = %s", (data_id,))
        row = mycursor.fetchone()
        if row:
            mycursor.execute("DELETE FROM Archive_Banking_Card WHERE data_id = %s", (data_id,))
            login_database.commit()

            destroyed_frame.destroy()

    def delete_archive_network_row(data_id, destroyed_frame):
        mycursor.execute("SELECT * FROM Archive_Network_Data WHERE data_id = %s", (data_id,))
        row = mycursor.fetchone()
        if row:
            mycursor.execute("DELETE FROM Archive_Network_Data WHERE data_id = %s", (data_id,))
            login_database.commit()

            destroyed_frame.destroy()

    def delete_archive_notes_row(data_id, destroyed_frame):
        mycursor.execute("SELECT * FROM Archive_Notes_Data WHERE data_id = %s", (data_id,))
        row = mycursor.fetchone()
        if row:
            mycursor.execute("DELETE FROM Archive_Notes_Data WHERE data_id = %s", (data_id,))
            login_database.commit()

            destroyed_frame.destroy()


def close_archive_page():
    MainArchive_Frame.destroy()
    main_frame.grid(row=1, column=1, sticky="nsew")


# Profile button in bottom bar
Profile_button = customtkinter.CTkButton(bottom_bar, text="Profile 👥", width=60, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_Profile_Page())
Profile_button.grid(row=0, column=4, pady=5)


# This is the profile page settings here you can upload an image and your name and save it!
def open_Profile_Page():
    window.minsize(800, 600)
    window.maxsize(1920, 1080)
    global Profile_Frame, Border_Frame, Profile_Name, PImage_label

    # Makes the frame if its not already made
    if "Profile_Frame" not in globals():
        Profile_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
        Profile_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

        Profile_Border_Frame = customtkinter.CTkFrame(Profile_Frame, fg_color="#A9A9A9")
        Profile_Border_Frame.pack(fill="both", expand=True, padx=5, pady=5)

        scroll_frame = customtkinter.CTkScrollableFrame(Profile_Border_Frame, fg_color="#A9A9A9")
        scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
        Profile_Border_Frame = scroll_frame

        label = customtkinter.CTkLabel(Profile_Border_Frame, text="Profile Page", font=("Verdana", 30), text_color="black")
        label.pack(pady=20)

        PImage_label = customtkinter.CTkLabel(Profile_Border_Frame, text="Please put a picture!", width=300, height=300, fg_color="black")
        PImage_label.pack(pady=10)

        UploadingI = customtkinter.CTkButton(Profile_Border_Frame, text="Upload Image", command=upload_profile_image)
        UploadingI.pack(pady=30)

        # Profile Name Input Field
        Profile_Name = customtkinter.StringVar()
        name_entry = customtkinter.CTkEntry(Profile_Border_Frame, textvariable=Profile_Name, width=250, placeholder_text="Enter your name")
        name_entry.pack(pady=20)

        Save_button = customtkinter.CTkButton(Profile_Border_Frame, text="Save Name", command=save_profile_name)
        Save_button.pack(pady=5)

        # Back Button
        back_button = customtkinter.CTkButton(Profile_Border_Frame, text="Back", command=close_Profile_Page)
        back_button.pack(pady=20)

    # Show the Profile Frame
    main_frame.grid_forget()
    Profile_Frame.grid(row=1, column=1, sticky="nsew")


def upload_profile_image():
    global profile_image_large, profile_image_small, PImage_label, profile_box_label

    file_path = filedialog.askopenfilename(title="Choosing PFP", filetypes=[("Image Files", "*.png *.jpg *.jpeg")])

    if file_path:
        img = Image.open(file_path)

        # Image for profile page
        img_large = img.resize((400, 400), Image.LANCZOS)
        profile_image_large = CTkImage(light_image=img_large, dark_image=img_large, size=(400, 400))

        # Image in top-right profile box
        img_small = img.resize((50, 50), Image.Resampling.LANCZOS)
        profile_image_small = CTkImage(light_image=img_small, dark_image=img_small, size=(70, 70))

        # The profile page image
        PImage_label.configure(image=profile_image_large, text="")
        PImage_label.image = profile_image_large

        # The profile box image
        profile_box_label.configure(image=profile_image_small, text="")
        profile_box_label.image = profile_image_small

    # Now we can save it and close the page and when we open it it will save till you click X out


def save_profile_name():
    global Profile_Name
    profile_name = Profile_Name.get()


def close_Profile_Page():
    Profile_Frame.grid_forget()
    main_frame.grid(row=1, column=1, sticky="nsew")


# Profile Picture Box inside main_frame (Top-Right Corner)
profile_box = customtkinter.CTkFrame(main_frame, fg_color="#282929", border_width=2, border_color="gray", width=50, height=50)
profile_box.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

# The image label inside the profile box
profile_box_label = customtkinter.CTkLabel(profile_box, text="")
profile_box_label.pack(expand=True)


# New Settings Button at Bottom
def open_settings_page():
    acc2.opening_settings(update_main_theme)
    settings_window = acc2.SettingsApp(parent = window)
    settings_window.mainloop()

Settings_button = customtkinter.CTkButton(bottom_bar, text="Settings ⚙️", width=10, height=70, corner_radius=900, fg_color="#282929", border_width=1, border_color="gray", command=lambda: open_settings_page())
Settings_button.grid(row=0, column=5, pady=5)

# Bottom Bar Setup
#🏠
bottom_bar.columnconfigure(0, weight=2)
# 🐦
bottom_bar.columnconfigure(1, weight=2)
# 📝
bottom_bar.columnconfigure(2, weight=1)
# 📦
bottom_bar.columnconfigure(3, weight=1)
# 👥
bottom_bar.columnconfigure(4, weight=1)
# ⚙️
bottom_bar.columnconfigure(5, weight=1)


# Left bar stuff
# Regular Password Maker
def open_passwordMaker_page(*args, **kwargs):
    import string, random  # needed for password generation
    global PasswordMaking_Frame
    if "PasswordMaking_Frame" in globals() and PasswordMaking_Frame.winfo_exists():
        PasswordMaking_Frame.destroy()
        window.minsize(800, 600)
        window.maxsize(1920, 1080)

    # Main frame and border setup
    PasswordMaking_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    PasswordMaking_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
    PasswordMakingBorder_Frame = customtkinter.CTkFrame(PasswordMaking_Frame, fg_color="#A9A9A9")
    PasswordMakingBorder_Frame.pack(fill="both", expand=True, padx=5, pady=5)
    scroll_frame = customtkinter.CTkScrollableFrame(PasswordMakingBorder_Frame, fg_color="#A9A9A9")
    scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
    PasswordMakingBorder_Frame = scroll_frame

    label = customtkinter.CTkLabel(PasswordMakingBorder_Frame, text="Password Maker", font=("Verdana", 20), text_color="black")
    label.grid(row=0, column=2, pady=(10, 20), sticky="nsew")

    label = customtkinter.CTkLabel(PasswordMakingBorder_Frame, text="Password Title", text_color="black")
    label.grid(row=1, column=2, pady=10, sticky="nsew")

    Title_entry = customtkinter.CTkEntry(PasswordMakingBorder_Frame, placeholder_text="Enter Title")
    Title_entry.grid(row=2, column=2, pady=10, sticky="nsew")

    label = customtkinter.CTkLabel(PasswordMakingBorder_Frame, text="Username", text_color="black")
    label.grid(row=3, column=2, pady=10, sticky="nsew")

    Username_entry = customtkinter.CTkEntry(PasswordMakingBorder_Frame, placeholder_text="Enter Username")
    Username_entry.grid(row=4, column=2, pady=10, sticky="nsew")

    label = customtkinter.CTkLabel(PasswordMakingBorder_Frame, text="Email", text_color="black")
    label.grid(row=5, column=2, pady=10, sticky="nsew")

    Email_entry = customtkinter.CTkEntry(PasswordMakingBorder_Frame, placeholder_text="Enter Email")
    Email_entry.grid(row=6, column=2, pady=10, sticky="nsew")

    label = customtkinter.CTkLabel(PasswordMakingBorder_Frame, text="Password", text_color="black")
    label.grid(row=7, column=2, pady=10, sticky="nsew")

    Password_entry = customtkinter.CTkEntry(PasswordMakingBorder_Frame, placeholder_text="Enter Password")
    Password_entry.grid(row=8, column=2, pady=10, sticky="nsew")

    label = customtkinter.CTkLabel(PasswordMakingBorder_Frame, text="Password Generation Checklist", text_color="black")
    label.grid(row=9, column=2, pady=10, sticky="nsew")
    #######################################################################################################################################################
    # AI-Assisted Code: Password Generation Feature - Marteno Romaya
    # This section was created with the help of ChatGPT to implement, as i accidentally deleted it when trying to delete a different one, i had it changed, the link is provided to the history
    # and it will be noted in the report. Any further questions ill be happy to answer
    # https://chatgpt.com/share/67e6ef3a-edf4-800a-8ad2-d5eb1e63c908

    # Create BooleanVars to hold checkbox states for character types
    use_special = customtkinter.BooleanVar(value=False)
    use_numbers = customtkinter.BooleanVar(value=False)
    use_upper = customtkinter.BooleanVar(value=False)
    use_lower = customtkinter.BooleanVar(value=False)

    # Checkboxes for user selection
    customtkinter.CTkCheckBox(PasswordMakingBorder_Frame, text="Special Characters", variable=use_special,
                              text_color="black").grid(row=10, column=2, pady=5, sticky="nsew")
    customtkinter.CTkCheckBox(PasswordMakingBorder_Frame, text="Numbers", variable=use_numbers,
                              text_color="black").grid(row=11, column=2, pady=5, sticky="nsew")
    customtkinter.CTkCheckBox(PasswordMakingBorder_Frame, text="Uppercase Letters", variable=use_upper,
                              text_color="black").grid(row=10, column=3, pady=5, sticky="nsew")
    customtkinter.CTkCheckBox(PasswordMakingBorder_Frame, text="Lowercase Letters", variable=use_lower,
                              text_color="black").grid(row=11, column=3, pady=5, sticky="nsew")

    # Label to display the result
    result_label = customtkinter.CTkLabel(PasswordMakingBorder_Frame, text="", text_color="black")
    result_label.grid(row=12, column=2, pady=10, sticky="nsew")

    # Password generator function
    def generate_password():
        char_pool = ""
        if use_special.get(): char_pool += string.punctuation
        if use_numbers.get(): char_pool += string.digits
        if use_upper.get(): char_pool += string.ascii_uppercase
        if use_lower.get(): char_pool += string.ascii_lowercase

        if not char_pool:
            result_label.configure(text="Select at least one option.")
            return

        generated = ''.join(random.choice(char_pool) for _ in range(12))
        result_label.configure(text=f"Generated: {generated}")

    # Button to trigger password generation
    customtkinter.CTkButton(PasswordMakingBorder_Frame, text="Generate Password", command=generate_password).grid(
        row=13, column=2, pady=10, sticky="nsew")

    #######################################################################################################################################################
    def store_password_data():
        global account_id

        if account_id is None:
            print("Error: account_id is not set. Data cannot be stored")
            return

        title = Title_entry.get()
        username = Username_entry.get()
        email = Email_entry.get()
        password = Password_entry.get()

        mycursor.execute(
            "INSERT INTO Account_Data_Password (AccountID, Title, Username, Email, Password) VALUES (%s,%s,%s,%s,%s)",
            (account_id, title, username, email, password))
        login_database.commit()
        created_label = customtkinter.CTkLabel(PasswordMakingBorder_Frame, text="Successfully created", font=("Courier", 14, "bold"), text_color="green")
        created_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)

    # Save Button
    create_button = customtkinter.CTkButton(PasswordMakingBorder_Frame, text="Create", command=store_password_data)
    create_button.grid(row=14, column=2, pady=(30, 10), sticky="nsew")

    # Back Button
    back_button = customtkinter.CTkButton(PasswordMakingBorder_Frame, text="Back", command=close_passwordMaker_page)
    back_button.grid(row=15, column=2, pady=(30, 10), sticky="nsew")

    main_frame.grid_forget()
    PasswordMaking_Frame.grid(row=1, column=1, sticky="nsew")

    PasswordMakingBorder_Frame.columnconfigure(0, weight=1)
    PasswordMakingBorder_Frame.columnconfigure(1, weight=1)
    PasswordMakingBorder_Frame.columnconfigure(2, weight=1)
    PasswordMakingBorder_Frame.columnconfigure(3, weight=1)
    PasswordMakingBorder_Frame.columnconfigure(4, weight=1)


# Closing the page
def close_passwordMaker_page():
    PasswordMaking_Frame.destroy()
    main_frame.grid(row=1, column=1, sticky="nsew")


# Open Notes page
def open_notes_page():
    global Notes_Frame
    if "Notes_Frame" in globals() and Notes_Frame.winfo_exists():
        Notes_Frame.destroy()

    Notes_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    Notes_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
    NotesBorder_Frame = customtkinter.CTkFrame(Notes_Frame, fg_color="#A9A9A9")
    NotesBorder_Frame.pack(fill="both", expand=True, padx=5, pady=5)

    scroll_frame = customtkinter.CTkScrollableFrame(NotesBorder_Frame, fg_color="#A9A9A9")
    scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
    NotesBorder_Frame = scroll_frame

    label = customtkinter.CTkLabel(NotesBorder_Frame, text="Notes Maker", font=("Verdana", 20,), text_color="black")
    label.grid(row=0, column=2, pady=10, sticky="ew")

    Notes_title_entry = customtkinter.CTkEntry(NotesBorder_Frame, placeholder_text="Enter Title")
    Notes_title_entry.grid(row=1, column=2, pady=10, sticky="ew")

    label = customtkinter.CTkLabel(NotesBorder_Frame, text="Enter Notes", text_color="black")
    label.grid(row=3, column=2, pady=10, sticky="ew")

    Notes_body = customtkinter.CTkTextbox(NotesBorder_Frame, height=150)
    Notes_body.grid(row=4, column=2, pady=10, sticky="ew")

    def store_notes_data():
        global account_id

        if account_id is None:
            print("Error: account_id is not set. Data cannot be stored")
            return

        notes_title = Notes_title_entry.get()
        notes_body = Notes_body.get("1.0", "end").strip()

        mycursor.execute(
            "INSERT INTO Notes_Data (AccountID, Notes_title, Notes_body) VALUES (%s,%s,%s)",
            (account_id, notes_title, notes_body))
        login_database.commit()
        created_label = customtkinter.CTkLabel(NotesBorder_Frame, text="Successfully created", font=("Courier", 14, "bold"), text_color="green")
        created_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)

    create_button = customtkinter.CTkButton(NotesBorder_Frame, text="Create", command=store_notes_data)
    create_button.grid(row=5, column=2, pady=(30, 10), sticky="ew")

    back_button = customtkinter.CTkButton(NotesBorder_Frame, text="Back", command=close_notes_page)
    back_button.grid(row=6, column=2, pady=10, sticky="ew")

    main_frame.grid_forget()
    Notes_Frame.grid(row=1, column=1, sticky="nsew")

    NotesBorder_Frame.columnconfigure(0, weight=1)
    NotesBorder_Frame.columnconfigure(1, weight=2)
    NotesBorder_Frame.columnconfigure(2, weight=1)
    NotesBorder_Frame.columnconfigure(3, weight=1)
    NotesBorder_Frame.columnconfigure(4, weight=1)
    NotesBorder_Frame.columnconfigure(5, weight=1)
    NotesBorder_Frame.columnconfigure(6, weight=1)


def close_notes_page():
    Notes_Frame.destroy()
    main_frame.grid(row=1, column=1, sticky="nsew")


# Open Banking Cards page
def open_banking_cards_page():
    global Banking_Cards_Frame
    if "Banking_Cards_Frame" in globals() and Banking_Cards_Frame.winfo_exists():
        Banking_Cards_Frame.destroy()

    Banking_Cards_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    Banking_Cards_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

    BankBorder_Frame = customtkinter.CTkFrame(Banking_Cards_Frame, fg_color="#A9A9A9")
    BankBorder_Frame.pack(fill="both", expand=True, padx=5, pady=5)

    scroll_frame = customtkinter.CTkScrollableFrame(BankBorder_Frame, fg_color="#A9A9A9")
    scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
    BankBorder_Frame = scroll_frame

    label = customtkinter.CTkLabel(BankBorder_Frame, text="Banking Cards Maker", font=("Verdana", 20), text_color="black")
    label.grid(row=0, column=2, pady=(10, 20), sticky="n")

    label = customtkinter.CTkLabel(BankBorder_Frame, text="Card Title", text_color="black")
    label.grid(row=1, column=2, pady=10, sticky="ew")

    Card_Title_entry = customtkinter.CTkEntry(BankBorder_Frame, placeholder_text="Enter Title")
    Card_Title_entry.grid(row=2, column=2, pady=10, sticky="ew")

    label = customtkinter.CTkLabel(BankBorder_Frame, text="Card Number", text_color="black")
    label.grid(row=3, column=2, pady=10, sticky="ew")

    Card_Number_Entry = customtkinter.CTkEntry(BankBorder_Frame, placeholder_text="Enter Card Number")
    Card_Number_Entry.grid(row=4, column=2, pady=10, sticky="ew")

    label = customtkinter.CTkLabel(BankBorder_Frame, text="Expire Date", text_color="black")
    label.grid(row=5, column=2, pady=10, sticky="ew")

    Expiration_Date_entry = customtkinter.CTkEntry(BankBorder_Frame, placeholder_text="Enter Expiration Date (EX: 03-2025)")
    Expiration_Date_entry.grid(row=6, column=2, pady=10, sticky="ew")

    label = customtkinter.CTkLabel(BankBorder_Frame, text="CVV", text_color="black")
    label.grid(row=7, column=2, pady=10, sticky="ew")

    CVV_entry = customtkinter.CTkEntry(BankBorder_Frame, placeholder_text="Enter CVV")
    CVV_entry.grid(row=8, column=2, pady=10, sticky="ew")

    def store_bank_data():
        global account_id

        if account_id is None:
            print("Error: account_id is not set. Data cannot be stored")
            return

        card_title = Card_Title_entry.get()
        card_number = Card_Number_Entry.get()
        expiration_date = Expiration_Date_entry.get()
        cvv = CVV_entry.get()

        mycursor.execute(
            "INSERT INTO Banking_Card (AccountID, Card_Title, Card_Number, Expire_Date, CVV) VALUES (%s,%s,%s,%s,%s)",
            (account_id, card_title, card_number, expiration_date, cvv))
        login_database.commit()
        created_label = customtkinter.CTkLabel(BankBorder_Frame, text="Successfully created", font=("Courier", 14, "bold"), text_color="green")
        created_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)

    create_button = customtkinter.CTkButton(BankBorder_Frame, text="Create", command=store_bank_data)
    create_button.grid(row=9, column=2, pady=(30, 10), sticky="ew")

    back_button = customtkinter.CTkButton(BankBorder_Frame, text="Back", command=close_banking_cards_page)
    back_button.grid(row=10, column=2, pady=10, sticky="ew")

    main_frame.grid_forget()
    Banking_Cards_Frame.grid(row=1, column=1, sticky="nsew")

    BankBorder_Frame.columnconfigure(0, weight=1)
    BankBorder_Frame.columnconfigure(1, weight=2)
    BankBorder_Frame.columnconfigure(2, weight=1)
    BankBorder_Frame.columnconfigure(3, weight=1)
    BankBorder_Frame.columnconfigure(4, weight=1)
    BankBorder_Frame.columnconfigure(5, weight=1)
    BankBorder_Frame.columnconfigure(6, weight=1)


def close_banking_cards_page():
    Banking_Cards_Frame.destroy()
    main_frame.grid(row=1, column=1, sticky="nsew")


# Open Network page
def open_Network_page():
    global Network_Frame
    if "One_Time_Password_Frame" in globals() and Network_Frame.winfo_exists():
        Network_Frame.destroy()

    Network_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    Network_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

    Network_Border_Frame = customtkinter.CTkFrame(Network_Frame, fg_color="#A9A9A9")
    Network_Border_Frame.pack(fill="both", expand=True, padx=5, pady=5)

    scroll_frame = customtkinter.CTkScrollableFrame(Network_Border_Frame, fg_color="#A9A9A9")
    scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
    Network_Border_Frame = scroll_frame

    label = customtkinter.CTkLabel(Network_Border_Frame, text="Network Password Maker", font=("Verdana", 20), text_color="black")
    label.grid(row=0, column=2, pady=(10, 20), sticky="n")

    label = customtkinter.CTkLabel(Network_Border_Frame, text="Network Title", text_color="black")
    label.grid(row=1, column=2, pady=10, sticky="ew")

    Network_title_entry = customtkinter.CTkEntry(Network_Border_Frame, placeholder_text="Enter Network Title")
    Network_title_entry.grid(row=2, column=2, pady=10, sticky="ew")

    label = customtkinter.CTkLabel(Network_Border_Frame, text="Network", text_color="black")
    label.grid(row=3, column=2, pady=10, sticky="ew")

    Network_entry = customtkinter.CTkEntry(Network_Border_Frame, placeholder_text="Enter Network")
    Network_entry.grid(row=4, column=2, pady=10, sticky="ew")

    label = customtkinter.CTkLabel(Network_Border_Frame, text="Ip Address", text_color="black")
    label.grid(row=5, column=2, pady=10, sticky="ew")

    ip_address_entry = customtkinter.CTkEntry(Network_Border_Frame, placeholder_text="Enter IP Address")
    ip_address_entry.grid(row=6, column=2, pady=10, sticky="ew")

    label = customtkinter.CTkLabel(Network_Border_Frame, text="Password", text_color="black")
    label.grid(row=7, column=2, pady=10, sticky="ew")

    network_password_entry = customtkinter.CTkEntry(Network_Border_Frame, placeholder_text="Enter Network password")
    network_password_entry.grid(row=8, column=2, pady=10, sticky="ew")

    def store_network_data():
        global account_id

        if account_id is None:
            print("Error: account_id is not set. Data cannot be stored")
            return

        network_title = Network_title_entry.get()
        network = Network_entry.get()
        ip_address = ip_address_entry.get()
        network_password = network_password_entry.get()

        mycursor.execute(
            "INSERT INTO Network_Data (AccountID, Network_Title, Network, IP_Address, Password) VALUES (%s,%s,%s,%s,%s)",
            (account_id, network_title, network, ip_address, network_password))
        login_database.commit()
        created_label = customtkinter.CTkLabel(Network_Border_Frame, text="Successfully created", font=("Courier", 14, "bold"), text_color="green")
        created_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)

    create_button = customtkinter.CTkButton(Network_Border_Frame, text="Create", command=store_network_data)
    create_button.grid(row=9, column=2, pady=(30, 10), sticky="ew")

    back_button = customtkinter.CTkButton(Network_Border_Frame, text="Back", command=close_network_page)
    back_button.grid(row=10, column=2, pady=10, sticky="ew")

    main_frame.grid_forget()
    Network_Frame.grid(row=1, column=1, sticky="nsew")

    Network_Border_Frame.columnconfigure(0, weight=1)
    Network_Border_Frame.columnconfigure(1, weight=2)
    Network_Border_Frame.columnconfigure(2, weight=1)
    Network_Border_Frame.columnconfigure(3, weight=1)
    Network_Border_Frame.columnconfigure(4, weight=1)
    Network_Border_Frame.columnconfigure(5, weight=1)
    Network_Border_Frame.columnconfigure(6, weight=1)


def close_network_page():
    Network_Frame.destroy()
    main_frame.grid(row=1, column=1, sticky="nsew")


# Make it not change size
window.resizable(False, False)
window.mainloop()