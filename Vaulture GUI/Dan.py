import customtkinter
from PIL import Image
import tkinter

window = customtkinter.CTk()

window.title("Vaulture")

# Screen width and height 
screen_dimension_width = window.winfo_screenwidth()
screen_dimension_height = window.winfo_screenheight()

window.geometry(f"{screen_dimension_width}x{screen_dimension_height}-10+0")

# Left side bar
sidebar = customtkinter.CTkFrame(window, width=200, height=screen_dimension_height, corner_radius=0, fg_color="#B8860B", border_width=8, border_color="black")
sidebar.grid(row=0, column=0, sticky="ns")  # "ns" means the sidebar will stretch vertically

# Search bar at top
search_frame = customtkinter.CTkFrame(window)
search_frame.place(x=700, y=5)  # Place the search bar in the top section

# Entry field
search_entry = customtkinter.CTkEntry(search_frame, placeholder_text="Search here...", width=300)
search_entry.grid(row=0, column=0, padx=10)

# Frame for top 
frame = customtkinter.CTkFrame(window)
frame.grid(row=1, column=1, padx=20, pady=20)

screen_dimension_width = window.winfo_screenwidth()
screen_dimension_height = window.winfo_screenheight()


# white bar at bottom
bottom_bar_height = 50  
bottom_bar = customtkinter.CTkFrame(window, height=bottom_bar_height, corner_radius=0, fg_color="gray")
bottom_bar.place(relx=0.13, rely=1, relwidth=1, y=-bottom_bar_height)

#settings button in the top right corner to get you to the settings page. (Marteno R)
Vsettings_button = customtkinter.CTkButton(window, text="⚙️", width=50, height=50, corner_radius=25, fg_color="#B8860B", border_width=2, border_color="black", command=lambda: print("Go to settings"))
Vsettings_button.place(x=screen_dimension_width - 75, y=10)  

#Bottom line buttons. This will allow you to have the buttons to access all passwords, favorites, search , and profile.
ValtureP_button = customtkinter.CTkButton(bottom_bar, text="🐦 Bird", width=50, height=50, corner_radius=25, fg_color="#B8860B", border_width=2, border_color="gray", command=lambda: print("Go to settings"))
ValtureP_button.pack(side="left", padx=300, pady=5)

#Favorite

#Search button

#Profile Button

#Create Button

window.mainloop()


