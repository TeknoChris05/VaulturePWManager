import customtkinter
from tkinter import colorchooser
from PIL import Image, ImageTk
import pyotp
import qrcode


class SettingsApp(customtkinter.CTk):
    """Main application window for the settings interface with sidebar navigation."""
    def __init__(self):
        super().__init__()
        self.state("zoomed")  # Fullscreen mode
        self.configure(fg_color="#2C2F33")  # Dark theme background

        # Default theme settings
        self.theme_color = "#2C2F33"  # Match background color
        self.text_color = "white"

        self.current_frame = None  # Holds the current displayed frame
        
        self._create_sidebar()
        self.show_settings_page()  # Initialize with the settings page

    def _create_sidebar(self):
        """Creates a stylish sidebar for navigation."""
        self.sidebar = customtkinter.CTkFrame(self, fg_color="#23272A", width=200, corner_radius=10)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)

        title = customtkinter.CTkLabel(self.sidebar, text="Vaulture", font=("Segoe UI", 24, "bold"),
                                       text_color="#FFFFFF", fg_color="#23272A")
        title.pack(pady=20)

        buttons = [
            ("⚙ Settings", self.show_settings_page),
            ("🔒 Security", self.show_security_page),
            ("🎨 Themes", self.show_themes_page),
        ]

        for text, command in buttons:
            btn = customtkinter.CTkButton(self.sidebar, text=text, font=("Segoe UI", 18),
                                          fg_color="#2C2F33", hover_color="#7289DA",
                                          text_color="#FFFFFF", command=command, corner_radius=10, border_width=2, border_color="#7289DA")
            btn.pack(fill="x", padx=10, pady=10)

    def show_settings_page(self):
        """Displays the main settings page."""
        self._switch_frame(SettingsFrame)

    def show_security_page(self):
        """Displays the security settings page."""
        self._switch_frame(SecurityFrame)

    def show_themes_page(self):
        """Displays the themes page."""
        self._switch_frame(ThemesFrame)

    def _switch_frame(self, frame_class):
        """Helper method to switch frames dynamically."""
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = frame_class(self)
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def update_theme(self, new_color):
        """Updates the theme color and adjusts text color for readability."""
        self.theme_color = new_color
        self.text_color = self.get_readable_text_color(new_color)
        self.sidebar.configure(fg_color=new_color)
        self.show_settings_page()

    @staticmethod
    def get_readable_text_color(bg_color):
        """Determines whether text should be black or white based on background brightness."""
        bg_color = bg_color.lstrip("#")
        r, g, b = int(bg_color[0:2], 16), int(bg_color[2:4], 16), int(bg_color[4:6], 16)
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        return "black" if brightness > 128 else "white"


class SettingsFrame(customtkinter.CTkFrame):
    """Main settings page with enhanced UI."""
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#2C2F33", border_width=0, border_color="#7289DA")

        title = customtkinter.CTkLabel(self, text="Settings", text_color=master.text_color,
                                       font=("Segoe UI", 28, "bold"), fg_color=master.theme_color, height=60)
        title.pack(fill="x")

        options = [
            "Auto-lock timeout",
            "Password strength meter",
            "Data export/import",
            "Biometric authentication"
        ]

        for option in options:
            btn = customtkinter.CTkButton(self, text=option, text_color=master.text_color,
                                          font=("Segoe UI", 18), fg_color=master.theme_color,
                                          hover_color="#d4af37", corner_radius=10, border_width=2, border_color="#7289DA")
            btn.pack(fill="x", padx=20, pady=5)


class SecurityFrame(customtkinter.CTkFrame):
    """Security settings page with improved layout."""
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#2C2F33", border_width=0, border_color="#7289DA")

        title = customtkinter.CTkLabel(self, text="Security Settings", text_color=master.text_color,
                                       font=("Segoe UI", 28, "bold"), fg_color=master.theme_color, height=60)
        title.pack(fill="x")

        label = customtkinter.CTkLabel(self, text="Enable Two-Factor Authentication (2FA)",
                                       font=("Segoe UI", 18), text_color="white")
        label.pack(pady=20)

        self.two_fa_frame = customtkinter.CTkFrame(self, fg_color="#23272A", border_width=2, border_color="#7289DA", corner_radius=10)
        self.two_fa_frame.pack(pady=10, padx=20, fill="x")
        
        self.two_fa_switch = customtkinter.CTkSwitch(self.two_fa_frame, text="Enable 2FA", fg_color=master.theme_color,
                                                     text_color=master.text_color)
        self.two_fa_switch.pack(pady=10, padx=10)

        self.recovery_code_button = customtkinter.CTkButton(self, text="Generate Recovery Codes", fg_color=master.theme_color,
                                                             hover_color="#d4af37", text_color=master.text_color,
                                                             corner_radius=10, border_width=2, border_color="#7289DA")
        self.recovery_code_button.pack(pady=10)

        back_button = customtkinter.CTkButton(self, text="Back", fg_color=master.theme_color, hover_color="#d4af37",
                                              text_color=master.text_color, command=master.show_settings_page,
                                              corner_radius=10, border_width=2, border_color="#7289DA")
        back_button.pack(pady=20)


class ThemesFrame(customtkinter.CTkFrame):
    """Themes settings page with color picker."""
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#2C2F33", border_width=0, border_color="#7289DA")

        title = customtkinter.CTkLabel(self, text="Themes", text_color=master.text_color,
                                       font=("Segoe UI", 28, "bold"), fg_color=master.theme_color, height=60)
        title.pack(fill="x")

        self.color_button = customtkinter.CTkButton(self, text="Pick Theme Color", fg_color=master.theme_color,
                                                    hover_color="#d4af37", text_color=master.text_color,
                                                    command=self.pick_color)
        self.color_button.pack(pady=10)

    def pick_color(self):
        color_code = colorchooser.askcolor(title="Choose Theme Color")[1]
        if color_code:
            self.master.update_theme(color_code)

 # Generate a secret key (store securely)
    secret_key = pyotp.random_base32()

    # Create a TOTP object
    totp = pyotp.TOTP(secret_key)

    # Generate the provisioning URI for the QR code
    provisioning_uri = totp.provisioning_uri(name='user@example.com', issuer_name='YourAppName')

    # Generate QR code
    img = qrcode.make(provisioning_uri)
    img.save('qrcode.png')

    # To verify OTP
    otp = input("Enter the OTP from the Google Authenticator app: ")
    if totp.verify(otp):
        print("OTP is valid")
    else:
        print("OTP is invalid")

if __name__ == "__main__":
    app = SettingsApp()
    app.mainloop()

