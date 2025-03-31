import customtkinter
import colorsys
from tkinter import colorchooser
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class SettingsApp(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
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
        Exit_button = customtkinter.CTkButton(self, text="Exit", command=self.destroy)
        Exit_button.pack(side="bottom", pady=100)
        self.lift()
        self.focus_force()
        self.grab_set()
            
    def _create_sidebar(self):
        self.sidebar = customtkinter.CTkFrame(self, fg_color="#23272A", width=200, corner_radius=10)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)        
        title = customtkinter.CTkLabel(self.sidebar, text="Vaulture", font=("Segoe UI", 24, "bold"), text_color="#FFFFFF", fg_color="#23272A")
        title.pack(pady=20)
        
        buttons = [
            ("⚙ Settings", self.show_settings_page),
            ("👤 Account", self.show_account_page),
            ("🔒 Security", self.show_security_page),
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
    
    #Color Picker Theme Change        
    def update_theme(self, new_color):
        self.theme_color = new_color  
        self.configure(fg_color=new_color)  
        self.sidebar.configure(fg_color=new_color)
        #Sidebar diff shade
        darker_color = self._darken_color(new_color, 0.8)
        self.sidebar.configure(fg_color=darker_color)
        #Update Sidebar
        for widget in self.sidebar.winfo_children():
            if isinstance(widget, customtkinter.CTkButton):
                widget.configure(fg_color=new_color)
        # Update Vaulture title label
        title_label = self.sidebar.winfo_children()[0] 
        if isinstance(title_label, customtkinter.CTkLabel):
            title_label.configure(fg_color=new_color)                
        #Update Current Frame
        if self.current_frame:
            self.current_frame.configure(fg_color=new_color)
            for widget in self.current_frame.winfo_children():
                if isinstance(widget, (customtkinter.CTkButton, customtkinter.CTkLabel, customtkinter.CTkSwitch, customtkinter.CTkFrame)):
                    widget.configure(fg_color=new_color, text_color="black" if new_color == "#FFFFFF" else "white")
        if isinstance(self.current_frame, SecurityFrame):
                    self.current_frame.twofa_frame.configure(fg_color=new_color)                    
        
        self.refresh_current_frame()  
    
    def refresh_current_frame(self):
    #Recreate Frame and Apply changes
     if self.current_frame:
        frame_class = type(self.current_frame)  
        self.current_frame.destroy()
        self.current_frame = frame_class(self)
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)
            
    def show_Intro_page(self):
        self._switch_frame(IntroFrame)

    def show_settings_page(self):
        self._switch_frame(SettingsFrame)
        
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
            
        self.current_frame = frame_class(self)
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)

        #Theme Color Update
        self.current_frame.configure(fg_color=self.theme_color)
        for widget in self.current_frame.winfo_children():
            if isinstance(widget, (customtkinter.CTkButton, customtkinter.CTkLabel, customtkinter.CTkFrame)):
                widget.configure(fg_color=self.theme_color, text_color="black" if self.theme_color == "#FFFFFF" else "white")

class IntroFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#2C2F33", border_width=0, border_color="#7289DA")
        self.configure(fg_color=master.theme_color)

        title = customtkinter.CTkLabel(self, text="Settings", text_color=master.text_color,
                                       font=("Segoe UI", 28, "bold"), fg_color=master.theme_color, height=60)
        title.pack(fill="x")

        contact_text = """Welcome to the settings page! """

        label = customtkinter.CTkLabel(self, text=contact_text, text_color="white",  justify="left", font=("Segoe UI", 16), wraplength=600)
        label.pack(pady=20, padx=20)

            
class SettingsFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#2C2F33", border_width=0, border_color="#7289DA")
        self.configure(fg_color=master.theme_color)

        title = customtkinter.CTkLabel(self, text="Settings", text_color=master.text_color,
                                       font=("Segoe UI", 28, "bold"), fg_color=master.theme_color, height=60)
        title.pack(fill="x")

        btn_options = [
            "Auto-lock",
            "Password Strength",
            "Autofill",
            "Data Import/Export",
            "Erase Data",
        ]

        for option in btn_options:
            btn = customtkinter.CTkButton(self, text=option, text_color=master.text_color,
                                          font=("Segoe UI", 18), fg_color=master.theme_color,
                                          hover_color="#d4af37", corner_radius=10, border_width=2, border_color="#7289DA")
            btn.pack(fill="x", padx=20, pady=0)    

        back_button = customtkinter.CTkButton(self, text="Back", fg_color=master.theme_color, hover_color="#d4af37", text_color=master.text_color, command=master.show_Intro_page, corner_radius=10, border_width=2, border_color="#7289DA")
        back_button.pack(pady=20)
        
import customtkinter
from tkinter import filedialog

class AccountFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#2C2F33", corner_radius=10)

        title = customtkinter.CTkLabel(self, text="Account Information", text_color="white", font=("Segoe UI", 28, "bold"), fg_color="#2C2F33")
        title.pack(pady=10)

        self.text_widget = customtkinter.CTkTextbox(self, height=200, width=400, font=("Arial", 16))
        self.text_widget.pack(pady=10, padx=10)

        self.load_Account_Info()

    def load_Account_Info(self):
        try:
            with open("Account_info", "r") as file:
                content = file.read()
                self.text_widget.delete("1.0", "end")  
                self.text_widget.insert("end", content)  
        except FileNotFoundError:
            self.text_widget.insert("end", "No account info file found.")

 
class SecurityFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=master.theme_color, border_width=0, border_color="#7289DA")

        title = customtkinter.CTkLabel(self, text="Security Settings", text_color=master.text_color, font=("Segoe UI", 28, "bold"), fg_color=master.theme_color, height=60)
        title.pack(fill="x")
        label = customtkinter.CTkLabel(self, text="Enable Two-Factor Authentication (2FA)", font=("Segoe UI", 18), text_color="white")
        label.pack(pady=20)
        
        self.twofa_frame = customtkinter.CTkFrame(self, fg_color=master.theme_color, border_width=2, border_color="#7289DA", corner_radius=10)
        self.twofa_frame.pack(pady=10, padx=20, fill="x")
        
        self.twofa_switch = customtkinter.CTkSwitch(self.twofa_frame, text="Enable 2FA", fg_color=master.theme_color, text_color=master.text_color)
        self.twofa_switch.pack(pady=10, padx=10)

        self.recovery_code_button = customtkinter.CTkButton(self, text="Generate Recovery Codes", fg_color=master.theme_color, hover_color="#d4af37", text_color=master.text_color,corner_radius=10, border_width=2, border_color="#7289DA")
        self.recovery_code_button.pack(pady=10)

        back_button = customtkinter.CTkButton(self, text="Back", fg_color=master.theme_color, hover_color="#d4af37", text_color=master.text_color, command=master.show_Intro_page, corner_radius=10, border_width=2, border_color="#7289DA")
        back_button.pack(pady=20)
        

class ThemesFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#2C2F33", border_width=0, border_color="#7289DA")
        self.configure(fg_color=master.theme_color)

        title = customtkinter.CTkLabel(self, text="Themes", text_color=master.text_color, font=("Segoe UI", 28, "bold"), fg_color=master.theme_color, height=60)
        title.pack(fill="x")

        self.color_button = customtkinter.CTkButton(self, text="Pick Theme Color", border_width=2, border_color="#7289DA", fg_color=master.theme_color, hover_color="#d4af37", text_color=master.text_color, command=self.pick_color)
        self.color_button.pack(pady=10)

        back_button = customtkinter.CTkButton(self, text="Back", fg_color=master.theme_color, hover_color="#d4af37", text_color=master.text_color, command=master.show_Intro_page, corner_radius=10, border_width=2, border_color="#7289DA")
        back_button.pack(pady=20)  

    def pick_color(self):
        color_code = colorchooser.askcolor(title="Choose Theme Color")[1]
        if color_code:
            self.master.update_theme(color_code)

class HelpFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#2C2F33", border_width=0, border_color="#7289DA")
        self.configure(fg_color=master.theme_color)

        title = customtkinter.CTkLabel(self, text="Help", text_color=master.text_color, font=("Segoe UI", 28, "bold"), fg_color=master.theme_color, height=60)
        title.pack(fill="x")

        contact_text = """Here is some helpful tips!

-How do i make passwords? Just click the waffle and all the options are there! 

-How do i change the theme? Go to the themes page and click the button to change the theme color!

-How do i enable 2FA? Go to the security page and click the switch to enable 2FA!

-How do i contact you? Go to the contact page and all the emails are there

-How can i see my passwords? Go hit the bird icon to dislpay!

-Can i make a pfp and profile name? Yes! Go to the Profile Page on the bottom bar and you can change it there!
        """

        back_button = customtkinter.CTkButton(self, text="Back", fg_color=master.theme_color, hover_color="#d4af37", text_color=master.text_color, command=master.show_Intro_page, corner_radius=10, border_width=2, border_color="#7289DA")
        back_button.pack(pady=20) 

        label = customtkinter.CTkLabel(self, text=contact_text, text_color="white",  justify="left", font=("Segoe UI", 16), wraplength=600)
        label.pack(pady=20, padx=20)

class ContactFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#2C2F33", border_width=0, border_color="#7289DA")
        self.configure(fg_color=master.theme_color)
        
        title = customtkinter.CTkLabel(self, text="Contact Us", text_color=master.text_color, font=("Segoe UI", 28, "bold"), fg_color=master.theme_color, height=60)
        title.pack(fill="x")

        contact_text = """Here is how you contact us!

        Emails: 
        - Martenoromaya@oakland.edu
        - dromaya@oakland.edu
        - danieltrpevski@oakland.edu
        - cgatie@oakland.edu
        """

        label = customtkinter.CTkLabel(self, text=contact_text, text_color="white",  justify="left", font=("Segoe UI", 16), wraplength=600)
        label.pack(pady=20, padx=20)

        back_button = customtkinter.CTkButton(self, text="Back", fg_color=master.theme_color, hover_color="#d4af37", text_color=master.text_color, command=master.show_Intro_page, corner_radius=10, border_width=2, border_color="#7289DA")
        back_button.pack(pady=20)



def opening_settings():
    app = SettingsApp()
    app.resizable(False, False)