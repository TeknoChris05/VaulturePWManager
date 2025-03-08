import customtkinter
from PIL import Image
import tkinter

window = customtkinter.CTk()
window.title("Vaulture")

# Screen width and height 
screen_dimension_width = window.winfo_screenwidth()
screen_dimension_height = window.winfo_screenheight()
window.geometry(f"{screen_dimension_width}x{screen_dimension_height}-10+0")

# Configure grid weights
# Sidebar
window.columnconfigure(0, weight=0)  
# MainStuffC
window.columnconfigure(1, weight=5)  
# SearchBar
window.rowconfigure(0, weight=0)  
# MainstuffR
window.rowconfigure(1, weight=2)  
# BottomBar
window.rowconfigure(2, weight=0)  

# Main content frame
main_frame = customtkinter.CTkFrame(window, fg_color="#60728a")
main_frame.grid(row=1, column=1, padx=0, pady=0, sticky="nsew")  

# Search bar and settings button within the main frame
search_frame = customtkinter.CTkFrame(main_frame, fg_color="#60728a")
search_frame.grid(row=0, column=3, sticky="n", pady=20)
searching = customtkinter.CTkEntry(search_frame, placeholder_text="Search here...", width=450)
searching.grid(row=0, column=0, padx=550)

# Left sidebar 
sidebar = customtkinter.CTkFrame(window, width=200, corner_radius=20, fg_color="#0e3161", border_width=8, border_color="black")
sidebar.grid(row=0, column=0, rowspan=3, sticky="nsw")  

# Text on left sidebar (Buttons)
filter1_button = customtkinter.CTkButton(sidebar, text="Passwords", width=40, height=70, corner_radius=30, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_passwords_page())
filter1_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

filter2_button = customtkinter.CTkButton(sidebar, text="Favorites", width=40, height=70, corner_radius=30, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_favorites_page())
filter2_button.grid(row=1, column=0, padx=10, pady=60, sticky="nsew")

filter3_button = customtkinter.CTkButton(sidebar, text="Notes", width=40, height=70, corner_radius=30, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_notes_page())
filter3_button.grid(row=2, column=0, padx=10, pady=60, sticky="nsew")

filter4_button = customtkinter.CTkButton(sidebar, text="Banking Cards", width=40, height=70, corner_radius=30, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_banking_cards_page())
filter4_button.grid(row=3, column=0, padx=10, pady=60, sticky="nsew")

filter5_button = customtkinter.CTkButton(sidebar, text="One-Time Password", width=40, height=70, corner_radius=30, fg_color="#282929", border_width=2, border_color="gray", command=lambda: open_one_time_password_page())
filter5_button.grid(row=4, column=0, padx=10, pady=80, sticky="nsew")

Archive_button = customtkinter.CTkButton(sidebar, text="Archived 📦", width=40, height=70, corner_radius=30, fg_color="#282929", border_width=2, border_color="gray")
Archive_button.grid(row=5, column=0, padx=10, pady=5, sticky="nsew")

Trash_button = customtkinter.CTkButton(sidebar, text="Trash 🗑️", width=40, height=70, corner_radius=30, fg_color="#282929", border_width=2, border_color="gray")
Trash_button.grid(row=6, column=0, padx=10, pady=5, sticky="nsew")


# White bottom bar
bottom_bar = customtkinter.CTkFrame(window, height=90, corner_radius=0, fg_color="#133f61")
bottom_bar.grid(row=2, column=1, columnspan=2, sticky="ew") 

# Bottom bar buttons 
ValtureP_button = customtkinter.CTkButton(bottom_bar, text="🐦", width=60, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray")
ValtureP_button.grid(row=0, column=0, pady=30)

Search_button = customtkinter.CTkButton(bottom_bar, text="🔍", width=60, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray")
Search_button.grid(row=0, column=1, pady=5)

# Profile button in bottom bar
Profile_button = customtkinter.CTkButton(bottom_bar, text="👥", width=60, height=70, corner_radius=900, fg_color="#282929",border_width=2, border_color="gray", command=lambda: ProfileP())
Profile_button.grid(row=0, column=2, pady=5)

Sort_button = customtkinter.CTkButton(bottom_bar, text="Sort", width=10, height=70, corner_radius=900, fg_color="#282929", border_width=1, border_color="gray")
Sort_button.grid(row=0, column=3, pady=5)

# Create Button and settings Button on main frame
Create_button = customtkinter.CTkButton(main_frame, text="➕", width=70, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray")
Create_button.place(relx=0.99, rely=0.99, anchor="se")

# Function to open the Passwords page
def open_passwords_page():
    passwords_window = customtkinter.CTkToplevel(window)
    passwords_window.title("Passwords Page")
    passwords_window.geometry("600x400")
    passwords_window.attributes("-topmost", True)  #Looked up how to keep window on top of desktop on chat gpt

    label = customtkinter.CTkLabel(passwords_window, text="Your Passwords", font=("Arial", 18))
    label.pack(pady=20)
    
    # Add other elements for your passwords page, such as a list of passwords
    password_example = customtkinter.CTkLabel(passwords_window, text="Example: Test Password 1")
    password_example.pack(pady=10)

    back_button = customtkinter.CTkButton(passwords_window, text="Back", command=passwords_window.destroy)
    back_button.pack(pady=20)

#Open Functions page used chat gpt for -topmost, true function
def open_favorites_page():
    favorites_window = customtkinter.CTkToplevel(window)
    favorites_window.title("Favorites Page")
    favorites_window.geometry("600x400")
    favorites_window.attributes("-topmost", True)  #Looked up how to keep window on top of desktop on chat gpt

    label = customtkinter.CTkLabel(favorites_window, text="Your Favorites", font=("Arial", 18))
    label.pack(pady=20)

    back_button = customtkinter.CTkButton(favorites_window, text="Back", command=favorites_window.destroy)
    back_button.pack(pady=20)

#Open Notes page used chat gpt for -topmost, true function
def open_notes_page():
    notes_window = customtkinter.CTkToplevel(window)
    notes_window.title("Notes Page")
    notes_window.geometry("600x400")
    notes_window.attributes("-topmost", True)  #Looked up how to keep window on top of desktop on chat gpt

    label = customtkinter.CTkLabel(notes_window, text="Your Notes", font=("Arial", 18))
    label.pack(pady=20)

    back_button = customtkinter.CTkButton(notes_window, text="Back", command=notes_window.destroy)
    back_button.pack(pady=20)

#Open Banking cards page used chat gpt for -topmost, true function
def open_banking_cards_page():
    banking_window = customtkinter.CTkToplevel(window)
    banking_window.title("Banking Cards Page")
    banking_window.geometry("600x400")
    banking_window.attributes("-topmost", True)  #Looked up how to keep window on top of desktop on chat gpt

    label = customtkinter.CTkLabel(banking_window, text="Your Banking Cards", font=("Arial", 18))
    label.pack(pady=20)

    back_button = customtkinter.CTkButton(banking_window, text="Back", command=banking_window.destroy)
    back_button.pack(pady=20)

#Open One time password page used chat gpt for -topmost, true function
def open_one_time_password_page():
    otp_window = customtkinter.CTkToplevel(window)
    otp_window.title("One-Time Password Page")
    otp_window.geometry("600x400")
    otp_window.attributes("-topmost", True)  #Looked up how to keep window on top of desktop on chat gpt

    label = customtkinter.CTkLabel(otp_window, text="Your One-Time Passwords", font=("Arial", 18))
    label.pack(pady=20)

    back_button = customtkinter.CTkButton(otp_window, text="Back", command=otp_window.destroy)
    back_button.pack(pady=20)

#This will open up the profile page 
def ProfileP():
    otp_window = customtkinter.CTkToplevel(window, fg_color="#60728a")
    otp_window.title("One-Time Password Page")
    otp_window.geometry("600x600")
    otp_window.attributes("-topmost", True)

    label = customtkinter.CTkLabel(otp_window, text="User Profile Picture", font=("Arial", 20))
    label.pack(pady=20)
    label2 = customtkinter.CTkLabel(otp_window, text="User Profile Name", font=("Arial", 20))
    label2.pack(pady=20)

    back_button = customtkinter.CTkButton(otp_window, text="Back", command=otp_window.destroy)
    back_button.pack(pady=20)

# Passwords
bottom_bar.columnconfigure(0, weight=1)    
# Search
bottom_bar.columnconfigure(1, weight=1)  
# Profile
bottom_bar.columnconfigure(2, weight=1)  
# Sort
bottom_bar.columnconfigure(3, weight=1) 

# Make it not change size
window.resizable(False, False)

window.mainloop()