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
main_frame.grid(row=1, column=1, padx= 0, pady=0, sticky="nsew")  

# Search bar and settings button within the main frame
search_frame = customtkinter.CTkFrame(main_frame, fg_color="#60728a")
search_frame.grid(row=0, column=3, sticky="n" , pady=20)
searching = customtkinter.CTkEntry(search_frame, placeholder_text="Search here...", width=450)
searching.grid(row=0, column=0, padx=550)

# Left sidebar 
sidebar = customtkinter.CTkFrame(window, width=200, corner_radius=20, fg_color="#0e3161", border_width=8, border_color="black")
sidebar.grid(row=0, column=0, rowspan=3, sticky="nsw")  

# White bottom bar 
bottom_bar = customtkinter.CTkFrame(window, height=90, corner_radius=0, fg_color="#133f61")
bottom_bar.grid(row=2, column=1, columnspan=2, sticky="ew") 

# Bottom bar buttons 
ValtureP_button = customtkinter.CTkButton(bottom_bar, text="🐦", width=70, height=70, corner_radius= 900, fg_color="#282929", border_width=2, border_color="gray")
ValtureP_button.grid(row=0, column=0, pady=30)

# Settings button 
Vsettings_button = customtkinter.CTkButton(main_frame, text="⚙️", width=70, height=70, corner_radius= 900, fg_color="#282929", border_width=2, border_color="gray")
Vsettings_button.grid(row=0, column=5, sticky="ne", padx=70, pady=5)

Favorite_button = customtkinter.CTkButton(bottom_bar, text="⭐", width=70, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray")
Favorite_button.grid(row=0, column=1, pady=5)

Search_button = customtkinter.CTkButton(bottom_bar, text="🔍", width=70, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray")
Search_button.grid(row=0, column=2, pady=5)

Profile_button = customtkinter.CTkButton(bottom_bar, text="👥", width=70, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray")
Profile_button.grid(row=0, column=3, pady=5)

# Create Button (Same size, but moved down into the proper corner)
Create_button = customtkinter.CTkButton(main_frame, text="➕", width=70, height=70, corner_radius=900, fg_color="#282929", border_width=2, border_color="gray")
Create_button.place(relx=0.98, rely=0.99, anchor="se")


# Passwords
bottom_bar.columnconfigure(0, weight=1)  
# Favorites
bottom_bar.columnconfigure(1, weight=1)  
# Search
bottom_bar.columnconfigure(2, weight=1)  
# Profile
bottom_bar.columnconfigure(3, weight=1)  

# Make it not change size
window.resizable(False, False)

window.mainloop()