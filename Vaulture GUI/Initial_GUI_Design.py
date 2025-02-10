import customtkinter
from PIL import Image
import tkinter

class Login_Page(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        self.title("Vaulture")


        #Retrieve screen width and height
        screen_dimension_width = self.winfo_screenwidth()
        screen_dimension_height = self.winfo_screenheight()

        self.geometry(f"{screen_dimension_width}x{screen_dimension_height}-10+0")

        self.login_frame = customtkinter.CTkFrame(master=self,
                                     width = screen_dimension_width/2,
                                     height = screen_dimension_height/1.5,
                                     corner_radius= 15,
                                     bg_color= "yellow")

        self.login_frame.pack(padx = 20, pady = 20)
        self.login_frame.pack_propagate(False)

        self.account_frame = customtkinter.CTkFrame(self, width = screen_dimension_width/2,
                                                      height= screen_dimension_height/1.5,
                                                      corner_radius= 15,
                                                      bg_color= "yellow")
        
        self.account_frame.pack_propagate(False)


        self.vulture = customtkinter.CTkImage(
            Image.open("C:/Users/romay/Downloads/imageedit_11_2501753302.png"),
            size = (200,200)
        )

        vulture_label = customtkinter.CTkLabel(self.login_frame, text = "", image=self.vulture)
        vulture_label.pack(pady=5)

        title_label = customtkinter.CTkLabel(self.login_frame, text= "VAULTURE", text_color="yellow", font= ("Arial", 22))
        title_label.place(relx= 0.5, rely= 0.35, anchor= tkinter.CENTER)


        username_label = customtkinter.CTkLabel(self.login_frame, text= "Username", font=("Courier", 16), text_color="yellow")
        username_label.place(relx= 0.5, rely= 0.4, anchor= tkinter.CENTER)

        username_entry = customtkinter.CTkEntry(self.login_frame, placeholder_text= "Enter Username",
                                        width = 150,
                                        height = 30,
                                        border_width= 1,
                                        corner_radius= 10)
        username_entry.place(relx = 0.5, rely = 0.45, anchor = tkinter.CENTER)


        password_label = customtkinter.CTkLabel(self.login_frame, text= "Password", font=("Courier", 16), text_color="yellow")
        password_label.place(relx= 0.5, rely= 0.5, anchor= tkinter.CENTER)

        password_entry = customtkinter.CTkEntry(self.login_frame, placeholder_text="Enter Password",
                                        width= 150,
                                        height= 30,
                                        border_width= 1,
                                        corner_radius= 10)
        password_entry.place(relx= 0.5, rely= 0.55, anchor= tkinter.CENTER)

        account_label = customtkinter.CTkLabel(self.login_frame, text="Don't have an account? Create one by clicking the 'Sign Up' button", font= ("Courier", 12), text_color="yellow")
        account_label.place(relx= 0.5, rely= 0.6, anchor= tkinter.CENTER)

        login_button = customtkinter.CTkButton(self.login_frame, text="Login", fg_color="yellow", text_color="black")
        login_button.place(x=230, rely= 0.65)

        sign_up_button = customtkinter.CTkButton(self.login_frame, text="Sign Up", fg_color="yellow", text_color="black", command= lambda: self.show_create_account_frame())
        sign_up_button.place(x=400, rely= 0.65)

    def show_create_account_frame(self):
            self.login_frame.pack_forget()
            self.account_frame.pack(padx=20, pady= 20)



if __name__ == "__main__":
    window = Login_Page()
    window.mainloop()
