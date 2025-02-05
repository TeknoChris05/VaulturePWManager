import customtkinter as ctk
import json
import random
import string
import os

# File in which passwords are stored
DATA_FILE = "passwords.json"


class PasswordManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Password Manager")
        self.geometry("500x400")

        # ========== Appearance Settings ==========
        # Uncomment and adjust if you want dark/light mode or system-based:
        # ctk.set_appearance_mode("dark")   # "dark", "light", or "system"
        # ctk.set_default_color_theme("blue")   # Or "green", "dark-blue"

        # ========== Widgets ==========
        # Labels and entries for website/app, username, and password
        self.label_website = ctk.CTkLabel(master=self, text="Website / App:")
        self.label_website.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_website = ctk.CTkEntry(master=self, width=200)
        self.entry_website.grid(row=0, column=1, padx=10, pady=10)

        self.label_username = ctk.CTkLabel(master=self, text="Username / Email:")
        self.label_username.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_username = ctk.CTkEntry(master=self, width=200)
        self.entry_username.grid(row=1, column=1, padx=10, pady=10)

        self.label_password = ctk.CTkLabel(master=self, text="Password:")
        self.label_password.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_password = ctk.CTkEntry(master=self, width=200, show="*")
        self.entry_password.grid(row=2, column=1, padx=10, pady=10)

        # Buttons for generate password, save, and show all
        self.button_generate = ctk.CTkButton(
            master=self, 
            text="Generate Password", 
            command=self.generate_password
        )
        self.button_generate.grid(row=3, column=0, padx=10, pady=10)

        self.button_save = ctk.CTkButton(
            master=self, 
            text="Save Password", 
            command=self.save_password
        )
        self.button_save.grid(row=3, column=1, padx=10, pady=10)

        self.button_show = ctk.CTkButton(
            master=self, 
            text="Show All Passwords", 
            command=self.show_all_passwords
        )
        self.button_show.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # A read-only textbox or scrolled text to display results
        self.text_display = ctk.CTkTextbox(master=self, width=450, height=150, state="disabled")
        self.text_display.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Ensure the JSON file exists
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w") as f:
                json.dump([], f)

    def generate_password(self, length=12):
        """Generate a random password of a given length."""
        chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(chars) for _ in range(length))
        self.entry_password.delete(0, ctk.END)
        self.entry_password.insert(0, password)

    def save_password(self):
        """Save the website, username, and password into a JSON file."""
        website = self.entry_website.get().strip()
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()

        if not website or not username or not password:
            self.update_display("Please fill in all fields before saving.")
            return

        new_entry = {
            "website": website,
            "username": username,
            "password": password
        }

        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = []

        data.append(new_entry)

        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

        self.update_display(f"Password for '{website}' saved successfully!")
        
        # Clear entry fields after saving
        self.entry_website.delete(0, ctk.END)
        self.entry_username.delete(0, ctk.END)
        self.entry_password.delete(0, ctk.END)

    def show_all_passwords(self):
        """Display all stored passwords in the text widget."""
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = []

        if not data:
            self.update_display("No passwords stored yet.")
            return

        display_text = "Stored Passwords:\n"
        display_text += "-" * 50 + "\n"
        for idx, entry in enumerate(data, start=1):
            website = entry.get("website", "")
            username = entry.get("username", "")
            password = entry.get("password", "")
            display_text += f"{idx}. Website/App: {website}\n"
            display_text += f"   Username/Email: {username}\n"
            display_text += f"   Password: {password}\n"
            display_text += "-" * 50 + "\n"

        self.update_display(display_text)

    def update_display(self, text):
        """Helper to update the read-only text widget."""
        self.text_display.configure(state="normal")
        self.text_display.delete("1.0", ctk.END)
        self.text_display.insert(ctk.END, text)
        self.text_display.configure(state="disabled")


if __name__ == "__main__":
    app = PasswordManagerApp()
    app.mainloop()
