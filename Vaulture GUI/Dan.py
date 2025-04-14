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
import pyotp

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

#######################################################################################################################################
# AI -Assisted Code: Theme Color Update Feature
def load_saved_theme_color():
    try:
        with open("theme_settings.txt", "r") as file:
            saved_color = file.read().strip()
            if not saved_color or saved_color.lower() == "#2c2f33":
                return "#133f61"  # Force blue if empty or default gray
            return saved_color
    except FileNotFoundError:
        return "#133f61"  # Default if no file exists
    
def load_saved_font_color():
    try:
        with open("font_color.txt", "r") as file:
            saved_color = file.read().strip()
            if not saved_color:
                return "white"  # Default
            return saved_color
    except FileNotFoundError:
        return "white"
    
def load_saved_mainframe_color():
    try:
        with open("mainframe_theme.txt", "r") as file:
            saved_color = file.read().strip()
            if not saved_color:
                return "#A9A9A9"  # Default
            return saved_color
    except FileNotFoundError:
        return "#A9A9A9"
        
saved_font_color = load_saved_font_color()
saved_mainframe_color = load_saved_mainframe_color()
saved_theme_color = load_saved_theme_color()
#######################################################################################################################################

# Main content frame
new_saved_mainframe_color = load_saved_mainframe_color()
main_frame = customtkinter.CTkFrame(window, fg_color=new_saved_mainframe_color)
main_frame.grid(row=1, column=1, padx=0, pady=0, sticky="nsew")
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
# AI -Assisted Code: Theme Color Update Feature
def update_main_theme(new_color, new_font_color=None):
    global saved_font_color

    if new_font_color:
        saved_font_color = new_font_color
    else:
        saved_font_color = load_saved_font_color()

    if new_color.lower() == "#2c2f33":
        actual_color = "#133f61"
    else:
        actual_color = new_color

    # Update sidebar and bottom bar
    sidebar.configure(fg_color=actual_color)
    bottom_bar.configure(fg_color=actual_color)

    # Update sidebar widgets
    for widget in sidebar.winfo_children():
        if widget == vulture_label or widget == Title_Spot:
            widget.configure(fg_color=actual_color)

    # Update bottom bar labels
    for widget in bottom_bar.winfo_children():
        if isinstance(widget, customtkinter.CTkLabel):
            widget.configure(fg_color=actual_color)

    hamburger_button.configure(fg_color=actual_color)

    saved_mainframe_color = load_saved_mainframe_color()
    main_frame.configure(fg_color=saved_mainframe_color)

    refresh_font_color()

def refresh_font_color():
    global saved_font_color
    saved_font_color = load_saved_font_color()

    # Update sidebar buttons
    for widget in sidebar.winfo_children():
        if isinstance(widget, customtkinter.CTkButton) or isinstance(widget, customtkinter.CTkLabel):
            widget.configure(text_color=saved_font_color)

    # Update bottom bar buttons
    for widget in bottom_bar.winfo_children():
        if isinstance(widget, customtkinter.CTkButton) or isinstance(widget, customtkinter.CTkLabel):
            widget.configure(text_color=saved_font_color)

    # Update main frame buttons (like hamburger button)
    hamburger_button.configure(text_color=saved_font_color)
    Settings_button.configure(text_color=saved_font_color)         

#######################################################################################################################################

# Sidebar buttons (These will appear when the sidebar is toggled)
# Hamburger Icon
hamburger_button = customtkinter.CTkButton(main_frame, text="☰", width=60, height=60, corner_radius=10, fg_color="#0e3161", border_width=3, border_color="black", font=("Arial", 24), command=lambda: toggle_sidebar())
hamburger_button.grid(row=0, column=0, padx=20, pady=30)
hamburger_button.configure(new_saved_mainframe_color)

Title_Spot = customtkinter.CTkLabel(sidebar, text="Storage Options", text_color=saved_font_color, font=("Segoe UI", 28, "bold"), height=60)
Title_Spot.grid(row=0, column=0, padx=30, pady=10, sticky="nsew")

Passwords_button = customtkinter.CTkButton(sidebar, text="Passwords🔒", text_color=saved_font_color, width=150, height=20, corner_radius=5, fg_color="#282929", border_width=3, border_color="#bbbdbf", command=lambda: open_passwordMaker_page())
Passwords_button.grid(row=1, column=0, padx=30, pady=10, sticky="nsew")

Notes_button = customtkinter.CTkButton(sidebar, text="Notes📝", text_color=saved_font_color, width=150, height=20, corner_radius=5, fg_color="#282929", border_width=3, border_color="#bbbdbf", command=lambda: open_Notes_page())
Notes_button.grid(row=2, column=0, padx=30, pady=10, sticky="nsew")

Banking_button = customtkinter.CTkButton(sidebar, text="Banking Cards💳", text_color=saved_font_color , width=150, height=20, corner_radius=5, fg_color="#282929", border_width=3, border_color="#bbbdbf", command=lambda: open_banking_cards_page())
Banking_button.grid(row=3, column=0, padx=30, pady=10, sticky="nsew")

Network_button = customtkinter.CTkButton(sidebar, text="Network 🛜", width=150, height=20, corner_radius=5, text_color=saved_font_color , fg_color="#282929", border_width=3, border_color="#bbbdbf", command=lambda: open_Network_page())
Network_button.grid(row=4, column=0, padx=30, pady=20, sticky="nsew")

script_dir = Path(__file__).parent
project_root = script_dir.parent
image_path = project_root / "images" / "Vaulture.png"
vulture_image = customtkinter.CTkImage(Image.open(image_path), size=(200, 200))
vulture_label = customtkinter.CTkLabel(sidebar, text="", image=vulture_image)
vulture_label.grid(row=5, column=0, padx=30, sticky="nsew")

# Assigning weights so that these buttons wont go offscreen
sidebar.rowconfigure(0, weight=2)
sidebar.rowconfigure(1, weight=2)
sidebar.rowconfigure(2, weight=2)
sidebar.rowconfigure(3, weight=2)
sidebar.rowconfigure(4, weight=2)
sidebar.rowconfigure(5, weight=2)
sidebar.rowconfigure(6, weight=2)

# Bottom bar buttons
ValtureP_button = customtkinter.CTkButton(bottom_bar, text="Home 🏠", text_color=saved_font_color, width=60, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray", command=lambda: go_to_home_page())
ValtureP_button.grid(row=0, column=0, pady=30)

# Function to go to home page
def go_to_home_page():
    if 'PasswordMaking_Frame' in globals() and PasswordMaking_Frame.winfo_exists():
        PasswordMaking_Frame.grid_forget()
    if 'Notes_Frame' in globals() and Notes_Frame.winfo_exists():
        Notes_Frame.grid_forget()
    if 'Banking_Cards_Frame' in globals() and Banking_Cards_Frame.winfo_exists():
        Banking_Cards_Frame.grid_forget()
    if 'Network_Frame' in globals() and Network_Frame.winfo_exists():
        Network_Frame.grid_forget()
    if 'MainPasswords_Frame' in globals() and MainPasswords_Frame.winfo_exists():
        MainPasswords_Frame.grid_forget()
    if 'MainNotes_Frame' in globals() and MainNotes_Frame.winfo_exists():
        MainNotes_Frame.grid_forget()
    if 'MainArchive_Frame' in globals() and MainArchive_Frame.winfo_exists():
        MainArchive_Frame.grid_forget()
    if 'Profile_Frame' in globals() and Profile_Frame.winfo_exists():
        Profile_Frame.grid_forget()
    main_frame.grid(row=1, column=1, sticky="nsew")

ValtureP_button = customtkinter.CTkButton(bottom_bar, text="Passwords 🐦", text_color=saved_font_color, width=60, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_passwords_page())
ValtureP_button.grid(row=0, column=1, pady=30)

# Passwords Page
def open_passwords_page():
    global MainPasswords_Frame, searching, entries_container
    if "MainPasswords_Frame" in globals() and MainPasswords_Frame.winfo_exists():
        MainPasswords_Frame.destroy()

    new_saved_mainframe_color = load_saved_mainframe_color()
    MainPasswords_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    MainPasswords_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
    PasswordBorder_Frame = customtkinter.CTkFrame(MainPasswords_Frame, fg_color=new_saved_mainframe_color)
    PasswordBorder_Frame.pack(fill="both", expand=True, padx=5, pady=5)

    label = customtkinter.CTkLabel(PasswordBorder_Frame, text="Passwords", font=("Verdana", 20), text_color=saved_font_color)
    label.pack(pady=20)

    controls_container = customtkinter.CTkFrame(PasswordBorder_Frame, fg_color=new_saved_mainframe_color)
    controls_container.pack(side="top", fill="x", padx=5, pady=5)

    scroll_frame = customtkinter.CTkScrollableFrame(PasswordBorder_Frame, fg_color=new_saved_mainframe_color)
    scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
    PasswordBorder_Frame = scroll_frame

    entries_container = customtkinter.CTkFrame(scroll_frame, fg_color=new_saved_mainframe_color)
    entries_container.pack(fill="both", expand=True, padx=5, pady=5)
    
    passwords_hamburger = customtkinter.CTkButton(MainPasswords_Frame, text="☰", width=60, height=60, corner_radius=10, fg_color=new_saved_mainframe_color, border_width=3, border_color="black", font=("Arial", 24), command=lambda: toggle_sidebar())
    passwords_hamburger.place(x=10, y=10) 

    search_frame = customtkinter.CTkFrame(controls_container, fg_color=new_saved_mainframe_color, height=50, width=480)
    search_frame.pack(pady=10)
    searching = customtkinter.CTkEntry(search_frame, placeholder_text="Search here...", width=450)
    searching.pack(pady=10)
    searching.bind("<KeyRelease>", search)

    back_button = customtkinter.CTkButton(PasswordBorder_Frame, text="Back", text_color=saved_font_color, command=close_passwords_page)
    back_button.pack(pady=20)

    main_frame.grid_forget()
    MainPasswords_Frame.grid(row=1, column=1, sticky="nsew")

    mycursor.execute("SELECT data_id, Title, Username, Email, Password FROM Account_Data_Password WHERE AccountID = %s", (account_id,))
    data = mycursor.fetchall()

    mycursor.execute("SELECT data_id, Card_Title, Card_Number, Expire_Date, CVV FROM Banking_Card WHERE AccountID = %s", (account_id,))
    banking_data = mycursor.fetchall()

    mycursor.execute("SELECT data_id, Network_Title, Network, IP_Address, Password FROM Network_Data WHERE AccountID = %s", (account_id,))
    network_data = mycursor.fetchall()

    if data:
        for index, row in enumerate(data):
            data_id, title, username, email, password_val = row
            entry_frame = customtkinter.CTkFrame(entries_container, fg_color=new_saved_mainframe_color)
            entry_frame.pack(fill="x", padx=10, pady=5)
            entry_label = customtkinter.CTkLabel(entry_frame,
                                                 text=f"{index + 1}. Title: {title} | Username: {username} | Email: {email} | Password: {password_val}",
                                                 anchor="w", justify="left", font=("Courier", 14), text_color=saved_font_color)
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))
            archive_button = customtkinter.CTkButton(entry_frame, text="Archive", width=60,
                                                  command=lambda d=data_id, frame=entry_frame: archive_row(d, frame))
            archive_button.pack(side="left", padx=5)
            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red",
                                                    command=lambda d=data_id, frame=entry_frame: delete_row(d, frame))
            delete_button.pack(side="left", padx=5)
            edit_button = customtkinter.CTkButton(entry_frame, text="Edit", width=60,
                                                  command=lambda d=data_id: edit_password_entry(d))
            edit_button.pack(side="left", padx=5)
    else:
        no_data_label = customtkinter.CTkLabel(PasswordBorder_Frame, text="No password and account data found.", text_color=saved_font_color)
        no_data_label.pack()

    if banking_data:
        for index, row in enumerate(banking_data, start=len(data) + 1):
            data_id, card_name, card_number, expiry_date, cvv = row
            entry_frame = customtkinter.CTkFrame(entries_container, fg_color=new_saved_mainframe_color)
            entry_frame.pack(fill="x", padx=10, pady=5)
            entry_label = customtkinter.CTkLabel(entry_frame, text=f"{index}. Card Name: {card_name} | Card Number: {card_number} | Expiry: {expiry_date} | CVV: {cvv}", anchor="w", justify="left", font=("Courier", 14), text_color=saved_font_color)
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))
            archive_button = customtkinter.CTkButton(entry_frame, text="Archive", width=60, command=lambda d=data_id, frame=entry_frame: archive_banking_row(d, frame))
            archive_button.pack(side="left", padx=5)
            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame=entry_frame: delete_banking_row(d, frame))
            delete_button.pack(side="left", padx=5)
            edit_button = customtkinter.CTkButton(entry_frame, text="Edit", width=60, command=lambda d=data_id: edit_banking_entry(d))
            edit_button.pack(side="left", padx=5)
    else:
        no_data_label = customtkinter.CTkLabel(PasswordBorder_Frame, text="No banking card data found.", text_color=saved_font_color)
        no_data_label.pack()

    if network_data:
        for index, row in enumerate(network_data, start=len(banking_data) + 1):
            data_id, network_name, network_type, ip_address, password_val = row
            entry_frame = customtkinter.CTkFrame(entries_container, fg_color=new_saved_mainframe_color)
            entry_frame.pack(fill="x", padx=10, pady=5)
            entry_label = customtkinter.CTkLabel(entry_frame, text=f"{index}. Network Name: {network_name} | Network Type: {network_type} | IP Address: {ip_address} | Network Password: {password_val}", anchor="w", justify="left", font=("Courier", 14), text_color=saved_font_color)
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))
            archive_button = customtkinter.CTkButton(entry_frame, text="Archive", width=60, command=lambda d=data_id, frame=entry_frame: archive_network_row(d, frame))
            archive_button.pack(side="left", padx=5)
            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame=entry_frame: delete_network_row(d, frame))
            delete_button.pack(side="left", padx=5)
    else:
        no_data_label = customtkinter.CTkLabel(PasswordBorder_Frame, text="No network data found.", text_color=saved_font_color)
        no_data_label.pack()
###############################################################################################################################################################################################################################################################################################################
#AI -Generated Code: Function for edit
def delete_row(data_id, destroyed_frame):
    mycursor.execute("SELECT * FROM Account_Data_Password WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        mycursor.execute("""INSERT INTO Deleted_Passwords (data_id, AccountID, Title, Username, Email, Password) VALUES (%s, %s, %s, %s, %s, %s)""", row)
        mycursor.execute("DELETE FROM Account_Data_Password WHERE data_id = %s", (data_id,))
        login_database.commit()
        destroyed_frame.destroy()

def archive_row(data_id, destroyed_frame):
    mycursor.execute("SELECT data_id, AccountID, Title, Username, Email, Password FROM Account_Data_Password WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        mycursor.execute("""INSERT INTO Archive_Data_Password (data_id, AccountID, Title, Username, Email, Password) VALUES (%s, %s, %s, %s, %s, %s)""", row)
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
    mycursor.execute("SELECT 1 FROM Archive_Banking_Card WHERE data_id = %s", (data_id,))
    if mycursor.fetchone():
        print(f"Data ID {data_id} is already archived.")
        return
    mycursor.execute("SELECT data_id, AccountID, Card_Title, Card_Number, Expire_Date, CVV FROM Banking_Card WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        mycursor.execute("""INSERT INTO Archive_Banking_Card (data_id, AccountID, Card_Title, Card_Number, Expire_Date, CVV) VALUES (%s, %s, %s, %s, %s, %s)""", row)
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
    mycursor.execute("SELECT 1 FROM Archive_Network_Data WHERE data_id = %s", (data_id,))
    if mycursor.fetchone():
        print(f"Data ID {data_id} is already archived.")
        return
    mycursor.execute("SELECT data_id, AccountID, Network_Title, Network, IP_Address, Password FROM Network_Data WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        mycursor.execute("""INSERT INTO Archive_Network_Data (data_id, AccountID, Network_Title, Network, IP_Address, Password) VALUES (%s, %s, %s, %s, %s, %s)""", row)
        mycursor.execute("DELETE FROM Network_Data WHERE data_id = %s", (data_id,))
        login_database.commit()
        destroyed_frame.destroy()

def delete_notes_row(data_id, destroyed_frame):
    mycursor.execute("SELECT * FROM Notes_Data WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        mycursor.execute("DELETE FROM Notes_Data WHERE data_id = %s", (data_id,))
        login_database.commit()
        destroyed_frame.destroy()

def archive_notes_row(data_id, destroyed_frame):
    mycursor.execute("SELECT data_id, AccountID, Notes_title, Notes_body FROM Notes_Data WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        mycursor.execute("""INSERT INTO Archive_Notes_Data (data_id, AccountID, Notes_title, Notes_body) VALUES (%s, %s, %s, %s)""", row)
        mycursor.execute("DELETE FROM Notes_Data WHERE data_id = %s", (data_id,))
        login_database.commit()
        destroyed_frame.destroy()

def remove_password_row(data_id, destroyed_frame):
    mycursor.execute("SELECT data_id, AccountID, Title, Username, Email, Password FROM Archive_Data_Password WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        mycursor.execute("""INSERT INTO Account_Data_Password (data_id, AccountID, Title, Username, Email, Password) VALUES (%s, %s, %s, %s, %s, %s)""", row)
        mycursor.execute("DELETE FROM Archive_Data_Password WHERE data_id = %s", (data_id,))
        login_database.commit()
        destroyed_frame.destroy()

def remove_banking_row(data_id, destroyed_frame):
    mycursor.execute("SELECT data_id, AccountID, Card_Title, Card_Number, Expire_Date, CVV FROM Archive_Banking_Card WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        mycursor.execute("""INSERT INTO Banking_Card (data_id, AccountID, Card_Title, Card_Number, Expire_Date, CVV) VALUES (%s, %s, %s, %s, %s, %s)""", row)
        mycursor.execute("DELETE FROM Archive_Banking_Card WHERE data_id = %s", (data_id,))
        login_database.commit()
        destroyed_frame.destroy()

def remove_network_row(data_id, destroyed_frame):
    mycursor.execute("SELECT data_id, AccountID, Network_Title, Network, IP_Address, Password FROM Archive_Network_Data WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        mycursor.execute("""INSERT INTO Network_Data (data_id, AccountID, Network_Title, Network, IP_Address, Password) VALUES (%s, %s, %s, %s, %s, %s)""", row)
        mycursor.execute("DELETE FROM Archive_Network_Data WHERE data_id = %s", (data_id,))
        login_database.commit()
        destroyed_frame.destroy()

def remove_notes_row(data_id, destroyed_frame):
    mycursor.execute("SELECT data_id, AccountID, Notes_title, Notes_body FROM Archive_Notes_Data WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        mycursor.execute("""INSERT INTO Notes_Data (data_id, AccountID, Notes_title, Notes_body) VALUES (%s, %s, %s, %s)""", row)
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

def search(event):
    query = searching.get().lower().strip()
    print("Search query:", query)

    for widget in entries_container.winfo_children():
        widget.destroy()

    mycursor.execute("SELECT data_id, Title, Username, Email, Password FROM Account_Data_Password WHERE AccountID = %s", (account_id,))
    password_data = mycursor.fetchall()

    mycursor.execute("SELECT data_id, Card_Title, Card_Number, Expire_Date, CVV FROM Banking_Card WHERE AccountID = %s", (account_id,))
    banking_data = mycursor.fetchall()

    mycursor.execute("SELECT data_id, Network_Title, Network, IP_Address, Password FROM Network_Data WHERE AccountID = %s", (account_id,))
    network_data = mycursor.fetchall()

    if query == "":
        for index, row in enumerate(password_data):
            data_id, title, username, email, password_val = row
            entry_frame = customtkinter.CTkFrame(entries_container, fg_color=new_saved_mainframe_color)
            entry_frame.pack(fill="x", padx=10, pady=5)
            entry_label = customtkinter.CTkLabel(
                entry_frame,
                text=f"{index + 1}. Title: {title} | Username: {username} | Email: {email} | Password: {password_val}",
                anchor="w", justify="left", font=("Courier", 14), text_color=saved_font_color
            )
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))
            archive_button = customtkinter.CTkButton(entry_frame, text="Archive", width=60, command=lambda d=data_id, frame=entry_frame: archive_row(d, frame))
            archive_button.pack(side="left", padx=5)
            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame=entry_frame: delete_row(d, frame))
            delete_button.pack(side="left", padx=5)
            edit_button = customtkinter.CTkButton(entry_frame, text="Edit", width=60, command=lambda d=data_id: edit_password_entry(d))
            edit_button.pack(side="left", padx=5)
        for index, row in enumerate(banking_data):
            data_id, card_name, card_number, expiry_date, cvv = row
            entry_frame = customtkinter.CTkFrame(entries_container, fg_color=new_saved_mainframe_color)
            entry_frame.pack(fill="x", padx=10, pady=5)
            entry_label = customtkinter.CTkLabel(
                entry_frame,
                text=f"{index}. Card Name: {card_name} | Card Number: {card_number} | Expiry: {expiry_date} | CVV: {cvv}",
                anchor="w", justify="left", font=("Courier", 14), text_color=saved_font_color
            )
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))
            archive_button = customtkinter.CTkButton(entry_frame, text="Archive", width=60, command=lambda d=data_id, frame=entry_frame: archive_banking_row(d, frame))
            archive_button.pack(side="left", padx=5)
            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame=entry_frame: delete_banking_row(d, frame))
            delete_button.pack(side="left", padx=5)
            edit_button = customtkinter.CTkButton(entry_frame, text="Edit", width=60, command=lambda d=data_id: edit_banking_entry(d))
            edit_button.pack(side="left", padx=5)
        for index, row in enumerate(network_data):
            data_id, network_name, network_type, ip_address, password_val = row
            entry_frame = customtkinter.CTkFrame(entries_container, fg_color=new_saved_mainframe_color)
            entry_frame.pack(fill="x", padx=10, pady=5)
            entry_label = customtkinter.CTkLabel(
                entry_frame,
                text=f"{index}. Network Name: {network_name} | Network Type: {network_type} | IP Address: {ip_address} | Network Password: {password_val}",
                anchor="w", justify="left", font=("Courier", 14), text_color=saved_font_color
            )
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))
            archive_button = customtkinter.CTkButton(entry_frame, text="Archive", width=60, command=lambda d=data_id, frame=entry_frame: archive_network_row(d, frame))
            archive_button.pack(side="left", padx=5)
            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame=entry_frame: delete_network_row(d, frame))
            delete_button.pack(side="left", padx=5)
    else:
        for index, row in enumerate(password_data):
            data_id, title, username, email, password_val = row
            display_text = f"{index + 1}. Title: {title} | Username: {username} | Email: {email} | Password: {password_val}"
            if query in display_text.lower():
                entry_frame = customtkinter.CTkFrame(entries_container, fg_color=new_saved_mainframe_color)
                entry_frame.pack(fill="x", padx=10, pady=5)
                entry_label = customtkinter.CTkLabel(entry_frame, text=display_text, anchor="w", justify="left", font=("Courier", 14), text_color=saved_font_color)
                entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))
                archive_button = customtkinter.CTkButton(entry_frame, text="Archive", width=60, command=lambda d=data_id, frame=entry_frame: archive_row(d, frame))
                archive_button.pack(side="left", padx=5)
                delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame=entry_frame: delete_row(d, frame))
                delete_button.pack(side="left", padx=5)
                edit_button = customtkinter.CTkButton(entry_frame, text="Edit", width=60, command=lambda d=data_id: edit_password_entry(d))
                edit_button.pack(side="left", padx=5)
        for index, row in enumerate(banking_data):
            data_id, card_name, card_number, expiry_date, cvv = row
            display_text_banking = f"{index}. Card Name: {card_name} | Card Number: {card_number} | Expiry: {expiry_date} | CVV: {cvv}"
            if query in display_text_banking.lower():
                entry_frame = customtkinter.CTkFrame(entries_container, fg_color=new_saved_mainframe_color)
                entry_frame.pack(fill="x", padx=10, pady=5)
                entry_label = customtkinter.CTkLabel(entry_frame, text=display_text_banking, anchor="w", justify="left", font=("Courier", 14), text_color=saved_font_color)
                entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))
                archive_button = customtkinter.CTkButton(entry_frame, text="Archive", width=60, command=lambda d=data_id, frame=entry_frame: archive_banking_row(d, frame))
                archive_button.pack(side="left", padx=5)
                delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame=entry_frame: delete_banking_row(d, frame))
                delete_button.pack(side="left", padx=5)
                edit_button = customtkinter.CTkButton(entry_frame, text="Edit", width=60, command=lambda d=data_id: edit_banking_entry(d))
                edit_button.pack(side="left", padx=5)
        for index, row in enumerate(network_data):
            data_id, network_name, network_type, ip_address, password_val = row
            display_text_network = f"{index}. Network Name: {network_name} | Network Type: {network_type} | IP Address: {ip_address} | Network Password: {password_val}"
            if query in display_text_network.lower():
                entry_frame = customtkinter.CTkFrame(entries_container, fg_color=new_saved_mainframe_color)
                entry_frame.pack(fill="x", padx=10, pady=5)
                entry_label = customtkinter.CTkLabel(entry_frame, text=display_text_network, anchor="w", justify="left", font=("Courier", 14), text_color=saved_font_color)
                entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))
                archive_button = customtkinter.CTkButton(entry_frame, text="Archive", width=60, command=lambda d=data_id, frame=entry_frame: archive_network_row(d, frame))
                archive_button.pack(side="left", padx=5)
                delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame=entry_frame: delete_network_row(d, frame))
                delete_button.pack(side="left", padx=5)

def close_passwords_page():
    MainPasswords_Frame.destroy()
    main_frame.grid(row=1, column=1, sticky="nsew")
## AI-Generated Code: Function for edit close
###################################################################################################################################################################################################################################################################################
# Notes button in bottom bar
Notes_button = customtkinter.CTkButton(bottom_bar, text="Notes 📝", text_color=saved_font_color, width=60, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_Notes_page())
Notes_button.grid(row=0, column=2, pady=30)

# Notes Page
def open_Notes_page():
    global MainNotes_Frame, searching, entries_container
    if "MainNotes_Frame" in globals() and MainNotes_Frame.winfo_exists():
        MainNotes_Frame.destroy()

    new_saved_mainframe_color = load_saved_mainframe_color()
    MainNotes_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    MainNotes_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

    NotesBorder_Frame = customtkinter.CTkFrame(MainNotes_Frame, fg_color=new_saved_mainframe_color)
    NotesBorder_Frame.pack(fill="both", expand=True, padx=5, pady=5)

    label = customtkinter.CTkLabel(NotesBorder_Frame, text="Notes List", font=("Verdana", 20), text_color=saved_font_color)
    label.pack(pady=20)

    controls_container = customtkinter.CTkFrame(NotesBorder_Frame, fg_color=new_saved_mainframe_color)
    controls_container.pack(side="top", fill="x", padx=5, pady=5)

    scroll_frame = customtkinter.CTkScrollableFrame(NotesBorder_Frame, fg_color=new_saved_mainframe_color)
    scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
    NotesBorder_Frame = scroll_frame

    entries_container = customtkinter.CTkFrame(scroll_frame, fg_color=new_saved_mainframe_color)
    entries_container.pack(fill="both", expand=True, padx=5, pady=5)

    search_frame = customtkinter.CTkFrame(controls_container, fg_color=new_saved_mainframe_color, height=50, width=480)
    search_frame.pack(pady=10)
    searching = customtkinter.CTkEntry(search_frame, placeholder_text="Search here...", width=450)
    searching.pack(pady=10)
    searching.bind("<KeyRelease>", search_notes)

    passwords_hamburger = customtkinter.CTkButton(MainNotes_Frame, text="☰", width=60, height=60, corner_radius=10, fg_color=new_saved_mainframe_color, border_width=3, border_color="black", font=("Arial", 24), command=lambda: toggle_sidebar())
    passwords_hamburger.place(x=10, y=10) 

    back_button = customtkinter.CTkButton(NotesBorder_Frame, text="Back", text_color=saved_font_color, command=close_Notes_page)
    back_button.pack(pady=20)

    mycursor.execute("SELECT data_id, Notes_title, Notes_body FROM Notes_Data WHERE AccountID = %s", (account_id,))
    notes_data = mycursor.fetchall()

    if notes_data:
        for index, row in enumerate(notes_data):
            data_id, notes_title, notes_body = row
            entry_frame = customtkinter.CTkFrame(entries_container, fg_color=new_saved_mainframe_color)
            entry_frame.pack(fill="x", padx=10, pady=5)
            entry_label = customtkinter.CTkLabel(entry_frame, text=f"{index}. Notes Title: {notes_title} | Notes Body: {notes_body}", anchor="w", justify="left", font=("Courier", 14), text_color=saved_font_color)
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))
            archive_button = customtkinter.CTkButton(entry_frame, text="Archive", width=60, command=lambda d=data_id, frame=entry_frame: archive_notes_row(d, frame))
            archive_button.pack(side="left", padx=5)
            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame=entry_frame: delete_notes_row(d, frame))
            delete_button.pack(side="left", padx=5)
            edit_button = customtkinter.CTkButton(entry_frame, text="Edit", width=60, command=lambda d=data_id: edit_notes_entry(d))
            edit_button.pack(side="left", padx=5)
    else:
        no_data_label = customtkinter.CTkLabel(NotesBorder_Frame, text="No notes data found.",  text_color=saved_font_color)
        no_data_label.pack()

def archive_notes_row(data_id, destroyed_frame):
    mycursor.execute("SELECT data_id, AccountID, Notes_title, Notes_body FROM Notes_Data WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        mycursor.execute("""INSERT INTO Archive_Notes_Data (data_id, AccountID, Notes_title, Notes_body) VALUES (%s, %s, %s, %s)""", row)
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

def search_notes(event):
    query = searching.get().lower().strip()
    print("Search query:", query)
    for widget in entries_container.winfo_children():
        widget.destroy()
    mycursor.execute("SELECT data_id, Notes_title, Notes_body FROM Notes_Data WHERE AccountID = %s", (account_id,))
    notes_data = mycursor.fetchall()
    if query == "":
        for index, row in enumerate(notes_data):
            data_id, notes_title, notes_body = row
            entry_frame = customtkinter.CTkFrame(entries_container, fg_color=new_saved_mainframe_color)
            entry_frame.pack(fill="x", padx=10, pady=5)
            entry_label = customtkinter.CTkLabel(entry_frame, text=f"{index}. Notes Title: {notes_title} | Notes Body: {notes_body}", anchor="w", justify="left", font=("Courier", 14), text_color=saved_font_color)
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))
            archive_button = customtkinter.CTkButton(entry_frame, text="Archive", width=60, command=lambda d=data_id, frame=entry_frame: archive_notes_row(d, frame))
            archive_button.pack(side="left", padx=5)
            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame=entry_frame: delete_notes_row(d, frame))
            delete_button.pack(side="left", padx=5)
            edit_button = customtkinter.CTkButton(entry_frame, text="Edit", width=60, command=lambda d=data_id: edit_notes_entry(d))
            edit_button.pack(side="left", padx=5)
    else:
        for index, row in enumerate(notes_data):
            data_id, notes_title, notes_body = row
            display_text_notes = f"{index}. Notes Title: {notes_title} | Notes Body: {notes_body}"
            if query in display_text_notes.lower():
                entry_frame = customtkinter.CTkFrame(entries_container, fg_color=new_saved_mainframe_color)
                entry_frame.pack(fill="x", padx=10, pady=5)
                entry_label = customtkinter.CTkLabel(entry_frame, text=display_text_notes, anchor="w", justify="left", font=("Courier", 14), text_color=saved_font_color)
                entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))
                archive_button = customtkinter.CTkButton(entry_frame, text="Archive", width=60, command=lambda d=data_id, frame=entry_frame: archive_notes_row(d, frame))
                archive_button.pack(side="left", padx=5)
                delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame=entry_frame: delete_notes_row(d, frame))
                delete_button.pack(side="left", padx=5)
                edit_button = customtkinter.CTkButton(entry_frame, text="Edit", width=60, command=lambda d=data_id: edit_notes_entry(d))
                edit_button.pack(side="left", padx=5)

def close_Notes_page():
    MainNotes_Frame.destroy()
    main_frame.grid(row=1, column=1, sticky="nsew")

Archive_button = customtkinter.CTkButton(bottom_bar, text="Archive 📦", text_color=saved_font_color, width=60, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_archive_page())
Archive_button.grid(row=0, column=3, pady=30)

def open_archive_page():
    global MainArchive_Frame, searching, entries_container
    if "MainArchive_Frame" in globals() and MainArchive_Frame.winfo_exists():
        MainArchive_Frame.destroy()
    new_saved_mainframe_color = load_saved_mainframe_color()
    MainArchive_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    MainArchive_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
    ArchiveBorder_Frame = customtkinter.CTkFrame(MainArchive_Frame, fg_color=new_saved_mainframe_color)
    ArchiveBorder_Frame.pack(fill="both", expand=True, padx=5, pady=5)
    scroll_frame = customtkinter.CTkScrollableFrame(ArchiveBorder_Frame, fg_color=new_saved_mainframe_color)
    scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
    ArchiveBorder_Frame = scroll_frame
    label = customtkinter.CTkLabel(ArchiveBorder_Frame, text="Archived Passwords", font=("Verdana", 20), text_color=saved_font_color)
    label.pack(pady=20)
    controls_container = customtkinter.CTkFrame(ArchiveBorder_Frame, fg_color=new_saved_mainframe_color)
    controls_container.pack(side="top", fill="x", padx=5, pady=5)
    entries_container = customtkinter.CTkFrame(scroll_frame, fg_color=new_saved_mainframe_color)
    entries_container.pack(fill="both", expand=True, padx=5, pady=5)
    search_frame = customtkinter.CTkFrame(controls_container, fg_color=new_saved_mainframe_color, height=50, width=480)
    search_frame.pack(pady=10)
    searching = customtkinter.CTkEntry(search_frame, placeholder_text="Search here...", width=450)
    searching.pack(pady=10)
    searching.bind("<KeyRelease>", search_archive)
    passwords_hamburger = customtkinter.CTkButton(MainArchive_Frame, text="☰", width=60, height=60, corner_radius=10, fg_color=new_saved_mainframe_color, border_width=3, border_color="black", font=("Arial", 24), command=lambda: toggle_sidebar())
    passwords_hamburger.place(x=10, y=10)
    mycursor.execute("SELECT data_id, Title, Username, Email, Password FROM Archive_Data_Password WHERE AccountID = %s", (account_id,))
    data = mycursor.fetchall()
    if data:
        for index, row in enumerate(data):
            data_id, title, username, email, password_val = row
            entry_frame = customtkinter.CTkFrame(entries_container, fg_color=new_saved_mainframe_color)
            entry_frame.pack(fill="x", padx=10, pady=5)
            entry_label = customtkinter.CTkLabel(entry_frame, text=f"{index + 1}. Title: {title} | Username: {username} | Email: {email} | Password: {password_val}", anchor="w", justify="left", font=("Courier", 14), text_color=saved_font_color)
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))
            archive_button = customtkinter.CTkButton(entry_frame, text="Remove", width=60, command=lambda d=data_id, frame=entry_frame: remove_password_row(d, frame))
            archive_button.pack(side="left", padx=5)
            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame=entry_frame: delete_archive_password_row(d, frame))
            delete_button.pack(side="left", padx=5)
    else:
        no_data_label = customtkinter.CTkLabel(ArchiveBorder_Frame, text="No password and account data found.", text_color=saved_font_color)
        no_data_label.pack()
    mycursor.execute("SELECT data_id, Card_Title, Card_Number, Expire_Date, CVV FROM Archive_Banking_Card WHERE AccountID = %s", (account_id,))
    banking_data = mycursor.fetchall()
    if banking_data:
        for index, row in enumerate(banking_data, start=len(data) + 1):
            data_id, card_name, card_number, expiry_date, cvv = row
            entry_frame = customtkinter.CTkFrame(entries_container, fg_color=new_saved_mainframe_color)
            entry_frame.pack(fill="x", padx=10, pady=5)
            entry_label = customtkinter.CTkLabel(entry_frame, text=f"{index}. Card Name: {card_name} | Card Number: {card_number} | Expiry: {expiry_date} | CVV: {cvv}", anchor="w", justify="left", font=("Courier", 14), text_color=saved_font_color)
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))
            archive_button = customtkinter.CTkButton(entry_frame, text="Remove", width=60, command=lambda d=data_id, frame=entry_frame: remove_banking_row(d, frame))
            archive_button.pack(side="left", padx=5)
            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame=entry_frame: delete_archive_banking_row(d, frame))
            delete_button.pack(side="left", padx=5)
    else:
        no_data_label = customtkinter.CTkLabel(ArchiveBorder_Frame, text="No banking card data found.", text_color=saved_font_color)
        no_data_label.pack()
    mycursor.execute("SELECT data_id, Network_Title, Network, IP_Address, Password FROM Archive_Network_Data WHERE AccountID = %s", (account_id,))
    network_data = mycursor.fetchall()
    if network_data:
        for index, row in enumerate(network_data, start=len(banking_data) + 1):
            data_id, network_name, network_type, ip_address, password_val = row
            entry_frame = customtkinter.CTkFrame(entries_container, fg_color=new_saved_mainframe_color)
            entry_frame.pack(fill="x", padx=10, pady=5)
            entry_label = customtkinter.CTkLabel(entry_frame, text=f"{index}. Network Name: {network_name} | Network Type: {network_type} | IP Address: {ip_address} | Network Password: {password_val}", anchor="w", justify="left", font=("Courier", 14), text_color=saved_font_color)
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))
            archive_button = customtkinter.CTkButton(entry_frame, text="Remove", width=60, command=lambda d=data_id, frame=entry_frame: remove_network_row(d, frame))
            archive_button.pack(side="left", padx=5)
            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame=entry_frame: delete_archive_network_row(d, frame))
            delete_button.pack(side="left", padx=5)
    else:
        no_data_label = customtkinter.CTkLabel(ArchiveBorder_Frame, text="No network data found.", text_color=saved_font_color)
        no_data_label.pack()
    mycursor.execute("SELECT data_id, Notes_title, Notes_body FROM Archive_Notes_Data WHERE AccountID = %s", (account_id,))
    notes_data = mycursor.fetchall()
    if notes_data:
        for index, row in enumerate(notes_data, start=len(network_data) + 1):
            data_id, notes_title, notes_body = row
            entry_frame = customtkinter.CTkFrame(entries_container, fg_color=new_saved_mainframe_color)
            entry_frame.pack(fill="x", padx=10, pady=5)
            entry_label = customtkinter.CTkLabel(entry_frame, text=f"{index}. Notes Title: {notes_title} | Notes Body: {notes_body}", anchor="w", justify="left", font=("Courier", 14), text_color=saved_font_color)
            entry_label.pack(side="left", fill="x", expand=True, padx=(0, 10))
            archive_button = customtkinter.CTkButton(entry_frame, text="Remove", width=60, command=lambda d=data_id, frame=entry_frame: remove_notes_row(d, frame))
            archive_button.pack(side="left", padx=5)
            delete_button = customtkinter.CTkButton(entry_frame, text="Delete", width=60, fg_color="red", command=lambda d=data_id, frame=entry_frame: delete_archive_notes_row(d, frame))
            delete_button.pack(side="left", padx=5)
    else:
        no_data_label = customtkinter.CTkLabel(ArchiveBorder_Frame, text="No notes data found.", text_color=saved_font_color)
        no_data_label.pack()
    back_button = customtkinter.CTkButton(controls_container, text="Back", text_color=saved_font_color, command=close_archive_page)
    back_button.pack(pady=10)
    main_frame.grid_forget()
    MainArchive_Frame.grid(row=1, column=1, sticky="nsew")

def close_archive_page():
    MainArchive_Frame.destroy()
    main_frame.grid(row=1, column=1, sticky="nsew")

# Profile button in bottom bar
Profile_button = customtkinter.CTkButton(bottom_bar, text="Profile 👥", text_color=saved_font_color, width=60, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_Profile_Page())
Profile_button.grid(row=0, column=4, pady=5)

def open_Profile_Page():
    window.minsize(800, 600)
    window.maxsize(1920, 1080)
    global Profile_Frame, Border_Frame, Profile_Name, PImage_label
    if "Profile_Frame" not in globals():
        new_saved_mainframe_color = load_saved_mainframe_color()
        Profile_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
        Profile_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
        Profile_Border_Frame = customtkinter.CTkFrame(Profile_Frame, fg_color=new_saved_mainframe_color)
        Profile_Border_Frame.pack(fill="both", expand=True, padx=5, pady=5)
        scroll_frame = customtkinter.CTkScrollableFrame(Profile_Border_Frame, fg_color=new_saved_mainframe_color)
        scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
        Profile_Border_Frame = scroll_frame
        label = customtkinter.CTkLabel(Profile_Border_Frame, text="Profile Page", font=("Verdana", 30), text_color=saved_font_color)
        label.pack(pady=20)
        passwords_hamburger = customtkinter.CTkButton(Profile_Frame, text="☰", width=60, height=60, corner_radius=10, fg_color=new_saved_mainframe_color, border_width=3, border_color="black", font=("Arial", 24), command=lambda: toggle_sidebar())
        passwords_hamburger.place(x=10, y=10)
        PImage_label = customtkinter.CTkLabel(Profile_Border_Frame, text="Please put a picture!", width=300, height=300, text_color="white", fg_color="black")
        PImage_label.pack(pady=10)
        UploadingI = customtkinter.CTkButton(Profile_Border_Frame, text="Upload Image", text_color=saved_font_color, command=upload_profile_image)
        UploadingI.pack(pady=30)
        Profile_Name = customtkinter.StringVar()
        name_entry = customtkinter.CTkEntry(Profile_Border_Frame, textvariable=Profile_Name, width=250, placeholder_text="Enter your name")
        name_entry.pack(pady=20)
        Save_button = customtkinter.CTkButton(Profile_Border_Frame, text="Save Name", text_color=saved_font_color, command=save_profile_name)
        Save_button.pack(pady=5)
        back_button = customtkinter.CTkButton(Profile_Border_Frame, text="Back", text_color=saved_font_color, command=close_Profile_Page)
        back_button.pack(pady=20)
    main_frame.grid_forget()
    Profile_Frame.grid(row=1, column=1, sticky="nsew")

def upload_profile_image():
    global profile_image_large, profile_image_small, PImage_label, profile_box_label
    file_path = filedialog.askopenfilename(title="Choosing PFP", filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if file_path:
        img = Image.open(file_path)
        img_large = img.resize((400, 400), Image.LANCZOS)
        profile_image_large = CTkImage(light_image=img_large, dark_image=img_large, size=(400, 400))
        img_small = img.resize((50, 50), Image.Resampling.LANCZOS)
        profile_image_small = CTkImage(light_image=img_small, dark_image=img_small, size=(70, 70))
        PImage_label.configure(image=profile_image_large, text="")
        PImage_label.image = profile_image_large
        profile_box_label.configure(image=profile_image_small, text="")
        profile_box_label.image = profile_image_small

def save_profile_name():
    global Profile_Name
    profile_name = Profile_Name.get()

def close_Profile_Page():
    Profile_Frame.grid_forget()
    main_frame.grid(row=1, column=1, sticky="nsew")

profile_box = customtkinter.CTkFrame(main_frame, fg_color="#282929", border_width=2, border_color="gray", width=50, height=50)
profile_box.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)
profile_box_label = customtkinter.CTkLabel(profile_box, text="")
profile_box_label.pack(expand=True)

def open_settings_page():
    acc2.opening_settings(update_main_theme)

Settings_button = customtkinter.CTkButton(bottom_bar, text="Settings ⚙️", text_color=saved_font_color, width=10, height=70, corner_radius=900, fg_color="#282929", border_width=1, border_color="gray", command=lambda: open_settings_page())
Settings_button.grid(row=0, column=5, pady=5)

bottom_bar.columnconfigure(0, weight=2)
bottom_bar.columnconfigure(1, weight=2)
bottom_bar.columnconfigure(2, weight=1)
bottom_bar.columnconfigure(3, weight=1)
bottom_bar.columnconfigure(4, weight=1)
bottom_bar.columnconfigure(5, weight=1)

def open_passwordMaker_page(*args, **kwargs):
    import string, random
    global PasswordMaking_Frame
    if "PasswordMaking_Frame" in globals() and PasswordMaking_Frame.winfo_exists():
        PasswordMaking_Frame.destroy()
        window.minsize(800, 600)
        window.maxsize(1920, 1080)
    new_saved_mainframe_color = load_saved_mainframe_color()
    PasswordMaking_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    PasswordMaking_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
    PasswordMakingBorder_Frame = customtkinter.CTkFrame(PasswordMaking_Frame, fg_color=new_saved_mainframe_color)
    PasswordMakingBorder_Frame.pack(fill="both", expand=True, padx=5, pady=5)
    scroll_frame = customtkinter.CTkScrollableFrame(PasswordMakingBorder_Frame, fg_color=new_saved_mainframe_color)
    scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
    PasswordMakingBorder_Frame = scroll_frame
    passwords_hamburger = customtkinter.CTkButton(PasswordMaking_Frame, text="☰", width=60, height=60, corner_radius=10, fg_color=new_saved_mainframe_color, border_width=3, border_color="black", font=("Arial", 24), command=lambda: toggle_sidebar())
    passwords_hamburger.place(x=10, y=10)
    label = customtkinter.CTkLabel(PasswordMakingBorder_Frame, text="Password Maker", font=("Verdana", 20), text_color=saved_font_color)
    label.grid(row=0, column=2, pady=(10, 20), sticky="nsew")
    label = customtkinter.CTkLabel(PasswordMakingBorder_Frame, text="Password Title", text_color=saved_font_color)
    label.grid(row=1, column=2, pady=10, sticky="nsew")
    Title_entry = customtkinter.CTkEntry(PasswordMakingBorder_Frame, placeholder_text="Enter Title")
    Title_entry.grid(row=2, column=2, pady=10, padx=10, sticky="nsew")

#New Edit Functions

def edit_password_entry(data_id):
    mycursor.execute("SELECT Title, Username, Email, Password FROM Account_Data_Password WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        title, username, email, password_val = row
        edit_window = customtkinter.CTkToplevel(window)
        edit_window.title("Edit Password Entry")
        title_label = customtkinter.CTkLabel(edit_window, text="Title:")
        title_label.grid(row=0, column=0, padx=10, pady=10)
        title_entry = customtkinter.CTkEntry(edit_window)
        title_entry.insert(0, title)
        title_entry.grid(row=0, column=1, padx=10, pady=10)
        username_label = customtkinter.CTkLabel(edit_window, text="Username:")
        username_label.grid(row=1, column=0, padx=10, pady=10)
        username_entry = customtkinter.CTkEntry(edit_window)
        username_entry.insert(0, username)
        username_entry.grid(row=1, column=1, padx=10, pady=10)
        email_label = customtkinter.CTkLabel(edit_window, text="Email:")
        email_label.grid(row=2, column=0, padx=10, pady=10)
        email_entry = customtkinter.CTkEntry(edit_window)
        email_entry.insert(0, email)
        email_entry.grid(row=2, column=1, padx=10, pady=10)
        password_label = customtkinter.CTkLabel(edit_window, text="Password:")
        password_label.grid(row=3, column=0, padx=10, pady=10)
        password_entry = customtkinter.CTkEntry(edit_window)
        password_entry.insert(0, password_val)
        password_entry.grid(row=3, column=1, padx=10, pady=10)
        def save_password_changes():
            new_title = title_entry.get()
            new_username = username_entry.get()
            new_email = email_entry.get()
            new_password = password_entry.get()
            mycursor.execute("UPDATE Account_Data_Password SET Title = %s, Username = %s, Email = %s, Password = %s WHERE data_id = %s",
                             (new_title, new_username, new_email, new_password, data_id))
            login_database.commit()
            edit_window.destroy()
            open_passwords_page()
        save_button = customtkinter.CTkButton(edit_window, text="Save", command=save_password_changes)
        save_button.grid(row=4, column=0, columnspan=2, pady=10)

def edit_banking_entry(data_id):
    mycursor.execute("SELECT Card_Title, Card_Number, Expire_Date, CVV FROM Banking_Card WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        card_title, card_number, expire_date, cvv = row
        edit_window = customtkinter.CTkToplevel(window)
        edit_window.title("Edit Banking Entry")
        title_label = customtkinter.CTkLabel(edit_window, text="Card Title:")
        title_label.grid(row=0, column=0, padx=10, pady=10)
        title_entry = customtkinter.CTkEntry(edit_window)
        title_entry.insert(0, card_title)
        title_entry.grid(row=0, column=1, padx=10, pady=10)
        number_label = customtkinter.CTkLabel(edit_window, text="Card Number:")
        number_label.grid(row=1, column=0, padx=10, pady=10)
        number_entry = customtkinter.CTkEntry(edit_window)
        number_entry.insert(0, card_number)
        number_entry.grid(row=1, column=1, padx=10, pady=10)
        expiry_label = customtkinter.CTkLabel(edit_window, text="Expiry Date:")
        expiry_label.grid(row=2, column=0, padx=10, pady=10)
        expiry_entry = customtkinter.CTkEntry(edit_window)
        expiry_entry.insert(0, expire_date)
        expiry_entry.grid(row=2, column=1, padx=10, pady=10)
        cvv_label = customtkinter.CTkLabel(edit_window, text="CVV:")
        cvv_label.grid(row=3, column=0, padx=10, pady=10)
        cvv_entry = customtkinter.CTkEntry(edit_window)
        cvv_entry.insert(0, cvv)
        cvv_entry.grid(row=3, column=1, padx=10, pady=10)
        def save_changes():
            new_title = title_entry.get()
            new_number = number_entry.get()
            new_expiry = expiry_entry.get()
            new_cvv = cvv_entry.get()
            mycursor.execute("UPDATE Banking_Card SET Card_Title = %s, Card_Number = %s, Expire_Date = %s, CVV = %s WHERE data_id = %s", 
                             (new_title, new_number, new_expiry, new_cvv, data_id))
            login_database.commit()
            edit_window.destroy()
            open_passwords_page()
        save_button = customtkinter.CTkButton(edit_window, text="Save", command=save_changes)
        save_button.grid(row=4, column=0, columnspan=2, pady=10)

def edit_notes_entry(data_id):
    mycursor.execute("SELECT Notes_title, Notes_body FROM Notes_Data WHERE data_id = %s", (data_id,))
    row = mycursor.fetchone()
    if row:
        notes_title, notes_body = row
        edit_window = customtkinter.CTkToplevel(window)
        edit_window.title("Edit Note")
        title_label = customtkinter.CTkLabel(edit_window, text="Note Title:")
        title_label.grid(row=0, column=0, padx=10, pady=10)
        title_entry = customtkinter.CTkEntry(edit_window)
        title_entry.insert(0, notes_title)
        title_entry.grid(row=0, column=1, padx=10, pady=10)
        body_label = customtkinter.CTkLabel(edit_window, text="Note Body:")
        body_label.grid(row=1, column=0, padx=10, pady=10)
        body_entry = customtkinter.CTkEntry(edit_window)
        body_entry.insert(0, notes_body)
        body_entry.grid(row=1, column=1, padx=10, pady=10)
        def save_note_changes():
            new_title = title_entry.get()
            new_body = body_entry.get()
            mycursor.execute("UPDATE Notes_Data SET Notes_title = %s, Notes_body = %s WHERE data_id = %s", 
                             (new_title, new_body, data_id))
            login_database.commit()
            edit_window.destroy()
            open_Notes_page()
        save_button = customtkinter.CTkButton(edit_window, text="Save", command=save_note_changes)
        save_button.grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()
