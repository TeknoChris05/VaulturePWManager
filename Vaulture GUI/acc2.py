import customtkinter
import subprocess
import sys
import os
import colorsys
from tkinter import colorchooser
import mysql.connector
from PIL import Image, ImageTk
from PIL._tkinter_finder import tk

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
    def __init__(self, update_callback=None , parent = None): # This update_callback=None was used by ai to make it so it can be used in the main.py file to update the theme color in the main.py file
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
        self.current_font = ("Segoe UI", 16)
        self.load_font_color()
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
        title = customtkinter.CTkLabel(self.sidebar, text="Vaulture", font=("Segoe UI", 24, "bold"), text_color="#FFFFFF", fg_color="#23272A")
        title.pack(pady=20)
        
        buttons = [
            ("👤 Account", self.show_account_page),
            ("🎨 Themes", self.show_themes_page),
            ("ℹ️ Help", self.show_Help_page),
            ("✉️ Contact", self.show_Contact_page),
        ]
     
        for text, command in buttons:
            button = customtkinter.CTkButton(self.sidebar, text=text, font=("Segoe UI", 18), fg_color="#2C2F33", hover_color="#7289DA", text_color="#FFFFFF", command=command, corner_radius=10, border_width=2, border_color="#7289DA")
            button.pack(fill="x", padx=10, pady=10)

    #Sidebar Diff Shade        
    def _darken_color(self, hex_color, factor=0.8):
        hex_color = hex_color.lstrip("#")
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
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
                    widget.configure(fg_color=self.theme_color,text_color=self.text_color )
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

    def show_themes_page(self):
        self._switch_frame(ThemesFrame)

    def show_Help_page(self):
        self._switch_frame(HelpFrame)

    def show_Contact_page(self):
        self._switch_frame(ContactFrame)       
 #######################################################################################################################################
# Modified the existing code with ai link down below           
    def _switch_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.destroy()

        if frame_class == AccountFrame:
            self.current_frame = frame_class(self, self.parent)
        else:
            self.current_frame = frame_class(self)

        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Apply background and text color to the current frame widgets
        self.current_frame.configure(fg_color=self.theme_color)
        
        for widget in self.current_frame.winfo_children():
            if isinstance(widget, (customtkinter.CTkButton, customtkinter.CTkLabel)):
                widget.configure(fg_color=self.theme_color, text_color=self.text_color)
            elif isinstance(widget, customtkinter.CTkFrame):
                widget.configure(fg_color=self.theme_color)

        # 🔥 ALSO update sidebar text color every time you switch frame
        for widget in self.sidebar.winfo_children():
            if isinstance(widget, (customtkinter.CTkButton, customtkinter.CTkLabel)):
                widget.configure(text_color=self.text_color)

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
                self.update_callback(self.theme_color, self.text_color)
            except Exception as e:
                print("Failed to update main theme:", e)

        # 🛠 Force main_frame to refresh its color
        if self.parent:
            try:
                self.parent.saved_mainframe_color = self.parent.load_saved_mainframe_color()
                self.parent.main_frame.configure(fg_color=self.parent.saved_mainframe_color)
            except Exception as e:
                print("Failed to update main frame color:", e)

        self.destroy()

    def save_font_color(self):
        try:
            with open("font_color.txt", "w") as file:
                file.write(self.text_color)
        except Exception as e:
            print(f"Failed to save font color: {e}")

    def load_font_color(self):
        try:
            with open("font_color.txt", "r") as file:
                saved_color = file.read().strip()
                if saved_color:
                    self.text_color = saved_color
        except FileNotFoundError:
            self.text_color = "white"
    def save_mainframe_theme(self, color):
        with open("mainframe_theme.txt", "w") as file:
            file.write(color)

    def load_mainframe_theme(self):
        try:
            with open("mainframe_theme.txt", "r") as file:
                saved_color = file.read().strip()
                if saved_color:
                    return saved_color
        except FileNotFoundError:
            return "#A9A9A9"  # Default main frame color
    
                
#######################################################################################################################################
class IntroFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#2C2F33", border_width=0, border_color="#7289DA")
        self.configure(fg_color=master.theme_color)

        title = customtkinter.CTkLabel(self, text="Settings", text_color=master.text_color, font=("Segoe UI", 28, "bold"), fg_color=master.theme_color, height=60)
        title.pack(fill="x")

        contact_text = """Welcome to the settings page! """

        label = customtkinter.CTkLabel(self, text=contact_text, text_color=master.text_color,  justify="left", font=("Segoe UI", 16), wraplength=600)
        label.pack(pady=20, padx=20)

class AccountFrame(customtkinter.CTkFrame):
    def __init__(self, master, parent):
        super().__init__(master)
        self.parent = parent
        self.configure(fg_color="#2C2F33", corner_radius=10)

        title = customtkinter.CTkLabel(self, text="Account Information", text_color="white", font=("Segoe UI", 28, "bold"), fg_color="#2C2F33")
        title.pack(pady=10)

        self.text_widget = customtkinter.CTkTextbox(self, height=200, width=400, font=("Arial", 16))
        self.text_widget.pack(pady=10, padx=10)

        self.load_Account_Info()

        Erase_button = customtkinter.CTkButton(self, text="Erase Account?", fg_color=master.theme_color, hover_color="#FF6666", text_color=master.text_color, command=self.confirm_erase, corner_radius=10, border_width=2, border_color="#FF6666", width=60, height=70)
        Erase_button.pack(pady=20)

        logout_button = customtkinter.CTkButton(self, text="Logout", fg_color=master.theme_color, hover_color="#d4af37", text_color=master.text_color, command=self.logout, corner_radius=10, border_width=2, border_color="#7289DA")
        logout_button.pack(pady=20)


        back_button = customtkinter.CTkButton(self, text="Back", fg_color=master.theme_color, hover_color="#d4af37", text_color=master.text_color, command=master.show_Intro_page, corner_radius=10, border_width=2, border_color="#7289DA")
        back_button.pack(pady=20) 

    def load_Account_Info(self):
        try:
            with open("Account_info", "r") as file:
                content = file.read()
                self.text_widget.delete("1.0", "end")
                self.text_widget.insert("end", content)
        except FileNotFoundError:
            self.text_widget.insert("end", "No account info file found.")

    def logout(self):
        try:
            subprocess.Popen([sys.executable, "Vaulture GUI/Initial_GUI_Design.py"])
        except Exception as e:
            print(f"Error launching login page: {e}")
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
            print(f"Error closing parent window (Dan.py): {e}")

    def confirm_erase(self):
        confirm_window = customtkinter.CTkToplevel(self)
        confirm_window.title("Confirm")
        confirm_window.geometry("400x200")
        confirm_window.configure(fg_color="#2C2F33")
        confirm_window.grab_set()

        label = customtkinter.CTkLabel(
            confirm_window, text="Are you sure you want to erase everything?",
            text_color="white", font=("Segoe UI", 16, "bold")
        )
        label.pack(pady=30)

        button_frame = customtkinter.CTkFrame(confirm_window, fg_color="#2C2F33")
        button_frame.pack(pady=10)

        yes_button = customtkinter.CTkButton(
            button_frame, text="Yes", fg_color="red", hover_color="#ff6666",
            command=lambda: self.erase_account(confirm_window)
        )
        yes_button.pack(side="left", padx=10)

        no_button = customtkinter.CTkButton(
            button_frame, text="No", fg_color="gray", hover_color="#a9a9a9",
            command=confirm_window.destroy
        )
        no_button.pack(side="left", padx=10)

class ThemesFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#2C2F33", border_width=0, border_color="#7289DA")
        self.configure(fg_color=master.theme_color)

        title = customtkinter.CTkLabel(self, text="Themes", text_color=master.text_color, font=("Segoe UI", 28, "bold"), fg_color=master.theme_color, height=60)
        title.pack(fill="x")

        self.color_button = customtkinter.CTkButton(self, text="Pick Theme Color", border_width=2, border_color="#7289DA", fg_color=master.theme_color, hover_color="#d4af37", text_color=master.text_color, command=self.pick_color)
        self.color_button.pack(pady=10)

        self.MainF_button = customtkinter.CTkButton(self, text="Change Main_Frame Color", border_width=2, border_color="#7289DA", fg_color=master.theme_color, hover_color="#d4af37", text_color=master.text_color, command=self.pick_mainframe_color)
        self.MainF_button.pack(pady=10)

        self.Font_button = customtkinter.CTkButton(self, text="Change Font Color", border_width=2, border_color="#7289DA", fg_color=master.theme_color, hover_color="#d4af37", text_color=master.text_color, command=self.pick_font_color)
        self.Font_button.pack(pady=10)

        self.reset_button = customtkinter.CTkButton(self, text="Click For Default Theme", border_width=2, border_color="#7289DA", fg_color=master.theme_color, hover_color="#d4af37", text_color=master.text_color, command=self.reset_theme)
        self.reset_button.pack(pady=10)

        back_button = customtkinter.CTkButton(self, text="Back", fg_color=master.theme_color, hover_color="#d4af37", text_color=master.text_color, command=master.show_Intro_page, corner_radius=10, border_width=2, border_color="#7289DA")
        back_button.pack(pady=20)  

    def pick_color(self):
        color_code = colorchooser.askcolor(title="Choose Theme Color")[1]
        if color_code:
            self.master.update_theme(color_code)
#######################################################################################################################################
#All font and mainframe related code here is ai the rest was existing code
    def pick_font_color(self):
        color_code = colorchooser.askcolor(title="Choose Font Color")[1]
        if color_code:
            try:
                self.master.text_color = color_code
                self.master.save_font_color()

                # Update sidebar (left buttons)
                for widget in self.master.sidebar.winfo_children():
                    if isinstance(widget, (customtkinter.CTkButton, customtkinter.CTkLabel)):
                        widget.configure(text_color=self.master.text_color)

                # Update current frame (right content area)
                if self.master.current_frame:
                    for widget in self.master.current_frame.winfo_children():
                        if isinstance(widget, (customtkinter.CTkButton, customtkinter.CTkLabel, customtkinter.CTkEntry, customtkinter.CTkSwitch, customtkinter.CTkTextbox, customtkinter.CTkScrollableFrame)):
                            widget.configure(text_color=self.master.text_color)

                print(f"Font color changed and saved: {color_code}")
            except Exception as e:
                print(f"Failed to apply font color: {e}")

    def pick_mainframe_color(self):
        color_code = colorchooser.askcolor(title="Choose Main Frame Color")[1]
        if color_code:
            try:
                self.master.save_mainframe_theme(color_code)
                print(f"Main Frame color changed and saved: {color_code}")
            except Exception as e:
                print(f"Failed to apply main frame color: {e}")

# This will Reset the theme to the original color 
    def reset_theme(self):
        # 🔥 Reset Settings window color to default
        OG_settings_color = "#2C2F33" 
        self.master.update_theme(OG_settings_color)

        # 🔥 Reset font color to white
        with open("font_color.txt", "w") as file:
            file.write("white")
        self.master.text_color = "white"

        # 🔥 Reset Main Frame color to default A9A9A9
        default_mainframe_color = "#A9A9A9"
        self.master.save_mainframe_theme(default_mainframe_color)

        # 🔥 Force Vaulture's main_frame to update immediately if open
        if self.master.parent:
            try:
                self.master.parent.saved_mainframe_color = default_mainframe_color
                self.master.parent.main_frame.configure(fg_color=default_mainframe_color)
            except Exception as e:
                print("Failed to reset main frame color:", e)

    def pick_font(self):
        from tkinter import simpledialog

        font_choice = simpledialog.askstring("Pick Font", "Enter font (e.g., 'Arial', 'Courier', 'Verdana'):")
        if font_choice:
            try:
                self.master.current_font = (font_choice, 16)  # Example: ("Arial", 16)

                # Save the font choice
                self.master.save_font()

                # Update sidebar
                for widget in self.master.sidebar.winfo_children():
                    if isinstance(widget, customtkinter.CTkButton) or isinstance(widget, customtkinter.CTkLabel):
                        widget.configure(font=self.master.current_font)

                # Update current frame
                if self.master.current_frame:
                    for widget in self.master.current_frame.winfo_children():
                        if isinstance(widget, (customtkinter.CTkButton, customtkinter.CTkLabel, customtkinter.CTkEntry, customtkinter.CTkSwitch, customtkinter.CTkTextbox)):
                            widget.configure(font=self.master.current_font)

                print(f"Font changed and saved: {font_choice}")
            except Exception as e:
                print(f"Failed to apply font: {e}")
#######################################################################################################################################

class HelpFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#2C2F33", border_width=0, border_color="#7289DA")
        self.configure(fg_color=master.theme_color)

        # Help Title
        title = customtkinter.CTkLabel(self, text="Help", text_color=master.text_color, font=("Segoe UI", 28, "bold"), fg_color=master.theme_color, height=60)
        title.pack(fill="x", pady=(10, 10))

        # Adding a border around the helpful tips message
        help_message = "Here are some helpful tips!"
        
        # "Here are some helpful tips!" message with a border
        help_message_frame = customtkinter.CTkFrame(self, fg_color=master.theme_color, border_width=2, border_color="#7289DA", corner_radius=10)
        help_message_frame.pack(padx=20, pady=(10, 20), fill="x")


        help_message_label = customtkinter.CTkLabel(help_message_frame, text=help_message,  text_color=master.text_color, font=("Segoe UI", 20, "bold"), fg_color=master.theme_color)
        help_message_label.pack(pady=10, padx=20)

        # Adding a border around tips menu
        text_frame = customtkinter.CTkFrame(self, fg_color="#2C2F33", border_width=2, border_color="#7289DA", corner_radius=10)
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
        ("Can I make a profile picture and profile name?", "Yes! Go to the Profile Page on the bottom bar and you can change it there!"),
        ("How do I change the theme?", "Go to the Themes page and click the button to change the theme color!"),
    ]

        # Question will make bold answer will stay regular
        for question, answer in contact_text:
            # If question it will make bold
            question_label = customtkinter.CTkLabel(text_frame, text=f"• {question}", text_color=master.text_color, font=("Segoe UI", 16, "bold"), fg_color=master.theme_color, anchor="w")
            question_label.pack(pady=(10, 0), padx=20, fill="x")

            # If answer it will stay regular font
            answer_label = customtkinter.CTkLabel(text_frame, text=answer,  text_color=master.text_color, font=("Segoe UI", 16), fg_color=master.theme_color, anchor="w")
            answer_label.pack(pady=(5, 10), padx=40, fill="x")

            # Horizontal Lines
            separator = customtkinter.CTkFrame(text_frame, height=2, fg_color="#7289DA")
            separator.pack(pady=(10, 10), padx=20, fill="x")

        # Back Button
        back_button = customtkinter.CTkButton(self, text="Back", fg_color=master.theme_color, hover_color="#d4af37", text_color=master.text_color, command=master.show_Intro_page, corner_radius=10, border_width=2, border_color="#7289DA")
        back_button.pack(pady=(20, 30))  
class ContactFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#2C2F33", border_width=0, border_color="#7289DA")
        self.configure(fg_color=master.theme_color)
        
        # Title
        title = customtkinter.CTkLabel(self, text="Contact Us", text_color=master.text_color, font=("Segoe UI", 28, "bold"), fg_color=master.theme_color, height=60)
        title.pack(fill="x", pady=(10, 20))
        
        # Contact Icons 
        contact_icons_frame = customtkinter.CTkFrame(self, fg_color=master.theme_color, corner_radius=10)
        contact_icons_frame.pack(pady=(10, 20), padx=20, fill="x")
        
        # Email icon added email picture and readjusted message says
        icon_data = [
            ("📧", "Need help? Reach out to us through the following emails at any time!")
        ]
        
        for icon, label_text in icon_data:
            contact_button = customtkinter.CTkButton(contact_icons_frame, text=f"{icon} {label_text}", font=("Segoe UI", 17,"bold"), fg_color=master.theme_color, hover_color="#d4af37", text_color=master.text_color, corner_radius=10, border_width=3, border_color="#7289DA")
            contact_button.pack(pady=5, fill="x", padx=20)
        
        # Email addresses added border to make it look neat 
        email_frame = customtkinter.CTkFrame(self, fg_color=master.theme_color, corner_radius=10, border_width=2, border_color="#7289DA")
        email_frame.pack(padx=20, pady=(0, 20), fill="x")

        email_list = [
            "martenoromaya@oakland.edu",
            "dromaya@oakland.edu",
            "danieltrpevski@oakland.edu",
            "cgatie@oakland.edu"
        ]
        
        for email in email_list:
            email_label = customtkinter.CTkLabel(email_frame, text=email, text_color=master.text_color, font=("Segoe UI", 14), fg_color=master.theme_color, height=40)
            email_label.pack(fill="x", padx=20, pady=5)
        
        # Back Button
        back_button = customtkinter.CTkButton(self, text="Back", fg_color=master.theme_color, hover_color="#d4af37", text_color=master.text_color, command=master.show_Intro_page, corner_radius=10, border_width=2, border_color="#7289DA")
        back_button.pack(pady=(20, 30))  

# This update_callback=None was used by ai to make it so it can be used in the main.py file to update the theme color in the main.py file
def opening_settings(update_callback=None): 
    app = SettingsApp(update_callback)
    app.resizable(False, False)