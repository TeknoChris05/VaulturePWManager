from typing import no_type_check_decorator

import customtkinter
from PIL import Image
import tkinter
import os
from pathlib import Path
import string
#from Dan import window



class Login_Page(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        self.title("Vaulture")
        self.configure(fg_color="#0d133e")


        #Retrieve screen width and height
        screen_dimension_width = self.winfo_screenwidth()
        screen_dimension_height = self.winfo_screenheight()

        x_pos = ((screen_dimension_width-self.winfo_screenwidth()) // 2) -10
        y_pos = ((screen_dimension_height-self.winfo_screenheight()) // 2) -1

        self.geometry(f"{screen_dimension_width}x{screen_dimension_height}+{x_pos}+{y_pos}")
        self.pack_propagate(False)
        self.minsize(800, 600)  
        self.maxsize(1920, 1080)
        self.login_frame = customtkinter.CTkFrame(master=self,
                                     width = screen_dimension_width/2,
                                     height = screen_dimension_height/1.5,
                                     border_width= 10,
                                     border_color ="#000206",
                                     fg_color = "#030c49")

        self.login_frame.pack(padx = 20, pady = 20)
        self.login_frame.pack_propagate(False)

        self.account_frame = customtkinter.CTkFrame(self, width = screen_dimension_width/2,
                                                        height= screen_dimension_height/1.5,
                                                        border_width= 10,
                                                        corner_radius= 10,
                                                        border_color="#000206",
                                                        fg_color="#030c49")
        
        self.account_frame.pack_propagate(False)

        create_account_label = customtkinter.CTkLabel(self.account_frame, text="Create an Account", text_color="yellow",font=("Arial", 22, "bold"))
        create_account_label.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        script_dir = Path(__file__).parent
        project_root = script_dir.parent
        image_path = project_root / "images" / "Vaulture.png"


        self.vulture = customtkinter.CTkImage(
            Image.open(image_path),
            size = (185,185)
        )


        vulture_label = customtkinter.CTkLabel(self.login_frame, text = "", image=self.vulture)
        vulture_label.pack(pady=10)

        title_label = customtkinter.CTkLabel(self.login_frame, text= "VAULTURE", text_color="yellow", font= ("Arial", 22, "bold"))
        title_label.place(relx= 0.5, rely= 0.35, anchor= tkinter.CENTER)


        username_label = customtkinter.CTkLabel(self.login_frame, text= "Username", font=("Courier", 16, "bold"), text_color="yellow")
        username_label.place(relx= 0.5, rely= 0.4, anchor= tkinter.CENTER)

        self.username_entry = customtkinter.CTkEntry(self.login_frame, placeholder_text= "Enter Username",
                                        width = 150,
                                        height = 30,
                                        border_width= 1,
                                        corner_radius= 10)
        self.username_entry.place(relx = 0.5, rely = 0.45, anchor = tkinter.CENTER)


        password_label = customtkinter.CTkLabel(self.login_frame, text= "Password", font=("Courier", 16, "bold"), text_color="yellow")
        password_label.place(relx= 0.5, rely= 0.5, anchor= tkinter.CENTER)

        self.password_entry = customtkinter.CTkEntry(self.login_frame, show="*", placeholder_text="Enter Password",
                                        width= 150,
                                        height= 30,
                                        border_width= 1,
                                        corner_radius= 10)
        self.password_entry.place(relx= 0.5, rely= 0.55, anchor= tkinter.CENTER)

        account_label = customtkinter.CTkLabel(self.login_frame, text="Don't have an account? Create one by clicking the 'Sign Up' button", font= ("Courier", 12, "bold"), text_color="yellow")
        account_label.place(relx= 0.5, rely= 0.6, anchor= tkinter.CENTER)

        login_button = customtkinter.CTkButton(self.login_frame, text="Login", fg_color="yellow", text_color="black", command = self.confirm_login)
        login_button.place(x=225, rely= 0.65)

        sign_up_button = customtkinter.CTkButton(self.login_frame, text="Sign Up", fg_color="yellow", text_color="black", command= lambda: self.show_create_account_frame())
        sign_up_button.place(x=380, rely= 0.65)

        new_username_label = customtkinter.CTkLabel(self.account_frame, text= "Username", font=("Courier", 16, "bold"), text_color="yellow")
        new_username_label.place(relx= 0.5, rely= 0.25, anchor= tkinter.CENTER)

        self.new_username_entry = customtkinter.CTkEntry(self.account_frame, placeholder_text= "Enter Username",
                                        width = 150,
                                        height = 30,
                                        border_width= 1,
                                        corner_radius= 10)
        self.new_username_entry.place(relx = 0.5, rely = 0.30, anchor = tkinter.CENTER)

        email_label = customtkinter.CTkLabel(self.account_frame, text= "Email", font=("Courier", 16, "bold"), text_color="yellow")
        email_label.place(relx= 0.5, rely= 0.35, anchor= tkinter.CENTER)

        self.email_entry = customtkinter.CTkEntry(self.account_frame, placeholder_text= "Enter Email",
                                        width = 150,
                                        height = 30,
                                        border_width= 1,
                                        corner_radius= 10)
        self.email_entry.place(relx = 0.5, rely = 0.40, anchor = tkinter.CENTER)

        #New password label and entry box
        new_password_label = customtkinter.CTkLabel(self.account_frame, text= "Password", font=("Courier", 16, "bold"), text_color="yellow")
        new_password_label.place(relx= 0.5, rely= 0.45, anchor= tkinter.CENTER)

        self.new_password_entry = customtkinter.CTkEntry(self.account_frame, show="*", placeholder_text="Enter Password",
                                        width= 150,
                                        height= 30,
                                        border_width= 1,
                                        corner_radius= 10)
        self.new_password_entry.place(relx= 0.5, rely= 0.50, anchor= tkinter.CENTER)

        confirm_password_label = customtkinter.CTkLabel(self.account_frame, text= "Confirm Password", font=("Courier", 16, "bold"), text_color="yellow")
        confirm_password_label.place(relx= 0.5, rely= 0.55, anchor= tkinter.CENTER)

        self.confirm_password_entry = customtkinter.CTkEntry(self.account_frame, show="*", placeholder_text="Enter Password Again",
                                        width= 150,
                                        height= 30,
                                        border_width= 1,
                                        corner_radius= 10)
        self.confirm_password_entry.place(relx= 0.5, rely= 0.60, anchor= tkinter.CENTER)

        create_account_button = customtkinter.CTkButton(self.account_frame, text="Create Account", fg_color="yellow", text_color="black", command = self.save_account_info)
        create_account_button.place(x=315, rely= 0.65)

        back_button = customtkinter.CTkButton(self.account_frame, text="Back", fg_color="yellow", text_color="black", command= lambda: self.show_login_frame())
        back_button.pack(side="bottom", padx = 20, pady= 20, anchor = "w")

        #Show and hide password switches
        self.show_password_var = customtkinter.StringVar(value = "off")
        self.show_password_button = customtkinter.CTkSwitch(self.account_frame, variable= self.show_password_var, text="Show", onvalue="on", offvalue="off", command = self.show_password)
        self.show_password_button.place(x= 470, y= 308)

        self.show_password_var = customtkinter.StringVar(value = "off")
        self.show_confirm_password_button = customtkinter.CTkSwitch(self.account_frame, variable= self.show_password_var, text="Show", onvalue="on", offvalue="off", command = self.show_confirm_password)
        self.show_confirm_password_button.place(x= 470, y= 370)

        self.show_password_var = customtkinter.StringVar(value = "off")
        self.show_password_button_login = customtkinter.CTkSwitch(self.login_frame, variable= self.show_password_var, text="Show", onvalue="on", offvalue="off", command = self.show_password_login)
        self.show_password_button_login.place(x= 470, y= 338)

        self.rules_label = customtkinter.CTkLabel(self.account_frame, text = "• Email Must have @ \n • Password must contain atleast one\nspecial character and atleast one number", text_color="yellow", font=("Courier", 12, "bold"))
        self.rules_label.pack(padx = 20, pady= 20, anchor= "e")

        self.username_error_label = None
        self.email_error_label = None
        self.password_error_label = None
        self.confirm_password_error_label = None
        self.successful_account = None
        self.login_username_error = None
        self.login_password_error = None

    #Show and hide password for all password entry boxes
    def show_password(self):
        if self.new_password_entry.cget("show") == "*":
            self.new_password_entry.configure(show="")
            self.show_password_button.configure(text = "Hide")
        else:
            self.new_password_entry.configure(show="*")
            self.show_password_button.configure(text="Show")

    def show_confirm_password(self):
        if self.confirm_password_entry.cget("show") == "*":
            self.confirm_password_entry.configure(show="")
            self.show_confirm_password_button.configure(text = "Hide")
        else:
            self.confirm_password_entry.configure(show="*")
            self.show_confirm_password_button.configure(text="Show")

    def show_password_login(self):
        if self.password_entry.cget("show") == "*":
            self.password_entry.configure(show="")
            self.show_password_button_login.configure(text = "Hide")
        else:
            self.password_entry.configure(show="*")
            self.show_password_button_login.configure(text="Show")

    #Move between login_frame and create_account frame
    def show_create_account_frame(self):
            self.login_frame.pack_forget()
            self.account_frame.pack(padx=20, pady= 20)

    def show_login_frame(self):
            self.account_frame.pack_forget()
            self.login_frame.pack(padx=20, pady= 20)
            self.new_username_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.password_entry.delete(0, "end")

    #Save account info into a text file and checks if any errors arise when creating an account
    def save_account_info(self):
        username = self.new_username_entry.get()
        email = self.email_entry.get()
        password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        contains_number = any(char.isdigit() for char in password)
        contains_special = any(char in string.punctuation for char in password)

        if self.username_error_label is not None:
            self.username_error_label.destroy()
            self.username_error_label = None

        if self.email_error_label is not None:
            self.email_error_label.destroy()
            self.email_error_label = None

        if self.confirm_password_error_label is not None:
            self.confirm_password_error_label.destroy()
            self.confirm_password_error_label = None

        if self.password_error_label is not None:
            self.password_error_label.destroy()
            self.password_error_label = None

        error = False

        if username == "":
            self.username_error_label = customtkinter.CTkLabel(self.account_frame, text="Please Enter A Valid Username", font=("Courier", 14, "bold"), text_color="red")
            self.username_error_label.pack(padx=20, pady=15, anchor="w")
            error = True
            print("username error")

        if email == "" or "@" not in email:
            self.email_error_label = customtkinter.CTkLabel(self.account_frame, text="Please Enter A Valid Email", font=("Courier", 14, "bold"), text_color="red")
            self.email_error_label.pack(padx=20, pady=15, anchor="w")
            error = True
            print("email error")

        if password == "" or password != confirm_password or (not contains_number or not contains_special):
            self.password_error_label = customtkinter.CTkLabel(self.account_frame, text="Please Enter a Valid Password or\ncheck if password entries match", font=("Courier", 14, "bold"), text_color="red")
            self.password_error_label.pack(padx=20, pady=15, anchor="w")
            error=True


        if not error:
            with open("Account_info" , "w") as file:
                file.write(f"Username: {username}\nEmail: {email}\nPassword: {password}\n\n")
            self.account_frame.pack_forget()
            self.login_frame.pack(padx=20, pady= 20)
            self.new_username_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.new_password_entry.delete(0, "end")
            self.confirm_password_entry.delete(0, "end")
            self.successful_account = customtkinter.CTkLabel(self.login_frame, text="Successfully Created Account!", font=("Courier", 14, "bold"), text_color="green")
            self.successful_account.pack(padx=20, pady=15, anchor="w")

    #Error handling in main login frame and checks if login information is correct
    def confirm_login(self):
        with open("Account_info", "r") as file:
            lines = file.readlines()
            line_one = lines[1-1].split(":")[1].strip()
            line_three = lines[3-1].split(":")[1].strip()
            print(line_one + "\n" + line_three)

            login_username = self.username_entry.get()
            login_password = self.password_entry.get()

            if self.login_username_error is not None:
                self.login_username_error.destroy()
                self.login_username_error = None

            if self.login_password_error is not None:
                self.login_password_error.destroy()
                self.login_password_error = None

            error = False

            if login_username != line_one:
                self.login_username_error = customtkinter.CTkLabel(self.login_frame, text="Username not found", font=("Courier", 14, "bold"), text_color="red")
                self.login_username_error.pack(padx=20, pady=15, anchor="w")
                error = True

            if login_password != line_three:
                self.login_password_error = customtkinter.CTkLabel(self.login_frame, text="Password not found", font=("Courier", 14, "bold"), text_color="red")
                self.login_password_error.pack(padx=20, pady=15, anchor="w")
                error = True

            if not error:
                print("Success")


    # def open_main_page(self):
    #         window.window.deiconify()
    #         self.withdraw()




    def close(self):
        print("closed")
        self.destroy()



if __name__ == "__main__":
    window_login = Login_Page()
    try:
        window_login.mainloop()
    except KeyboardInterrupt:
        print("Window Closed")
