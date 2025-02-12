import customtkinter
from PIL import Image
import tkinter

window = customtkinter.CTk()

window.title("Vaulture Profile Page")

# Screen width and height 
screen_dimension_width = window.winfo_screenwidth()
screen_dimension_height = window.winfo_screenheight()

window.geometry(f"{screen_dimension_width}x{screen_dimension_height}-10+0")

window.mainloop()