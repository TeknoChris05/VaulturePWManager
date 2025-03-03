import customtkinter
from tkinter import colorchooser


class SettingsApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.state("zoomed")  # Fullscreen mode
        self.configure(fg_color="gray")

        self.theme_color = "gold"  # Default color
        self.text_color = "black"  # Default text color

        self.current_frame = None  
        self.show_settings_page()  

    def show_settings_page(self):
        """Displays the main settings page."""
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = SettingsFrame(self)
        self.current_frame.pack(fill="both", expand=True)

    def show_security_page(self):
        """Displays the security settings page."""
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = SecurityFrame(self)
        self.current_frame.pack(fill="both", expand=True)

    def show_themes_page(self):
        """Displays the themes page."""
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = ThemesFrame(self)
        self.current_frame.pack(fill="both", expand=True)

    def update_theme(self, new_color):
        """Updates the theme color and adjusts text color for readability."""
        self.theme_color = new_color
        self.text_color = self.get_readable_text_color(new_color)
        self.show_settings_page()  

    def get_readable_text_color(self, bg_color):
        """Determines whether text should be black or white based on background brightness."""
        bg_color = bg_color.lstrip("#")
        r, g, b = int(bg_color[0:2], 16), int(bg_color[2:4], 16), int(bg_color[4:6], 16)
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        return "black" if brightness > 128 else "white"


class SettingsFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="gray")

        title = customtkinter.CTkLabel(self, text="Settings", text_color=master.text_color,
                                       font=("Arial", 24, "bold"), fg_color=master.theme_color, height=60)
        title.pack(fill="x")

        sections = [
            ("Security", master.show_security_page),
            ("Account Change", None),
            ("Themes", master.show_themes_page),
            "",
            ("Help", None),
            ("Contact", None)
        ]

        for section in sections:
            if isinstance(section, tuple):
                button = customtkinter.CTkButton(self, text=section[0], text_color=master.text_color,
                                                 font=("Arial", 18), fg_color=master.theme_color,
                                                 hover_color="#d4af37", corner_radius=0,
                                                 command=section[1] if section[1] else None)
            elif section:
                button = customtkinter.CTkButton(self, text=section, text_color=master.text_color,
                                                 font=("Arial", 18), fg_color=master.theme_color,
                                                 hover_color="#d4af37", corner_radius=0)
            else:
                button = customtkinter.CTkLabel(self, text="", fg_color="gray", height=20)

            button.pack(fill="x", padx=20, pady=5, expand=True)


class SecurityFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="gray")

        title = customtkinter.CTkLabel(self, text="Security Settings", text_color=master.text_color,
                                       font=("Arial", 24, "bold"), fg_color=master.theme_color, height=60)
        title.pack(fill="x")

        label = customtkinter.CTkLabel(self, text="Enable Two-Factor Authentication (2FA)", 
                                       font=("Arial", 18), text_color="white")
        label.pack(pady=20)

        self.two_fa_switch = customtkinter.CTkSwitch(self, text="2FA", fg_color=master.theme_color,
                                                     text_color=master.text_color)
        self.two_fa_switch.pack(pady=10)

        back_button = customtkinter.CTkButton(self, text="Back", fg_color=master.theme_color, hover_color="#d4af37",
                                              text_color=master.text_color, command=master.show_settings_page)
        back_button.pack(pady=20)


class ThemesFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="gray")

        title = customtkinter.CTkLabel(self, text="Themes", text_color=master.text_color,
                                       font=("Arial", 24, "bold"), fg_color=master.theme_color, height=60)
        title.pack(fill="x")

        label = customtkinter.CTkLabel(self, text="Choose a Theme Color", 
                                       font=("Arial", 18), text_color="white")
        label.pack(pady=20)

        self.color_button = customtkinter.CTkButton(self, text="Pick Color", fg_color=master.theme_color, 
                                                    hover_color="#d4af37", text_color=master.text_color, 
                                                    command=self.pick_color)
        self.color_button.pack(pady=10)

        back_button = customtkinter.CTkButton(self, text="Back", fg_color=master.theme_color, hover_color="#d4af37",
                                              text_color=master.text_color, command=master.show_settings_page)
        back_button.pack(pady=20)

    def pick_color(self):
        """Opens a color picker and updates the theme."""
        color_code = colorchooser.askcolor(title="Choose Theme Color")[1]  
        if color_code:
            self.master.update_theme(color_code)  


# Run the app
app = SettingsApp()
app.mainloop()
