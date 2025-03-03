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
window.columnconfigure(0, weight=0)  # Sidebar
window.columnconfigure(1, weight=5)  # MainStuff
window.rowconfigure(0, weight=0)  # SearchBar
window.rowconfigure(1, weight=1)  # Content
window.rowconfigure(2, weight=0)  # BottomBar


# Left sidebar 
sidebar = customtkinter.CTkFrame(window, width=200, corner_radius=0, fg_color="#B8860B", border_width=8, border_color="black")
sidebar.grid(row=0, column=0, rowspan=3, sticky="nsw")  

# Main content frame 
main_frame = customtkinter.CTkFrame(window)
main_frame.grid(row=1, column=1, padx= 10, pady=5, sticky="nsew")  

# Search bar and settings button within the main frame
search_frame = customtkinter.CTkFrame(main_frame)
search_frame.grid(row=0, column=3, sticky="n" , pady=20)
search_entry = customtkinter.CTkEntry(search_frame, placeholder_text="Search here...", width=450)
search_entry.grid(row=0, column=0, padx=250)

# White bottom bar 
bottom_bar = customtkinter.CTkFrame(window, height=90, corner_radius=0, fg_color="gray")
bottom_bar.grid(row=2, column=1, columnspan=2, sticky="ew", pady=30)  
bottom_bar.columnconfigure(0, weight=1)  # Passwords
bottom_bar.columnconfigure(1, weight=1)  # Favorites
bottom_bar.columnconfigure(2, weight=1)  # Search
bottom_bar.columnconfigure(3, weight=1)  # Profile

# Bottom bar buttons 
ValtureP_button = customtkinter.CTkButton(bottom_bar, text="🐦", width=50, height=50, corner_radius=25, fg_color="#B8860B", border_width=2, border_color="gray")
ValtureP_button.grid(row=0, column=0, pady=5)

# Settings button 
Vsettings_button = customtkinter.CTkButton(main_frame, text="⚙️", width=50, height=50, corner_radius=25, fg_color="#B8860B", border_width=2, border_color="black")
Vsettings_button.grid(row=0, column=5, sticky="ne", padx=10, pady=5)

Favorite_button = customtkinter.CTkButton(bottom_bar, text="⭐", width=50, height=50, corner_radius=25, fg_color="#B8860B", border_width=2, border_color="gray")
Favorite_button.grid(row=0, column=1, pady=5)

Search_button = customtkinter.CTkButton(bottom_bar, text="🔍", width=50, height=50, corner_radius=25, fg_color="#B8860B", border_width=2, border_color="gray")
Search_button.grid(row=0, column=2, pady=5)

Profile_button = customtkinter.CTkButton(bottom_bar, text="👥", width=50, height=50, corner_radius=25, fg_color="#B8860B", border_width=2, border_color="gray")
Profile_button.grid(row=0, column=3, pady=5)

# Create Button (Same size, but moved down into the proper corner)
Create_button = customtkinter.CTkButton(window, text="➕", width=45, height=45, corner_radius=1000, fg_color="#B8860B", border_width=2, border_color="black")
Create_button.grid(row=1, column=1, sticky="se", padx=20, pady=30)  

# Make it not change size
window.resizable(False, False)

window.mainloop()