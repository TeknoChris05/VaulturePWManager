import customtkinter
from PIL import Image
import tkinter

window = customtkinter.CTk()

window.title("Vaulture")


#Retrieve screen width and height
screen_dimension_width = window.winfo_screenwidth()
screen_dimension_height = window.winfo_screenheight()

window.geometry(f"{screen_dimension_width}x{screen_dimension_height}-10+0")

login_frame = customtkinter.CTkFrame(master=window,
                                     width = screen_dimension_width/2,
                                     height = screen_dimension_height/1.5,
                                     corner_radius= 15,
                                     bg_color= "yellow")

login_frame.pack(padx = 20, pady = 20)
login_frame.pack_propagate(False)


vulture = customtkinter.CTkImage(
    Image.open("C:/Users/romay/Downloads/imageedit_11_2501753302.png"),
    size = (200,200)
)

vulture_label = customtkinter.CTkLabel(login_frame, text = "", image=vulture)
vulture_label.pack(pady=5)

title_label = customtkinter.CTkLabel(login_frame, text= "VAULTURE", text_color="yellow", font= ("Arial", 22))
title_label.place(relx= 0.5, rely= 0.35, anchor= tkinter.CENTER)


username_label = customtkinter.CTkLabel(login_frame, text= "Username", font=("Courier", 16), text_color="yellow")
username_label.place(relx= 0.5, rely= 0.4, anchor= tkinter.CENTER)

username_entry = customtkinter.CTkEntry(login_frame, placeholder_text= "Enter Username",
                                        width = 150,
                                        height = 30,
                                        border_width= 1,
                                        corner_radius= 10)
username_entry.place(relx = 0.5, rely = 0.45, anchor = tkinter.CENTER)


password_label = customtkinter.CTkLabel(login_frame, text= "Password", font=("Courier", 16), text_color="yellow")
password_label.place(relx= 0.5, rely= 0.5, anchor= tkinter.CENTER)

password_entry = customtkinter.CTkEntry(login_frame, placeholder_text="Enter Password",
                                        width= 150,
                                        height= 30,
                                        border_width= 1,
                                        corner_radius= 10)
password_entry.place(relx= 0.5, rely= 0.55, anchor= tkinter.CENTER)

account_label = customtkinter.CTkLabel(login_frame, text="Don't have an account? Create one by clicking the 'Sign Up' button", font= ("Courier", 12), text_color="yellow")
account_label.place(relx= 0.5, rely= 0.6, anchor= tkinter.CENTER)

login_button = customtkinter.CTkButton(login_frame, text="Login", fg_color="yellow", text_color="black")
login_button.place(x=230, rely= 0.65)

sign_up_button = customtkinter.CTkButton(login_frame, text="Sign Up", fg_color="yellow", text_color="black")
sign_up_button.place(x=400, rely= 0.65)

window.mainloop()
