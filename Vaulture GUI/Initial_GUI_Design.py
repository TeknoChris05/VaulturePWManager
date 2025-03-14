
import customtkinter
from PIL import Image
import tkinter
import os
from pathlib import Path


class Login_Page(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        self.title("Vaulture")
        self.configure(fg_color="#0d133e")


        #Retrieve screen width and height
        self.minsize(800, 600) 
        self.maxsize(1920, 1080)
        screen_dimension_width = self.winfo_screenwidth()
        screen_dimension_height = self.winfo_screenheight()

        x_pos = ((screen_dimension_width-self.winfo_screenwidth()) // 2) -10
        y_pos = ((screen_dimension_height-self.winfo_screenheight()) // 2) -1

        self.geometry(f"{screen_dimension_width}x{screen_dimension_height}+{x_pos}+{y_pos}")
        self.pack_propagate(False)\

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

        username_entry = customtkinter.CTkEntry(self.login_frame, placeholder_text= "Enter Username",
                                        width = 150,
                                        height = 30,
                                        border_width= 1,
                                        corner_radius= 10)
        username_entry.place(relx = 0.5, rely = 0.45, anchor = tkinter.CENTER)


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

        login_button = customtkinter.CTkButton(self.login_frame, text="Login", fg_color="yellow", text_color="black")
        login_button.place(x=225, rely= 0.65)

        sign_up_button = customtkinter.CTkButton(self.login_frame, text="Sign Up", fg_color="yellow", text_color="black", command= lambda: self.show_create_account_frame())
        sign_up_button.place(x=380, rely= 0.65)

        new_username_label = customtkinter.CTkLabel(self.account_frame, text= "Username", font=("Courier", 16, "bold"), text_color="yellow")
        new_username_label.place(relx= 0.5, rely= 0.25, anchor= tkinter.CENTER)

        new_username_entry = customtkinter.CTkEntry(self.account_frame, placeholder_text= "Enter Username",
                                        width = 150,
                                        height = 30,
                                        border_width= 1,
                                        corner_radius= 10)
        new_username_entry.place(relx = 0.5, rely = 0.30, anchor = tkinter.CENTER)

        email_label = customtkinter.CTkLabel(self.account_frame, text= "Email", font=("Courier", 16, "bold"), text_color="yellow")
        email_label.place(relx= 0.5, rely= 0.35, anchor= tkinter.CENTER)

        email_entry = customtkinter.CTkEntry(self.account_frame, placeholder_text= "Enter Email",
                                        width = 150,
                                        height = 30,
                                        border_width= 1,
                                        corner_radius= 10)
        email_entry.place(relx = 0.5, rely = 0.40, anchor = tkinter.CENTER)

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

        create_account_button = customtkinter.CTkButton(self.account_frame, text="Create Account", fg_color="yellow", text_color="black")
        create_account_button.place(x=315, rely= 0.65)

        back_button = customtkinter.CTkButton(self.account_frame, text="Back", fg_color="yellow", text_color="black", command= lambda: self.show_login_frame())
        back_button.place(x=30, y=580)

        self.show_password_var = customtkinter.StringVar(value = "off")
        self.show_password_button = customtkinter.CTkSwitch(self.account_frame, variable= self.show_password_var, text="Show", onvalue="on", offvalue="off", command = self.show_password)
        self.show_password_button.place(x= 470, y= 308)

        self.show_password_var = customtkinter.StringVar(value = "off")
        self.show_confirm_password_button = customtkinter.CTkSwitch(self.account_frame, variable= self.show_password_var, text="Show", onvalue="on", offvalue="off", command = self.show_confirm_password)
        self.show_confirm_password_button.place(x= 470, y= 370)

        self.show_password_var = customtkinter.StringVar(value = "off")
        self.show_password_button_login = customtkinter.CTkSwitch(self.login_frame, variable= self.show_password_var, text="Show", onvalue="on", offvalue="off", command = self.show_password_login)
        self.show_password_button_login.place(x= 470, y= 338)



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

    def close(self):
        print("closed")
        self.destroy()



if __name__ == "__main__":
    window = Login_Page()
    try:
        window.mainloop()
    except KeyboardInterrupt:
        print("Window Closed")
