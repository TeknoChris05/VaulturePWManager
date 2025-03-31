import customtkinter
from Initial_GUI_Design import Login_Page


class Account_Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Retrieve screen width and height
        screen_dimension_width = self.winfo_screenwidth()
        screen_dimension_height = self.winfo_screenheight()

        self.account_frame.configure(width= screen_dimension_width/2,
                        height= screen_dimension_height / 1.5,
                        corner_radius=15,
                        bg_color="yellow")

        self.pack_propagate(False)

        self.label = customtkinter.CTkLabel(self, text="Account Frame", text_color="white", font=("Arial", 20))
        self.label.pack(pady=20)