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

window = customtkinter.CTk()
window.title("Vaulture")

# Screen width and height 
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


# Left sidebar 
sidebar = customtkinter.CTkFrame(window, width=200, corner_radius=20, fg_color="#0e3161", border_width=8, border_color="black")
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
bottom_bar = customtkinter.CTkFrame(window, height=90, corner_radius=0, fg_color="#133f61")
bottom_bar.grid(row=2, column=1, columnspan=2, sticky="ew") 

# Sidebar buttons (These will appear when the sidebar is toggled)
# Hamburger Icon
hamburger_button = customtkinter.CTkButton(main_frame, text="☰", width=60, height=60, corner_radius=10, fg_color="#0e3161", border_width=3, border_color="black", font=("Arial", 24), command=lambda: toggle_sidebar())
hamburger_button.grid(row=0, column=0, padx=20, pady=30)

Title_Spot = customtkinter.CTkLabel(sidebar, text="Storage Options", text_color= "White", font=("Segoe UI", 28, "bold"), height=60)
Title_Spot.grid(row=0, column=0, padx=30, pady=10, sticky="nsew")

Passwords_button = customtkinter.CTkButton(sidebar, text="Passwords🔒", width=150, height=20, corner_radius=5, fg_color="#282929", border_width=3, border_color="#bbbdbf", command=lambda: open_passwordMaker_page())
Passwords_button.grid(row=1, column=0, padx=30, pady=10, sticky="nsew")

Notes_button = customtkinter.CTkButton(sidebar, text="Notes📝", width=150, height=20, corner_radius=5, fg_color="#282929", border_width=3, border_color="#bbbdbf", command=lambda: open_notes_page())
Notes_button.grid(row=2, column=0, padx=30, pady=10, sticky="nsew")

Filter4_button = customtkinter.CTkButton(sidebar, text="Banking Cards💳", width=150, height=20, corner_radius=5, fg_color="#282929", border_width=3, border_color="#bbbdbf", command=lambda: open_banking_cards_page())
Filter4_button.grid(row=3, column=0, padx=30, pady=10, sticky="nsew")

Network_button = customtkinter.CTkButton(sidebar, text="Network 🛜", width=150, height=20, corner_radius=5, fg_color="#282929", border_width=3, border_color="#bbbdbf", command=lambda: open_Network_page())
Network_button.grid(row=4, column=0, padx=30, pady=20, sticky="nsew")


script_dir = Path(__file__).parent
project_root = script_dir.parent
image_path = project_root / "images" / "Vaulture.png"
vulture_image = customtkinter.CTkImage(Image.open(image_path), size = (200,200))
vulture_label = customtkinter.CTkLabel(sidebar, text = "", image= vulture_image)
vulture_label.grid(row=5, column=0, padx=30, sticky="nsew")



#Assigning weights so that these buttons wont go offscreen
#Hamburger Button
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
# Passwords
def open_passwords_page():
    global MainPasswords_Frame
    if "MainPasswords_Fram" in globals() and MainPasswords_Frame.winfo_exists():
        MainPasswords_Frame.destroy()

#  The creation of the frame and border
    MainPasswords_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    MainPasswords_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
    PasswordBorder_Frame= customtkinter.CTkFrame(MainPasswords_Frame, fg_color="#A9A9A9")
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

#Closing the page 
def close_passwords_page():
    MainPasswords_Frame.destroy() 
    main_frame.grid(row=1, column=1, sticky="nsew") 


ValtureP_button = customtkinter.CTkButton(bottom_bar, text="Passwords 🐦", width=60, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_passwords_page())
ValtureP_button.grid(row=0, column=0, pady=30)

# Open archive page
def open_archive_page():
    global MainArchive_Frame
    if "MainArchive_Frame" in globals() and MainArchive_Frame.winfo_exists():
        MainArchive_Frame.destroy()

#  The creation of the frame and border
    MainArchive_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    MainArchive_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
    ArchiveBorder_Frame= customtkinter.CTkFrame(MainArchive_Frame, fg_color="#A9A9A9")
    ArchiveBorder_Frame.pack(fill="both", expand=True, padx=5, pady=5)

    label = customtkinter.CTkLabel(ArchiveBorder_Frame, text="Archived Passwords", font=("Verdana", 20))
    label.pack(pady=20)

    scroll_frame = customtkinter.CTkScrollableFrame(ArchiveBorder_Frame, fg_color="#A9A9A9")
    scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
    ArchiveBorder_Frame = scroll_frame 
# Search Bar inside Passwords Page
    search_frame = customtkinter.CTkFrame(ArchiveBorder_Frame, fg_color="#A9A9A9", height=50, width=480)
    search_frame.pack(pady=10)
    searching = customtkinter.CTkEntry(search_frame, placeholder_text="Search here...", width=450)
    searching.pack(pady=10)

    back_button = customtkinter.CTkButton(ArchiveBorder_Frame, text="Back", command=close_archive_page)
    back_button.pack(pady=20)

    main_frame.grid_forget()
    MainArchive_Frame.grid(row=1, column=1, sticky="nsew")

def close_archive_page():
    MainArchive_Frame.destroy()
    main_frame.grid(row=1, column=1, sticky="nsew")

# Profile button in bottom bar
Profile_button = customtkinter.CTkButton(bottom_bar, text="Profile 👥", width=60, height=70, corner_radius=900, fg_color="#282929",border_width=2, border_color="gray", command=lambda: open_Profile_Page())
Profile_button.grid(row=0, column=2, pady=5)

# New Settings Button at Bottom 
def open_settings_page():
    acc2.opening_settings()
    
Archive_button = customtkinter.CTkButton(bottom_bar, text="Archive 📦", width=60, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_archive_page())
Archive_button.grid(row=0, column=1, pady=30,)

Settings_button = customtkinter.CTkButton(bottom_bar, text="Settings ⚙️", width=10, height=70, corner_radius=900, fg_color="#282929", border_width=1, border_color="gray", command=lambda: open_settings_page())
Settings_button.grid(row=0, column=3, pady=5) 


# Bottom Bar Setup
#🐦
bottom_bar.columnconfigure(0, weight=2)    
# 📦
bottom_bar.columnconfigure(1, weight=1)  
# 👥
bottom_bar.columnconfigure(2, weight=1)  
# ⚙️
bottom_bar.columnconfigure(3, weight=1) 

#Left bar stuff
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
    PasswordMakingBorder_Frame= customtkinter.CTkFrame(PasswordMaking_Frame, fg_color="#A9A9A9")
    PasswordMakingBorder_Frame.pack(fill="both", expand=True, padx=5, pady=5)
    scroll_frame = customtkinter.CTkScrollableFrame(PasswordMakingBorder_Frame, fg_color="#A9A9A9")
    scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
    PasswordMakingBorder_Frame = scroll_frame 

    label = customtkinter.CTkLabel(PasswordMakingBorder_Frame, text="Password Maker", font=("Verdana", 20), text_color="black")
    label.grid(row=0, column=2, pady=(10, 20), sticky="n")

    label = customtkinter.CTkLabel(PasswordMakingBorder_Frame, text="Username", text_color="black")
    label.grid(row=1,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkEntry(PasswordMakingBorder_Frame, placeholder_text="Enter 1")
    label.grid(row=2,column=2, pady=10, sticky="ew")
    
    label = customtkinter.CTkLabel(PasswordMakingBorder_Frame, text="Email", text_color="black")
    label.grid(row=3,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkEntry(PasswordMakingBorder_Frame, placeholder_text="Enter 2")
    label.grid(row=4,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkLabel(PasswordMakingBorder_Frame, text="Password", text_color="black")
    label.grid(row=5,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkEntry(PasswordMakingBorder_Frame, placeholder_text="Enter 3")
    label.grid(row=6,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkLabel(PasswordMakingBorder_Frame, text="Password Generation Checklist", text_color="black")
    label.grid(row=7,column=2, pady=10, sticky="ew")
#######################################################################################################################################################
# AI-Assisted Code: Password Generation Feature
# This section was created with the help of ChatGPT to implement, as i accidentally deleted it when trying to delete a different one, i had it changed, the link is provided to the history
# and it will be noted in the report. Any further questions ill be happy to answer 
# https://chatgpt.com/share/67e6ef3a-edf4-800a-8ad2-d5eb1e63c908

    # Create BooleanVars to hold checkbox states for character types
    use_special = customtkinter.BooleanVar(value=False)
    use_numbers = customtkinter.BooleanVar(value=False)
    use_upper = customtkinter.BooleanVar(value=False)
    use_lower = customtkinter.BooleanVar(value=False)

    # Checkboxes for user selection
    customtkinter.CTkCheckBox(PasswordMakingBorder_Frame, text="Special Characters", variable=use_special, text_color="black").grid(row=8, column=2, pady=5, sticky="ew")
    customtkinter.CTkCheckBox(PasswordMakingBorder_Frame, text="Numbers", variable=use_numbers, text_color="black").grid(row=9, column=2, pady=5, sticky="ew")
    customtkinter.CTkCheckBox(PasswordMakingBorder_Frame, text="Uppercase Letters", variable=use_upper, text_color="black").grid(row=8, column=3, pady=5, sticky="ew")
    customtkinter.CTkCheckBox(PasswordMakingBorder_Frame, text="Lowercase Letters", variable=use_lower, text_color="black").grid(row=9, column=3, pady=5, sticky="ew")

    # Label to display the result
    result_label = customtkinter.CTkLabel(PasswordMakingBorder_Frame, text="", text_color="black")
    result_label.grid(row=11, column=2, pady=10, sticky="ew")

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
    customtkinter.CTkButton(PasswordMakingBorder_Frame, text="Generate Password", command=generate_password).grid(row=10, column=2, pady=10, sticky="ew")
#######################################################################################################################################################

    # Save Button
    create_button = customtkinter.CTkButton(PasswordMakingBorder_Frame, text="Create")
    create_button.grid(row=12,column=2, pady=(30, 10), sticky="ew")

    # Back Button
    back_button = customtkinter.CTkButton(PasswordMakingBorder_Frame, text="Back", command=close_passwordMaker_page)
    back_button.grid(row=13,column=2, pady=(30, 10), sticky="ew")

    main_frame.grid_forget()
    PasswordMaking_Frame.grid(row=1, column=1, sticky="nsew")

    PasswordMakingBorder_Frame.columnconfigure(0, weight=1)
    PasswordMakingBorder_Frame.columnconfigure(1, weight=2)
    PasswordMakingBorder_Frame.columnconfigure(2, weight=1)
    PasswordMakingBorder_Frame.columnconfigure(3, weight=1)
    PasswordMakingBorder_Frame.columnconfigure(4, weight=1)
    PasswordMakingBorder_Frame.columnconfigure(5, weight=1)
    PasswordMakingBorder_Frame.columnconfigure(6, weight=1)

#Closing the page 
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

    label = customtkinter.CTkLabel(NotesBorder_Frame, text="Notes Maker", font=("Verdana", 20, ), text_color="black")
    label.grid(row=0,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkLabel(NotesBorder_Frame, text="Notes Title", text_color="black")
    label.grid(row=1,column=2, pady=10, sticky="ew")
    label = customtkinter.CTkEntry(NotesBorder_Frame, placeholder_text="Enter 1")
    label.grid(row=2,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkLabel(NotesBorder_Frame, text="Enter Notes", text_color="black")
    label.grid(row=3,column=2, pady=10, sticky="ew")
    label = customtkinter.CTkTextbox(NotesBorder_Frame, height=150)
    label.grid(row=4,column=2, pady=10, sticky="ew")

    create_button = customtkinter.CTkButton(NotesBorder_Frame, text="Create")
    create_button.grid(row=5,column=2, pady=(30, 10), sticky="ew")

    back_button = customtkinter.CTkButton(NotesBorder_Frame, text="Back", command=close_notes_page)
    back_button.grid(row=6,column=2, pady=10, sticky="ew")

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

    label = customtkinter.CTkLabel(BankBorder_Frame, text="Banking Cards Maker", font=("Verdana", 20), text_color="black")
    label.grid(row=0, column=2, pady=(10, 20), sticky="n")

    label = customtkinter.CTkLabel(BankBorder_Frame, text="Card Number", text_color="black")
    label.grid(row=1,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkEntry(BankBorder_Frame, placeholder_text="Enter 1")
    label.grid(row=2,column=2, pady=10, sticky="ew")
    
    label = customtkinter.CTkLabel(BankBorder_Frame, text="Expire Date", text_color="black")
    label.grid(row=3,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkEntry(BankBorder_Frame, placeholder_text="Enter 2")
    label.grid(row=4,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkLabel(BankBorder_Frame, text="CVV", text_color="black")
    label.grid(row=5,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkEntry(BankBorder_Frame, placeholder_text="Enter 3")
    label.grid(row=6,column=2, pady=10, sticky="ew")

    create_button = customtkinter.CTkButton(BankBorder_Frame, text="Create")
    create_button.grid(row=7,column=2, pady=(30, 10), sticky="ew")

    back_button = customtkinter.CTkButton(BankBorder_Frame, text="Back", command=close_banking_cards_page)
    back_button.grid(row=8,column=2, pady=10, sticky="ew")

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

# Open One-Time Password page
def open_Network_page():
    global Network_Frame
    if "One_Time_Password_Frame" in globals() and Network_Frame.winfo_exists():
        Network_Frame.destroy()

    Network_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    Network_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

    Network_Border_Frame = customtkinter.CTkFrame(Network_Frame, fg_color="#A9A9A9")
    Network_Border_Frame.pack(fill="both", expand=True, padx=5, pady=5)

    label = customtkinter.CTkLabel(Network_Border_Frame, text="Network Password Maker", font=("Verdana", 20), text_color="black")
    label.pack(pady=20)

    back_button = customtkinter.CTkButton(Network_Border_Frame, text="Back", command=close_network_page)
    back_button.pack(pady=20)

    main_frame.grid_forget()
    Network_Frame.grid(row=1, column=1, sticky="nsew")

def close_network_page():
    Network_Frame.destroy()
    main_frame.grid(row=1, column=1, sticky="nsew")
    
#This is the profile page settings here you can upload an image and your name and save it!
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

        PImage_label = customtkinter.CTkLabel(Profile_Border_Frame , text="Please put a picture!", width=300, height=300, fg_color="black")
        PImage_label.pack(pady=10)

        UploadingI = customtkinter.CTkButton(Profile_Border_Frame , text="Upload Image", command=upload_profile_image)
        UploadingI.pack(pady=30)

# Profile Name Input Field   
        Profile_Name = customtkinter.StringVar()
        name_entry = customtkinter.CTkEntry(Profile_Border_Frame , textvariable=Profile_Name, width=250, placeholder_text ="Enter your name")
        name_entry.pack(pady=20)

        Save_button = customtkinter.CTkButton(Profile_Border_Frame , text="Save Name", command=save_profile_name)
        Save_button.pack(pady=5)

# Back Button
        back_button = customtkinter.CTkButton(Profile_Border_Frame , text="Back", command=close_Profile_Page)
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

#The profile page image
        PImage_label.configure(image=profile_image_large, text="")
        PImage_label.image = profile_image_large  

#The profile box image
        profile_box_label.configure(image=profile_image_small, text="")
        profile_box_label.image = profile_image_small  

#Now we can save it and close the page and when we open it it will save till you click X out
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

    
# Make it not change size
window.resizable(False, False)
window.mainloop()