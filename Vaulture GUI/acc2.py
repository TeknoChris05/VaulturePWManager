import customtkinter
import subprocess
import sys
import colorsys
from tkinter import colorchooser

import mysql.connector
from PIL import Image, ImageTk
from PIL._tkinter_finder import tk

account_id = sys.argv[1] if len(sys.argv) > 1 else None

login_database = mysql.connector.connect(
    host="db-mysql-nyc3-37387-do-user-15222509-0.l.db.ondigitalocean.com",
    user="doadmin",
    passwd='AVNS_AK8FErb1DuSyVpZeMZR',
    port='25060',
    database="Vaulturedb"
)

mycursor = login_database.cursor()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class SettingsApp(customtkinter.CTkToplevel):
    def __init__(self, update_callback=None,
                 parent=None):  # This update_callback=None was used by ai to make it so it can be used in the main.py file to update the theme color in the main.py file
        super().__init__()
        self.parent = parent
        self.update_callback = update_callback
        screen_dimension_width = self.winfo_screenwidth()
        screen_dimension_height = self.winfo_screenheight()
        self.geometry(f"{screen_dimension_width}x{screen_dimension_height}-10+0")
        self.configure(fg_color="#2C2F33")
        self.minsize(800, 600)
        self.maxsize(1920, 1080)
        self.theme_color = "#2C2F33"
        self.text_color = "white"
        self.current_frame = None
        self._create_sidebar()
        self.show_Intro_page()
        Exit_button = customtkinter.CTkButton(self, text="Exit", command=self.Saving)
        Exit_button.pack(side="bottom", pady=100)
        self.lift()
        self.focus_force()
        self.grab_set()
        self.load_theme()

    def _create_sidebar(self):
        self.sidebar = customtkinter.CTkFrame(self, fg_color="#23272A", width=200, corner_radius=10)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)
        title = customtkinter.CTkLabel(self.sidebar, text="Vaulture", font=("Segoe UI", 24, "bold"),
                                       text_color="#FFFFFF", fg_color="#23272A")
        title.pack(pady=20)

        buttons = [
            ("👤 Account", self.show_account_page),
            ("🔒 Security", self.show_security_page),
            ("🎨 Themes", self.show_themes_page),
            ("ℹ️ Help", self.show_Help_page),
            ("✉️ Contact", self.show_Contact_page),
        ]

        for text, command in buttons:
            button = customtkinter.CTkButton(self.sidebar, text=text, font=("Segoe UI", 18), fg_color="#2C2F33",
                                             hover_color="#7289DA", text_color="#FFFFFF", command=command,
                                             corner_radius=10, border_width=2, border_color="#7289DA")
            button.pack(fill="x", padx=10, pady=10)

    # Sidebar Diff Shade
    def _darken_color(self, hex_color, factor=0.8):
        hex_color = hex_color.lstrip("#")
        r, g, b = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
        h, l, s = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
        l = max(0, min(1, l * factor))
        r, g, b = colorsys.hls_to_rgb(h, l, s)

        return f"#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}"

    def update_theme(self, new_color):
        self.theme_color = new_color
        self.configure(fg_color=new_color)
        self.sidebar.configure(fg_color=new_color)

        darker_color = self._darken_color(new_color, 0.8)
        self.sidebar.configure(fg_color=darker_color)

        for widget in self.sidebar.winfo_children():
            if isinstance(widget, customtkinter.CTkButton):
                widget.configure(fg_color=new_color)

        title_label = self.sidebar.winfo_children()[0]
        if isinstance(title_label, customtkinter.CTkLabel):
            title_label.configure(fg_color=new_color)

        if self.current_frame:
            self.current_frame.configure(fg_color=new_color)
            for widget in self.current_frame.winfo_children():
                if isinstance(widget, (customtkinter.CTkButton, customtkinter.CTkLabel, customtkinter.CTkSwitch)):
                    widget.configure(fg_color=self.theme_color,
                                     text_color="black" if self.theme_color == "#FFFFFF" else "white")
                elif isinstance(widget, customtkinter.CTkFrame):
                    widget.configure(fg_color=self.theme_color)

        self.refresh_current_frame()

    def refresh_current_frame(self):
        # Recreate Frame and Apply changes
        if self.current_frame:
            frame_class = type(self.current_frame)
            self.current_frame.destroy()
            self.current_frame = frame_class(self)
            self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def show_Intro_page(self):
        self._switch_frame(IntroFrame)

    def show_account_page(self):
        self._switch_frame(AccountFrame)

    def show_security_page(self):
        self._switch_frame(SecurityFrame)

    def show_themes_page(self):
        self._switch_frame(ThemesFrame)

    def show_Help_page(self):
        self._switch_frame(HelpFrame)

    def show_Contact_page(self):
        self._switch_frame(ContactFrame)

    def _switch_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.destroy()

        if frame_class == AccountFrame:
            self.current_frame = frame_class(self, self.parent)
        else:
            self.current_frame = frame_class(self)

        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Theme Color Update
        self.current_frame.configure(fg_color=self.theme_color)
        for widget in self.current_frame.winfo_children():
            if isinstance(widget, (customtkinter.CTkButton, customtkinter.CTkLabel)):
                widget.configure(fg_color=self.theme_color,
                                 text_color="black" if self.theme_color == "#FFFFFF" else "white")
            elif isinstance(widget, customtkinter.CTkFrame):
                widget.configure(fg_color=self.theme_color)

    def save_theme_(self):
        with open("theme_settings.txt", "w") as file:
            file.write(self.theme_color)

    def load_theme(self):
        try:
            with open("theme_settings.txt", "r") as file:
                saved_color = file.read().strip()
                if saved_color:
                    self.update_theme(saved_color)
        except FileNotFoundError:
            pass

    #######################################################################################################################################
    # Used ai to edit what i already had here to make it so it saves to dan.py as well https://chatgpt.com/share/67f19bc3-4ab8-800a-bfaa-5ae77d2372a2
    def Saving(self):
        self.save_theme_()
        if self.update_callback:
            try:
                self.update_callback(self.theme_color)
            except Exception as e:
                print("Failed to update main theme:", e)
        self.destroy()


#######################################################################################################################################


class IntroFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#2C2F33", border_width=0, border_color="#7289DA")
        self.configure(fg_color=master.theme_color)

        title = customtkinter.CTkLabel(self, text="Settings", text_color=master.text_color,
                                       font=("Segoe UI", 28, "bold"), fg_color=master.theme_color, height=60)
        title.pack(fill="x")

        contact_text = """Welcome to the settings page! """

        label = customtkinter.CTkLabel(self, text=contact_text, text_color="white", justify="left",
                                       font=("Segoe UI", 16), wraplength=600)
        label.pack(pady=20, padx=20)


class AccountFrame(customtkinter.CTkFrame):
    def __init__(self, master, parent):
        super().__init__(master)
        self.parent = parent
        self.configure(fg_color="#2C2F33", corner_radius=10)

        title = customtkinter.CTkLabel(self, text="Account Information", text_color="white",
                                       font=("Segoe UI", 28, "bold"), fg_color="#2C2F33")
        title.pack(pady=10)

        self.text_widget = customtkinter.CTkTextbox(self, height=200, width=400, font=("Arial", 16))
        self.text_widget.pack(pady=10, padx=10)

        self.load_Account_Info()

        Erase_button = customtkinter.CTkButton(self, text="Erase Account?", fg_color=master.theme_color,
                                               hover_color="#d4af37", text_color=master.text_color, corner_radius=10,
                                               border_width=2, border_color="#7289DA", width=60, height=70)
        Erase_button.pack(pady=20)

        logout_button = customtkinter.CTkButton(self, text="Logout", fg_color=master.theme_color, hover_color="#d4af37",
                                                text_color=master.text_color, command=self.logout, corner_radius=10,
                                                border_width=2, border_color="#7289DA")
        logout_button.pack(pady=20)

        back_button = customtkinter.CTkButton(self, text="Back", fg_color=master.theme_color, hover_color="#d4af37",
                                              text_color=master.text_color, command=master.show_Intro_page,
                                              corner_radius=10, border_width=2, border_color="#7289DA")
        back_button.pack(pady=20)

    def load_Account_Info(self):
        mycursor.execute(
            "SELECT Username, Email, Password FROM Account WHERE AccountID = %s",
            (account_id,))

        data = mycursor.fetchall()

        if data:
            for index, row in enumerate(data):
                username, email, password = row
                display_password_text = f"{index + 1}. Username: {username} | Email: {email} | Password: {password}"
                self.text_widget.insert("end", display_password_text)

    def logout(self):
        try:
            # Launch the login page when logging out
            subprocess.Popen([sys.executable, "Initial_GUI_Design.py"])
        except Exception as e:
            print(f"Error launching login page: {e}")

        # Destroy both windows
        try:
            if hasattr(self, "master") and self.master.winfo_exists():
                self.master.destroy()
        except Exception as e:
            print(f"Error closing master window: {e}")

        try:
            self.destroy()
        except Exception as e:
            print(f"Error closing current window: {e}")

        try:
            if self.parent:
                self.parent.quit()
                self.parent.destroy()
        except Exception as e:
            print(f"Error closing parent window: {e}")


class SecurityFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=master.theme_color, border_width=0, border_color="#7289DA")

        title = customtkinter.CTkLabel(self, text="Security Settings", text_color=master.text_color,
                                       font=("Segoe UI", 28, "bold"), fg_color=master.theme_color, height=60)
        title.pack(fill="x")
        label = customtkinter.CTkLabel(self, text="Enable Two-Factor Authentication (2FA)", font=("Segoe UI", 18),
                                       text_color="white")
        label.pack(pady=20)

        self.twofa_frame = customtkinter.CTkFrame(self, fg_color=master.theme_color, border_width=2,
                                                  border_color="#7289DA", corner_radius=10)
        self.twofa_frame.pack(pady=10, padx=20, fill="x")

        self.twofa_switch = customtkinter.CTkSwitch(self.twofa_frame, text="Enable 2FA", fg_color=master.theme_color,
                                                    text_color=master.text_color)
        self.twofa_switch.pack(pady=10, padx=10)

        self.recovery_code_button = customtkinter.CTkButton(self, text="Generate Recovery Codes",
                                                            fg_color=master.theme_color, hover_color="#d4af37",
                                                            text_color=master.text_color, corner_radius=10,
                                                            border_width=2, border_color="#7289DA")
        self.recovery_code_button.pack(pady=10)

        back_button = customtkinter.CTkButton(self, text="Back", fg_color=master.theme_color, hover_color="#d4af37",
                                              text_color=master.text_color, command=master.show_Intro_page,
                                              corner_radius=10, border_width=2, border_color="#7289DA")
        back_button.pack(pady=20)


class ThemesFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#2C2F33", border_width=0, border_color="#7289DA")
        self.configure(fg_color=master.theme_color)

        title = customtkinter.CTkLabel(self, text="Themes", text_color=master.text_color, font=("Segoe UI", 28, "bold"),
                                       fg_color=master.theme_color, height=60)
        title.pack(fill="x")

        self.color_button = customtkinter.CTkButton(self, text="Pick Theme Color", border_width=2,
                                                    border_color="#7289DA", fg_color=master.theme_color,
                                                    hover_color="#d4af37", text_color=master.text_color,
                                                    command=self.pick_color)
        self.color_button.pack(pady=10)

        self.Font_button = customtkinter.CTkButton(self, text="Change Font Color", border_width=2,
                                                   border_color="#7289DA", fg_color=master.theme_color,
                                                   hover_color="#d4af37", text_color=master.text_color)
        self.Font_button.pack(pady=10)

        self.reset_button = customtkinter.CTkButton(self, text="Click For Default Theme", border_width=2,
                                                    border_color="#7289DA", fg_color=master.theme_color,
                                                    hover_color="#d4af37", text_color=master.text_color,
                                                    command=self.reset_theme)
        self.reset_button.pack(pady=10)

        back_button = customtkinter.CTkButton(self, text="Back", fg_color=master.theme_color, hover_color="#d4af37",
                                              text_color=master.text_color, command=master.show_Intro_page,
                                              corner_radius=10, border_width=2, border_color="#7289DA")
        back_button.pack(pady=20)

    def pick_color(self):
        color_code = colorchooser.askcolor(title="Choose Theme Color")[1]
        if color_code:
            self.master.update_theme(color_code)

    # This will Reset the theme to the original color
    def reset_theme(self):
        # Og Color for settings page
        OG_settings_color = "#2C2F33"
        self.master.update_theme(OG_settings_color)


class HelpFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#2C2F33", border_width=0, border_color="#7289DA")
        self.configure(fg_color=master.theme_color)

        # Help Title
        title = customtkinter.CTkLabel(self, text="Help", text_color=master.text_color, font=("Segoe UI", 28, "bold"),
                                       fg_color=master.theme_color, height=60)
        title.pack(fill="x", pady=(10, 10))

        # Adding a border around the helpful tips message
        help_message = "Here are some helpful tips!"

        # "Here are some helpful tips!" message with a border
        help_message_frame = customtkinter.CTkFrame(self, fg_color=master.theme_color, border_width=2,
                                                    border_color="#7289DA", corner_radius=10)
        help_message_frame.pack(padx=20, pady=(10, 20), fill="x")

        help_message_label = customtkinter.CTkLabel(help_message_frame, text=help_message, text_color="white",
                                                    font=("Segoe UI", 20, "bold"), fg_color=master.theme_color)
        help_message_label.pack(pady=10, padx=20)

        # Adding a border around tips menu
        text_frame = customtkinter.CTkFrame(self, fg_color="#2C2F33", border_width=2, border_color="#7289DA",
                                            corner_radius=10)
        text_frame.pack(padx=20, pady=(0, 50), fill="both", expand=True)

        scroll_frame = customtkinter.CTkScrollableFrame(text_frame, fg_color=master.theme_color)
        scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
        text_frame = scroll_frame

        contact_text = [
            ("How do I make passwords?", "Click the waffle at the bottom of the screen and all the options are there!"),
            ("How can I see my passwords?", "Go hit the bird towards the bottom of the main page icon to display!"),
            ("How do I enable 2FA?", "Go to the security page and click the switch to enable 2FA!"),
            ("How do I contact you?", "Go to the contact page and all the emails are displayed."),
            ("How can I see my passwords?", "Go hit the bird icon to display them!"),
            ("Can I make a profile picture and profile name?",
             "Yes! Go to the Profile Page on the bottom bar and you can change it there!"),
            ("How do I change the theme?", "Go to the Themes page and click the button to change the theme color!"),
        ]

        # Question will make bold answer will stay regular
        for question, answer in contact_text:
            # If question it will make bold
            question_label = customtkinter.CTkLabel(text_frame, text=f"• {question}", text_color="white",
                                                    font=("Segoe UI", 16, "bold"), fg_color=master.theme_color,
                                                    anchor="w")
            question_label.pack(pady=(10, 0), padx=20, fill="x")

            # If answer it will stay regular font
            answer_label = customtkinter.CTkLabel(text_frame, text=answer, text_color="white", font=("Segoe UI", 16),
                                                  fg_color=master.theme_color, anchor="w")
            answer_label.pack(pady=(5, 10), padx=40, fill="x")

            # Horizontal Lines
            separator = customtkinter.CTkFrame(text_frame, height=2, fg_color="#7289DA")
            separator.pack(pady=(10, 10), padx=20, fill="x")

        # Back Button
        back_button = customtkinter.CTkButton(self, text="Back", fg_color=master.theme_color, hover_color="#d4af37",
                                              text_color=master.text_color, command=master.show_Intro_page,
                                              corner_radius=10, border_width=2, border_color="#7289DA")
        back_button.pack(pady=(20, 30))


class ContactFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#2C2F33", border_width=0, border_color="#7289DA")
        self.configure(fg_color=master.theme_color)

        # Title
        title = customtkinter.CTkLabel(self, text="Contact Us", text_color=master.text_color,
                                       font=("Segoe UI", 28, "bold"), fg_color=master.theme_color, height=60)
        title.pack(fill="x", pady=(10, 20))

        # Contact Icons
        contact_icons_frame = customtkinter.CTkFrame(self, fg_color=master.theme_color, corner_radius=10)
        contact_icons_frame.pack(pady=(10, 20), padx=20, fill="x")

        # Email icon added email picture and readjusted message says
        icon_data = [
            ("📧", "Need help? Reach out to us through the following emails at any time!")
        ]

        for icon, label_text in icon_data:
            contact_button = customtkinter.CTkButton(contact_icons_frame, text=f"{icon} {label_text}",
                                                     font=("Segoe UI", 17, "bold"), fg_color=master.theme_color,
                                                     hover_color="#d4af37", text_color=master.text_color,
                                                     corner_radius=10, border_width=3, border_color="#7289DA")
            contact_button.pack(pady=5, fill="x", padx=20)

        # Email addresses added border to make it look neat
        email_frame = customtkinter.CTkFrame(self, fg_color=master.theme_color, corner_radius=10, border_width=2,
                                             border_color="#7289DA")
        email_frame.pack(padx=20, pady=(0, 20), fill="x")

        email_list = [
            "martenoromaya@oakland.edu",
            "dromaya@oakland.edu",
            "danieltrpevski@oakland.edu",
            "cgatie@oakland.edu"
        ]

        for email in email_list:
            email_label = customtkinter.CTkLabel(email_frame, text=email, text_color="white", font=("Segoe UI", 14),
                                                 fg_color=master.theme_color, height=40)
            email_label.pack(fill="x", padx=20, pady=5)

        # Back Button
        back_button = customtkinter.CTkButton(self, text="Back", fg_color=master.theme_color, hover_color="#d4af37",
                                              text_color=master.text_color, command=master.show_Intro_page,
                                              corner_radius=10, border_width=2, border_color="#7289DA")
        back_button.pack(pady=(20, 30))

    # This update_callback=None was used by ai to make it so it can be used in the main.py file to update the theme color in the main.py file


def opening_settings(update_callback=None):
    app = SettingsApp(update_callback)
    app.resizable(False, False)