import customtkinter
from PIL import Image
import tkinter
import acc2 
import os
from customtkinter import CTkImage
from tkinter import filedialog
from PIL import Image, ImageTk


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
# SearchBar
window.rowconfigure(0, weight=0)  
# MainstuffR
window.rowconfigure(1, weight=2)  
# BottomBar
window.rowconfigure(2, weight=0)  

# Main content frame
main_frame = customtkinter.CTkFrame(window, fg_color="#A9A9A9")
main_frame.grid(row=1, column=1, padx=0, pady=0, sticky="nsew")  

# Search bar and settings button within the main frame
search_frame = customtkinter.CTkFrame(main_frame, fg_color="#A9A9A9", height=50, width=480)  
search_frame.place(relx=0.5, rely=0.05, anchor="center")
searching = customtkinter.CTkEntry(search_frame, placeholder_text="Search here...", width=450)
searching.place(relx=0.5, rely=0.5, anchor="center") 

# Left sidebar 
sidebar = customtkinter.CTkFrame(window, width=200, corner_radius=20, fg_color="#0e3161", border_width=8, border_color="black")
sidebar.grid(row=0, column=0, rowspan=2, sticky="nsw")  
sidebar.grid_forget()  

# White bottom bar
bottom_bar = customtkinter.CTkFrame(window, height=90, corner_radius=0, fg_color="#133f61")
bottom_bar.grid(row=2, column=1, columnspan=2, sticky="ew") 

# Sidebar buttons (These will appear when the sidebar is toggled)
hamburger_button = customtkinter.CTkButton(main_frame, text="☰", width=60, height=60, corner_radius=10, fg_color="#0e3161", border_width=2, border_color="gray", command=lambda: toggle_sidebar())
hamburger_button.grid(row=0, column=0, padx=20, pady=30)

filter1_button = customtkinter.CTkButton(sidebar, text="Passwords", width=150, height=20, corner_radius=5, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_passwords_page())
filter1_button.grid(row=0, column=0, padx=30, pady=10, sticky="nsew")

filter2_button = customtkinter.CTkButton(sidebar, text="Favorites", width=150, height=0, corner_radius=5, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_favorites_page())
filter2_button.grid(row=1, column=0, padx=30, pady=10, sticky="nsew")

filter3_button = customtkinter.CTkButton(sidebar, text="Notes", width=150, height=20, corner_radius=5, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_notes_page())
filter3_button.grid(row=2, column=0, padx=30, pady=10, sticky="nsew")

filter4_button = customtkinter.CTkButton(sidebar, text="Banking Cards", width=150, height=20, corner_radius=5, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_banking_cards_page())
filter4_button.grid(row=3, column=0, padx=30, pady=10, sticky="nsew")

filter5_button = customtkinter.CTkButton(sidebar, text="One-Time Password", width=150, height=20, corner_radius=5, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_one_time_password_page())
filter5_button.grid(row=4, column=0, padx=30, pady=10, sticky="nsew")

Archive_button = customtkinter.CTkButton(sidebar, text="Archived 📦", width=40, height=20, corner_radius=5, fg_color="#282929", border_width=2, border_color="gray")
Archive_button.grid(row=5, column=0, padx=30, pady=20, sticky="nsew")

Trash_button = customtkinter.CTkButton(sidebar, text="Trash 🗑️", width=40, height=20, corner_radius=5, fg_color="#282929", border_width=2, border_color="gray")
Trash_button.grid(row=6, column=0, padx=30, pady=20, sticky="nsew")

#Assigning weights so that these buttons wont go offscreen
#Hamburger Button
sidebar.rowconfigure(0, weight=2)
# Passwords
sidebar.rowconfigure(1, weight=2)
# Favorites
sidebar.rowconfigure(2, weight=2)  
# Notes
sidebar.rowconfigure(3, weight=2)  
# Banking Cards
sidebar.rowconfigure(4, weight=2)  
# One-Time Password
sidebar.rowconfigure(5, weight=2)  
# Archived
sidebar.rowconfigure(6, weight=2)  
# Trash
sidebar.rowconfigure(7, weight=2)  


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
    sidebar_open = not sidebar_open  # Toggle the state



# Bottom bar buttons 
ValtureP_button = customtkinter.CTkButton(bottom_bar, text="🐦", width=60, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray")
ValtureP_button.grid(row=0, column=0, pady=30)

Search_button = customtkinter.CTkButton(bottom_bar, text="🔍", width=60, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray", command=lambda: search_bar_Click())
Search_button.grid(row=0, column=1, pady=5)

#this will move the mouse to the search bar
def search_bar_Click():
    searching.focus_set()


# Profile button in bottom bar
Profile_button = customtkinter.CTkButton(bottom_bar, text="👥", width=60, height=70, corner_radius=900, fg_color="#282929",border_width=2, border_color="gray", command=lambda: open_Profile_Page())
Profile_button.grid(row=0, column=2, pady=5)

# New Settings Button at Bottom 
def open_settings_page():
    settings_window = customtkinter.CTkFrame(main_frame)
    settings_window = acc2.SettingsApp() 

Settings_button = customtkinter.CTkButton(bottom_bar, text="⚙️", width=10, height=70, corner_radius=900, fg_color="#282929", border_width=1, border_color="gray", command=open_settings_page)
Settings_button.grid(row=0, column=3, pady=5) 


# Bottom Bar Setup
bottom_bar.columnconfigure(0, weight=1)    
# 
bottom_bar.columnconfigure(1, weight=1)  
# 
bottom_bar.columnconfigure(2, weight=1)  
# 
bottom_bar.columnconfigure(3, weight=1) 



# Open passwords page
def open_passwords_page():
    favorites_window = customtkinter.CTkToplevel(window)
    favorites_window.title("Passwords Page")
    favorites_window.geometry("600x400")
    favorites_window.attributes("-topmost", True)

    label = customtkinter.CTkLabel(favorites_window, text="Create Passwords", font=("Verdana", 20))
    label.pack(pady=20)

    back_button = customtkinter.CTkButton(favorites_window, text="Back", command=favorites_window.destroy)
    back_button.pack(pady=20)
# Open Favorites page
def open_favorites_page():
    favorites_window = customtkinter.CTkToplevel(window)
    favorites_window.title("Favorites Page")
    favorites_window.geometry("600x400")
    favorites_window.attributes("-topmost", True)

    label = customtkinter.CTkLabel(favorites_window, text="Favorites", font=("Verdana", 20))
    label.pack(pady=20)

    back_button = customtkinter.CTkButton(favorites_window, text="Back", command=favorites_window.destroy)
    back_button.pack(pady=20)

# Open Notes page
def open_notes_page():
    notes_window = customtkinter.CTkToplevel(window)
    notes_window.title("Create Notes Page")
    notes_window.geometry("600x400")
    notes_window.attributes("-topmost", True)

    label = customtkinter.CTkLabel(notes_window, text="Create Notes", font=("Verdana", 20))
    label.pack(pady=20)

    back_button = customtkinter.CTkButton(notes_window, text="Back", command=notes_window.destroy)
    back_button.pack(pady=20)

# Open Banking Cards page
def open_banking_cards_page():
    banking_window = customtkinter.CTkToplevel(window)
    banking_window.title("Create Banking Cards Page")
    banking_window.geometry("600x400")
    banking_window.attributes("-topmost", True)

    label = customtkinter.CTkLabel(banking_window, text="Create Banking Cards", font=("Verdana", 20))
    label.pack(pady=20)

    back_button = customtkinter.CTkButton(banking_window, text="Back", command=banking_window.destroy)
    back_button.pack(pady=20)

# Open One-Time Password page
def open_one_time_password_page():
    otp_window = customtkinter.CTkToplevel(window)
    otp_window.title("One-Time Password Page")
    otp_window.geometry("600x400")
    otp_window.attributes("-topmost", True)

    label = customtkinter.CTkLabel(otp_window, text="Create One-Time Passwords", font=("Verdana", 20))
    label.pack(pady=20)

    back_button = customtkinter.CTkButton(otp_window, text="Back", command=otp_window.destroy)
    back_button.pack(pady=20)

#This is the profile page settings here you can upload an image and your name and save it!
def open_Profile_Page():
    global Profile_Frame, Border_Frame, Profile_Name, PImage_label, profile_image


# Makes the frame if its not already made
    if "Profile_Frame" not in globals():
        Profile_Frame = customtkinter.CTkFrame(window, fg_color="black", border_width=3)  
        Profile_Frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

        Border_Frame = customtkinter.CTkFrame(Profile_Frame, fg_color="#A9A9A9")  
        Border_Frame.pack(fill="both", expand=True, padx=5, pady=5) 

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