import customtkinter
from PIL import Image
import tkinter

def ProfileP():
    profile_window = customtkinter.CTkToplevel()  
    profile_window.title("Profile Page")
    profile_frame = customtkinter.CTkFrame(profile_window, fg_color="#60728a") 
    profile_frame.grid(row=1, column=1, padx=0, pady=0, sticky="nsew") 

    profile_window.geometry("600x600")
    profile_window.minsize(600, 600)
    profile_window.maxsize(600, 600)

    profile_window.columnconfigure(1, weight=5)  
    profile_window.rowconfigure(1, weight=2)  

    # Text on top
    label = customtkinter.CTkLabel(profile_frame, text="User Profile", font=("Arial", 20))
    label.grid(row=0, column=0, padx=20, pady=20)

    label2 = customtkinter.CTkLabel(profile_frame, text="____________________", font=("Arial", 20))
    label2.grid(row=1 , column=0, padx=20, pady=20)

    profile_window.mainloop() 