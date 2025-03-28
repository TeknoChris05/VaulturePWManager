import customtkinter
from PIL import Image
import tkinter
import acc2 
import os
from customtkinter import CTkImage
from tkinter import filedialog
from PIL import Image, ImageTk
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
hamburger_button = customtkinter.CTkButton(main_frame, text="☰", width=60, height=60, corner_radius=10, fg_color="#0e3161", border_width=2, border_color="gray", command=lambda: toggle_sidebar())
hamburger_button.grid(row=0, column=0, padx=20, pady=30)

filter1_button = customtkinter.CTkButton(sidebar, text="Passwords🔒", width=150, height=20, corner_radius=5, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_passwordMaker_page())
filter1_button.grid(row=0, column=0, padx=30, pady=10, sticky="nsew")

filter3_button = customtkinter.CTkButton(sidebar, text="Notes📝", width=150, height=20, corner_radius=5, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_notes_page())
filter3_button.grid(row=1, column=0, padx=30, pady=10, sticky="nsew")

filter4_button = customtkinter.CTkButton(sidebar, text="Banking Cards💳", width=150, height=20, corner_radius=5, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_banking_cards_page())
filter4_button.grid(row=2, column=0, padx=30, pady=10, sticky="nsew")

filter5_button = customtkinter.CTkButton(sidebar, text="One-Time Password🔐", width=150, height=20, corner_radius=5, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_one_time_password_page())
filter5_button.grid(row=3, column=0, padx=30, pady=10, sticky="nsew")

Archive_button = customtkinter.CTkButton(sidebar, text="Archived 📦", width=40, height=20, corner_radius=5, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_archive_page())
Archive_button.grid(row=4, column=0, padx=30, pady=20, sticky="nsew")

Trash_button = customtkinter.CTkButton(sidebar, text="Trash 🗑️", width=40, height=20, corner_radius=5, fg_color="#282929", border_width=2, border_color="gray")
Trash_button.grid(row=5, column=0, padx=30, pady=20, sticky="nsew")

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
    global Passwords_Frame
    if "Passwords_Frame" in globals() and Passwords_Frame.winfo_exists():
        Passwords_Frame.destroy()

#  The creation of the frame and border
    Passwords_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    Passwords_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
    Border_Frame = customtkinter.CTkFrame(Passwords_Frame, fg_color="#A9A9A9")
    Border_Frame.pack(fill="both", expand=True, padx=5, pady=5)

    label = customtkinter.CTkLabel(Border_Frame, text="Passwords", font=("Verdana", 20))
    label.pack(pady=20)
# Search Bar inside Passwords Page
    search_frame = customtkinter.CTkFrame(Border_Frame, fg_color="#A9A9A9", height=50, width=480)
    search_frame.pack(pady=10)
    searching = customtkinter.CTkEntry(search_frame, placeholder_text="Search here...", width=450)
    searching.pack(pady=10)

    back_button = customtkinter.CTkButton(Border_Frame, text="Back", command=close_passwords_page)
    back_button.pack(pady=20)

    main_frame.grid_forget()
    Passwords_Frame.grid(row=1, column=1, sticky="nsew")

#Closing the page 
def close_passwords_page():
    Passwords_Frame.destroy() 
    main_frame.grid(row=1, column=1, sticky="nsew") 


ValtureP_button = customtkinter.CTkButton(bottom_bar, text="🐦", width=60, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_passwords_page())
ValtureP_button.grid(row=0, column=0, pady=30)

# Open Favorites page
def open_favorites_page():
    global Favorites_Frame
    if "Favorites_Frame" in globals() and Favorites_Frame.winfo_exists():
        Favorites_Frame.destroy()

    Favorites_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    Favorites_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

    Border_Frame = customtkinter.CTkFrame(Favorites_Frame, fg_color="#A9A9A9")
    Border_Frame.pack(fill="both", expand=True, padx=5, pady=5)

    label = customtkinter.CTkLabel(Border_Frame, text="Favorites", font=("Verdana", 20))
    label.pack(pady=20)

# Search Bar inside Favorites Page
    search_frame = customtkinter.CTkFrame(Border_Frame, fg_color="#A9A9A9", height=50, width=480)
    search_frame.pack(pady=10)
    searching = customtkinter.CTkEntry(search_frame, placeholder_text="Search here...", width=450)
    searching.pack(pady=10)

    back_button = customtkinter.CTkButton(Border_Frame, text="Back", command=close_favorites_page)
    back_button.pack(pady=20)

    main_frame.grid_forget()
    Favorites_Frame.grid(row=1, column=1, sticky="nsew")

Search_button = customtkinter.CTkButton(bottom_bar, text="⭐", width=60, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_favorites_page())
Search_button.grid(row=0, column=1, pady=5)

# Profile button in bottom bar
Profile_button = customtkinter.CTkButton(bottom_bar, text="👥", width=60, height=70, corner_radius=900, fg_color="#282929",border_width=2, border_color="gray", command=lambda: open_Profile_Page())
Profile_button.grid(row=0, column=2, pady=5)

# New Settings Button at Bottom 
def open_settings_page():
    acc2.opening_settings()
    
Settings_button = customtkinter.CTkButton(bottom_bar, text="⚙️", width=10, height=70, corner_radius=900, fg_color="#282929", border_width=1, border_color="gray", command=lambda: open_settings_page())
Settings_button.grid(row=0, column=3, pady=5) 


# Bottom Bar Setup
#🐦
bottom_bar.columnconfigure(0, weight=2)    
# ⭐
bottom_bar.columnconfigure(1, weight=1)  
# 👥
bottom_bar.columnconfigure(2, weight=1)  
# ⚙️
bottom_bar.columnconfigure(3, weight=1) 

#Left bar stuff
# Regular Password Maker
def open_passwordMaker_page(*args, **kwargs):
    import string, random  # needed for password generation
    global Passwords_Frame
    if "Passwords_Frame" in globals() and Passwords_Frame.winfo_exists():
        Passwords_Frame.destroy()

    # Main frame and border setup
    Passwords_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    Passwords_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
    Border_Frame = customtkinter.CTkFrame(Passwords_Frame, fg_color="#A9A9A9")
    Border_Frame.pack(fill="both", expand=True, padx=5, pady=5)

    label = customtkinter.CTkLabel(Border_Frame, text="Password Maker", font=("Verdana", 20), text_color="black")
    label.grid(row=0, column=2, pady=(10, 20), sticky="n")

    label = customtkinter.CTkLabel(Border_Frame, text="Username", text_color="black")
    label.grid(row=1,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkEntry(Border_Frame, placeholder_text="Enter 1")
    label.grid(row=2,column=2, pady=10, sticky="ew")
    
    label = customtkinter.CTkLabel(Border_Frame, text="Email", text_color="black")
    label.grid(row=3,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkEntry(Border_Frame, placeholder_text="Enter 2")
    label.grid(row=4,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkLabel(Border_Frame, text="Password", text_color="black")
    label.grid(row=5,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkEntry(Border_Frame, placeholder_text="Enter 3")
    label.grid(row=6,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkLabel(Border_Frame, text="Password Generation Checklist", text_color="black")
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
    customtkinter.CTkCheckBox(Border_Frame, text="Special Characters", variable=use_special, text_color="black").grid(row=8, column=2, pady=5, sticky="ew")
    customtkinter.CTkCheckBox(Border_Frame, text="Numbers", variable=use_numbers, text_color="black").grid(row=9, column=2, pady=5, sticky="ew")
    customtkinter.CTkCheckBox(Border_Frame, text="Uppercase Letters", variable=use_upper, text_color="black").grid(row=8, column=3, pady=5, sticky="ew")
    customtkinter.CTkCheckBox(Border_Frame, text="Lowercase Letters", variable=use_lower, text_color="black").grid(row=9, column=3, pady=5, sticky="ew")

    # Label to display the result
    result_label = customtkinter.CTkLabel(Border_Frame, text="", text_color="black")
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
    customtkinter.CTkButton(Border_Frame, text="Generate Password", command=generate_password).grid(row=10, column=2, pady=10, sticky="ew")
#######################################################################################################################################################

    # Save Button
    create_button = customtkinter.CTkButton(Border_Frame, text="Create")
    create_button.grid(row=12,column=2, pady=(30, 10), sticky="ew")

    # Back Button
    back_button = customtkinter.CTkButton(Border_Frame, text="Back", command=close_passwordMaker_page)
    back_button.grid(row=13,column=2, pady=(30, 10), sticky="ew")

    main_frame.grid_forget()
    Passwords_Frame.grid(row=1, column=1, sticky="nsew")

    Border_Frame.columnconfigure(0, weight=1)
    Border_Frame.columnconfigure(1, weight=2)
    Border_Frame.columnconfigure(2, weight=1)
    Border_Frame.columnconfigure(3, weight=1)
    Border_Frame.columnconfigure(4, weight=1)
    Border_Frame.columnconfigure(5, weight=1)
    Border_Frame.columnconfigure(6, weight=1)

#Closing the page 
def close_passwordMaker_page():
    Passwords_Frame.destroy() 
    main_frame.grid(row=1, column=1, sticky="nsew") 

   
def close_favorites_page():
    Favorites_Frame.destroy()
    main_frame.grid(row=1, column=1, sticky="nsew")

# Open Notes page
def open_notes_page():
    global Notes_Frame
    if "Notes_Frame" in globals() and Notes_Frame.winfo_exists():
        Notes_Frame.destroy()

    Notes_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    Notes_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
    Border_Frame = customtkinter.CTkFrame(Notes_Frame, fg_color="#A9A9A9")
    Border_Frame.pack(fill="both", expand=True, padx=5, pady=5)

    label = customtkinter.CTkLabel(Border_Frame, text="Notes Maker", font=("Verdana", 20, ), text_color="black")
    label.grid(row=0,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkLabel(Border_Frame, text="Notes Title", text_color="black")
    label.grid(row=1,column=2, pady=10, sticky="ew")
    label = customtkinter.CTkEntry(Border_Frame, placeholder_text="Enter 1")
    label.grid(row=2,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkLabel(Border_Frame, text="Enter Notes", text_color="black")
    label.grid(row=3,column=2, pady=10, sticky="ew")
    label = customtkinter.CTkTextbox(Border_Frame, height=150)
    label.grid(row=4,column=2, pady=10, sticky="ew")

    create_button = customtkinter.CTkButton(Border_Frame, text="Create")
    create_button.grid(row=5,column=2, pady=(30, 10), sticky="ew")

    back_button = customtkinter.CTkButton(Border_Frame, text="Back", command=close_notes_page)
    back_button.grid(row=6,column=2, pady=10, sticky="ew")

    main_frame.grid_forget()
    Notes_Frame.grid(row=1, column=1, sticky="nsew")


    Border_Frame.columnconfigure(0, weight=1)
    Border_Frame.columnconfigure(1, weight=2)
    Border_Frame.columnconfigure(2, weight=1)
    Border_Frame.columnconfigure(3, weight=1)
    Border_Frame.columnconfigure(4, weight=1)
    Border_Frame.columnconfigure(5, weight=1)
    Border_Frame.columnconfigure(6, weight=1)

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

    Border_Frame = customtkinter.CTkFrame(Banking_Cards_Frame, fg_color="#A9A9A9")
    Border_Frame.pack(fill="both", expand=True, padx=5, pady=5)

    label = customtkinter.CTkLabel(Border_Frame, text="Banking Cards Maker", font=("Verdana", 20), text_color="black")
    label.grid(row=0, column=2, pady=(10, 20), sticky="n")

    label = customtkinter.CTkLabel(Border_Frame, text="Card Number", text_color="black")
    label.grid(row=1,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkEntry(Border_Frame, placeholder_text="Enter 1")
    label.grid(row=2,column=2, pady=10, sticky="ew")
    
    label = customtkinter.CTkLabel(Border_Frame, text="Expire Date", text_color="black")
    label.grid(row=3,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkEntry(Border_Frame, placeholder_text="Enter 2")
    label.grid(row=4,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkLabel(Border_Frame, text="CVV", text_color="black")
    label.grid(row=5,column=2, pady=10, sticky="ew")

    label = customtkinter.CTkEntry(Border_Frame, placeholder_text="Enter 3")
    label.grid(row=6,column=2, pady=10, sticky="ew")

    create_button = customtkinter.CTkButton(Border_Frame, text="Create")
    create_button.grid(row=7,column=2, pady=(30, 10), sticky="ew")

    back_button = customtkinter.CTkButton(Border_Frame, text="Back", command=close_banking_cards_page)
    back_button.grid(row=8,column=2, pady=10, sticky="ew")

    main_frame.grid_forget()
    Banking_Cards_Frame.grid(row=1, column=1, sticky="nsew")

    Border_Frame.columnconfigure(0, weight=1)
    Border_Frame.columnconfigure(1, weight=2)
    Border_Frame.columnconfigure(2, weight=1)
    Border_Frame.columnconfigure(3, weight=1)
    Border_Frame.columnconfigure(4, weight=1)
    Border_Frame.columnconfigure(5, weight=1)
    Border_Frame.columnconfigure(6, weight=1)

    
def close_banking_cards_page():
    Banking_Cards_Frame.destroy()
    main_frame.grid(row=1, column=1, sticky="nsew")

# Open One-Time Password page
def open_one_time_password_page():
    global One_Time_Password_Frame
    if "One_Time_Password_Frame" in globals() and One_Time_Password_Frame.winfo_exists():
        One_Time_Password_Frame.destroy()

    One_Time_Password_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    One_Time_Password_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

    Border_Frame = customtkinter.CTkFrame(One_Time_Password_Frame, fg_color="#A9A9A9")
    Border_Frame.pack(fill="both", expand=True, padx=5, pady=5)

    label = customtkinter.CTkLabel(Border_Frame, text="One-Time Password Maker", font=("Verdana", 20), text_color="black")
    label.pack(pady=20)

    back_button = customtkinter.CTkButton(Border_Frame, text="Back", command=close_one_time_password_page)
    back_button.pack(pady=20)

    main_frame.grid_forget()
    One_Time_Password_Frame.grid(row=1, column=1, sticky="nsew")

def close_one_time_password_page():
    One_Time_Password_Frame.destroy()
    main_frame.grid(row=1, column=1, sticky="nsew")
    
#This is the profile page settings here you can upload an image and your name and save it!
def open_Profile_Page():
    window.minsize(800, 600)  
    window.maxsize(1920, 1080)
    global Profile_Frame, Border_Frame, Profile_Name, PImage_label, profile_image


# Makes the frame if its not already made
    if "Profile_Frame" not in globals():
        Profile_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)  
        Profile_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

        Border_Frame = customtkinter.CTkFrame(Profile_Frame, fg_color="#A9A9A9")  
        Border_Frame.pack(fill="both", expand=True, padx=5, pady=5) 

        label = customtkinter.CTkLabel(Border_Frame, text="Profile Page", font=("Verdana", 20), text_color="black")
        label.pack(pady=20)

        PImage_label = customtkinter.CTkLabel(Border_Frame , text="Please put a picture!", width=180, height=180, fg_color="black")
        PImage_label.pack(pady=10)

        UploadingI = customtkinter.CTkButton(Border_Frame , text="Upload Image", command=upload_profile_image)
        UploadingI.pack(pady=30)

# Profile Name Input Field   
        Profile_Name = customtkinter.StringVar()
        name_entry = customtkinter.CTkEntry(Border_Frame , textvariable=Profile_Name, width=250, placeholder_text ="Enter your name")
        name_entry.pack(pady=20)

        Save_button = customtkinter.CTkButton(Border_Frame , text="Save Name", command=save_profile_name)
        Save_button.pack(pady=5)

# Back Button
        back_button = customtkinter.CTkButton(Border_Frame , text="Back", command=close_Profile_Page)
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
        profile_image_large = CTkImage(light_image=img_large, dark_image=img_large, size=(200, 200))

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

# Open Notes page
def open_archive_page():
    global Notes_Frame
    if "Notes_Frame" in globals() and Notes_Frame.winfo_exists():
        Notes_Frame.destroy()

    Notes_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)
    Notes_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

    Border_Frame = customtkinter.CTkFrame(Notes_Frame, fg_color="#A9A9A9")
    Border_Frame.pack(fill="both", expand=True, padx=5, pady=5)

    label = customtkinter.CTkLabel(Border_Frame, text="Archived", font=("Verdana", 20), text_color="black")
    label.pack(pady=20)

    back_button = customtkinter.CTkButton(Border_Frame, text="Back", command=close_notes_page)
    back_button.pack(pady=20)

    main_frame.grid_forget()
    Notes_Frame.grid(row=1, column=1, sticky="nsew")

def close_archive_page():
    Notes_Frame.destroy()
    main_frame.grid(row=1, column=1, sticky="nsew")
    
# Make it not change size
window.resizable(False, False)
window.mainloop()