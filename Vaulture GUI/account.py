import customtkinter


class Account_Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        screen_dimension_width = master.winfo_screenwidth()
        screen_dimension_height = master.winfo_screenheight()

        self.configure(width=screen_dimension_width / 2,
                       height=screen_dimension_height / 1.5,
                       corner_radius=15,
                       fg_color="gray")

        self.pack_propagate(False)

        self.label = customtkinter.CTkLabel(self, text="Account Frame", text_color="white", font=("Arial", 20))
        self.label.pack(pady=20)

        self.pack(pady=20)


root = customtkinter.CTk()
root.geometry("800x600")

frame = Account_Frame(root)
frame.pack(expand=True)

root.mainloop()
