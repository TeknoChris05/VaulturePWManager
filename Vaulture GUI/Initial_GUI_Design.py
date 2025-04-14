import signal
import subprocess
import hashlib
import customtkinter
from PIL import Image, ImageTk
import tkinter
import os
from pathlib import Path
import string
import mysql.connector
import sys
import pyotp
import qrcode

#NOTICE: Some Sections of Code are AI GENERATED. The sections will be labeled (AI GENERATED) in its comment

class Login_Page(customtkinter.CTk):

    # Function to convert password string into SHA256 HASH
    def password_hash(self, str_password):
        hash_object = hashlib.sha256()
        hash_object.update(str_password.encode('utf-8'))
        return hash_object.hexdigest()

    def __init__(self):
        super().__init__()

        self.title("Vaulture")
        self.configure(fg_color="#0d133e")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.minsize(800, 600)
        self.maxsize(1920, 1080)

        # Connect to MySQL database
        self.login_database = mysql.connector.connect(
            host="db-mysql-nyc3-37387-do-user-15222509-0.l.db.ondigitalocean.com",
            user="doadmin",
            passwd='AVNS_AK8FErb1DuSyVpZeMZR',
            port='25060',
            database="Vaulturedb"
        )
        self.mycursor = self.login_database.cursor()

        # Retrieve screen dimensions (AI GENERATED)
        screen_dimension_width = self.winfo_screenwidth()
        screen_dimension_height = self.winfo_screenheight()
        x_pos = ((screen_dimension_width - self.winfo_screenwidth()) // 2) - 10
        y_pos = ((screen_dimension_height - self.winfo_screenheight()) // 2) - 1
        self.geometry(f"{screen_dimension_width}x{screen_dimension_height}+{x_pos}+{y_pos}")
        self.pack_propagate(False)

        # Create main frames for login and account creation
        self.login_frame = customtkinter.CTkFrame(
            master=self,
            width=screen_dimension_width/2,
            height=screen_dimension_height/1.5,
            border_width=10,
            border_color="#000206",
            fg_color="#030c49"
        )
        self.login_frame.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        self.login_frame.pack_propagate(False)

        self.account_frame = customtkinter.CTkScrollableFrame(
            self,
            width=screen_dimension_width/2,
            height=screen_dimension_height/1.5,
            border_width=10,
            corner_radius=10,
            border_color="#000206",
            fg_color="#030c49"
        )
        self.account_frame.pack_propagate(False)

        # Account creation label
        create_account_label = customtkinter.CTkLabel(
            self.account_frame,
            text="Create an Account",
            text_color="yellow",
            font=("Arial", 26, "bold")
        )
        create_account_label.grid(row=0, column=0, sticky="n", pady=20)

        # Load image for logo
        script_dir = Path(__file__).parent
        project_root = script_dir.parent
        image_path = project_root / "images" / "Vaulture.png"
        self.vulture = customtkinter.CTkImage(
            Image.open(image_path),
            size=(200,200)
        )

        # Configure layout for login_frame and account_frame
        self.login_frame.columnconfigure(0, weight=1)
        self.login_frame.rowconfigure(0, weight=1)
        self.login_frame.rowconfigure((1,2,3), weight=2)
        self.login_frame.rowconfigure(4, weight=5)
        self.account_frame.columnconfigure(0, weight=1)
        self.account_frame.rowconfigure(0, weight=1)
        self.account_frame.rowconfigure(1, weight=3)
        self.account_frame.rowconfigure(2, weight=15)

        # Logo and Title on login frame
        vulture_label = customtkinter.CTkLabel(self.login_frame, text="", image=self.vulture)
        vulture_label.grid(row=0, column=0, pady=30, sticky="n")
        title_label = customtkinter.CTkLabel(
            self.login_frame, text="VAULTURE", text_color="yellow", font=("Arial", 35, "bold")
        )
        title_label.grid(row=0, column=0, pady=15, sticky="n")

        # Login Widgets
        username_label = customtkinter.CTkLabel(
            self.login_frame, text="Username", font=("Courier", 20, "bold"), text_color="yellow"
        )
        username_label.grid(row=0, column=0, sticky="s", pady=(10,0))
        self.username_entry = customtkinter.CTkEntry(
            self.login_frame, placeholder_text="Enter Username",
            width=200, height=30, border_width=1, corner_radius=10
        )
        self.username_entry.grid(row=1, column=0, sticky="n", pady=(0,10))

        password_label = customtkinter.CTkLabel(
            self.login_frame, text="Password", font=("Courier", 20, "bold"), text_color="yellow"
        )
        password_label.grid(row=1, column=0, sticky="s", pady=(10,0))
        self.password_entry = customtkinter.CTkEntry(
            self.login_frame, show="*", placeholder_text="Enter Password",
            width=200, height=30, border_width=1, corner_radius=10
        )
        self.password_entry.grid(row=2, column=0, sticky="n", pady=(0,10))

        # 2FA Code widget on login (used during login)
        code_label = customtkinter.CTkLabel(
            self.login_frame, text="2FA Code", font=("Courier", 20, "bold"), text_color="yellow"
        )
        code_label.grid(row=3, column=0, sticky="n", pady=(10,0))
        self.code_entry = customtkinter.CTkEntry(
            self.login_frame, placeholder_text="Enter 2FA Code",
            width=200, height=30, border_width=1, corner_radius=10
        )
        self.code_entry.grid(row=2, column=0, sticky="n", pady=(80,0))

        account_label2 = customtkinter.CTkLabel(
            self.login_frame,
            text="Don't have an account? Create one by clicking the 'Sign Up' button",
            font=("Courier", 12, "bold"),
            text_color="yellow"
        )
        account_label2.grid(row=2, column=0, sticky="s")

        login_button = customtkinter.CTkButton(
            self.login_frame, text="Login", fg_color="yellow", text_color="black", command=self.confirm_login
        )
        login_button.grid(row=3, column=0, sticky="n", padx=10, pady=5)
        sign_up_button = customtkinter.CTkButton(
            self.login_frame, text="Sign Up", fg_color="yellow", text_color="black", command=lambda: self.show_create_account_frame()
        )
        sign_up_button.grid(row=3, column=0)

        # Account Creation Widgets
        new_username_label = customtkinter.CTkLabel(
            self.account_frame, text="Username", font=("Courier", 18, "bold"), text_color="yellow"
        )
        new_username_label.grid(row=1, column=0, sticky="n")
        self.new_username_entry = customtkinter.CTkEntry(
            self.account_frame, placeholder_text="Enter Username",
            width=200, height=30, border_width=1, corner_radius=10
        )
        self.new_username_entry.grid(row=1, column=0, sticky="n", pady=30)
        email_label = customtkinter.CTkLabel(
            self.account_frame, text="Email", font=("Courier", 18, "bold"), text_color="yellow"
        )
        email_label.grid(row=1, column=0, sticky="n", pady=80)
        self.email_entry = customtkinter.CTkEntry(
            self.account_frame, placeholder_text="Enter Email",
            width=200, height=30, border_width=1, corner_radius=10
        )
        self.email_entry.grid(row=1, column=0, sticky="n", pady=110)
        new_password_label = customtkinter.CTkLabel(
            self.account_frame, text="Password", font=("Courier", 18, "bold"), text_color="yellow"
        )
        new_password_label.grid(row=1, column=0, sticky="n", pady=165)
        self.new_password_entry = customtkinter.CTkEntry(
            self.account_frame, show="*", placeholder_text="Enter Password",
            width=200, height=30, border_width=1, corner_radius=10
        )
        self.new_password_entry.grid(row=1, column=0, sticky="n", pady=195)
        confirm_password_label = customtkinter.CTkLabel(
            self.account_frame, text="Confirm Password", font=("Courier", 18, "bold"), text_color="yellow"
        )
        confirm_password_label.grid(row=1, column=0, sticky="n", pady=255)
        self.confirm_password_entry = customtkinter.CTkEntry(
            self.account_frame, show="*", placeholder_text="Enter Password Again",
            width=200, height=30, border_width=1, corner_radius=10
        )
        self.confirm_password_entry.grid(row=1, column=0, sticky="n", pady=285)

        create_account_button = customtkinter.CTkButton(
            self.account_frame, text="Create Account", fg_color="yellow", text_color="black", command=self.save_account_info
        )
        create_account_button.grid(row=1, column=0, sticky="n", pady=345)
        back_button = customtkinter.CTkButton(
            self.account_frame, text="Back", fg_color="yellow", text_color="black", command=lambda: self.show_login_frame()
        )
        back_button.grid(row=2, column=0, sticky="w", padx=20, pady=50)

        # Show/hide password switches (for account creation and login)
        self.show_password_var = customtkinter.StringVar(value="off")
        self.show_password_button = customtkinter.CTkSwitch(
            self.account_frame, variable=self.show_password_var, text="Show", onvalue="on", offvalue="off", command=self.show_password
        )
        self.show_password_button.grid(row=1, column=0, sticky="ne", pady=198, padx=550)
        self.show_password_var = customtkinter.StringVar(value="off")
        self.show_confirm_password_button = customtkinter.CTkSwitch(
            self.account_frame, variable=self.show_password_var, text="Show", onvalue="on", offvalue="off", command=self.show_confirm_password
        )
        self.show_confirm_password_button.grid(row=1, column=0, sticky="ne", pady=285, padx=550)
        self.show_password_var = customtkinter.StringVar(value="off")
        self.show_password_button_login = customtkinter.CTkSwitch(
            self.login_frame, variable=self.show_password_var, text="Show", onvalue="on", offvalue="off", command=self.show_password_login
        )
        self.show_password_button_login.grid(row=2, column=0, sticky="ne", padx=535)

        self.rules_label = customtkinter.CTkLabel(
            self.account_frame,
            text="• Email must be valid (contain '@' and '.com')\n• Password must contain at least one special character and one number",
            text_color="yellow",
            font=("Courier", 14, "bold")
        )
        self.rules_label.pack(padx=20, pady=20, anchor="e")

        # Initialize error labels for feedback
        self.username_error_label = None
        self.email_error_label = None
        self.password_error_label = None
        self.confirm_password_error_label = None
        self.successful_account = None
        self.login_username_error = None
        self.login_password_error = None

    # Show/hide password methods
    def show_password(self):
        if self.new_password_entry.cget("show") == "*":
            self.new_password_entry.configure(show="")
            self.show_password_button.configure(text="Hide")
        else:
            self.new_password_entry.configure(show="*")
            self.show_password_button.configure(text="Show")

    def show_confirm_password(self):
        if self.confirm_password_entry.cget("show") == "*":
            self.confirm_password_entry.configure(show="")
            self.show_confirm_password_button.configure(text="Hide")
        else:
            self.confirm_password_entry.configure(show="*")
            self.show_confirm_password_button.configure(text="Show")

    def show_password_login(self):
        if self.password_entry.cget("show") == "*":
            self.password_entry.configure(show="")
            self.show_password_button_login.configure(text="Hide")
        else:
            self.password_entry.configure(show="*")
            self.show_password_button_login.configure(text="Show")

    # Switch between login frame and account creation frame
    def show_create_account_frame(self):
        self.login_frame.pack_forget()
        self.account_frame.pack(fill="both", expand=True)

    def show_login_frame(self):
        self.account_frame.pack_forget()
        if self.login_username_error is not None:
            self.login_username_error.destroy()
            self.login_username_error = None
        if self.login_password_error is not None:
            self.login_password_error.destroy()
            self.login_password_error = None
        if self.username_error_label is not None:
            self.username_error_label.destroy()
            self.username_error_label = None
        if self.email_error_label is not None:
            self.email_error_label.destroy()
            self.email_error_label = None
        if self.confirm_password_error_label is not None:
            self.confirm_password_error_label.destroy()
            self.confirm_password_error_label = None
        if self.password_error_label is not None:
            self.password_error_label.destroy()
            self.password_error_label = None
        if self.successful_account is not None:
            self.successful_account.destroy()
            self.successful_account = None

        self.login_frame.pack(fill="both", expand=True)
        self.new_username_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.password_entry.delete(0, "end")

    # Save account info (sign-up) and generate QR code popup for 2FA registration
    def save_account_info(self):
        username = self.new_username_entry.get()
        email = self.email_entry.get()
        password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Check password criteria
        contains_number = any(char.isdigit() for char in password)
        contains_special = any(char in string.punctuation for char in password)

        # Destroy previous error labels if they exist
        if self.username_error_label is not None:
            self.username_error_label.destroy()
            self.username_error_label = None
        if self.email_error_label is not None:
            self.email_error_label.destroy()
            self.email_error_label = None
        if self.confirm_password_error_label is not None:
            self.confirm_password_error_label.destroy()
            self.confirm_password_error_label = None
        if self.password_error_label is not None:
            self.password_error_label.destroy()
            self.password_error_label = None

        error = False

        if username == "":
            self.username_error_label = customtkinter.CTkLabel(
                self.account_frame, text="Please Enter A Username",
                font=("Courier", 18, "bold"), text_color="red"
            )
            self.username_error_label.pack(padx=20, pady=15, anchor="w")
            error = True

        if email == "" or ("@" not in email or ".com" not in email):
            self.email_error_label = customtkinter.CTkLabel(
                self.account_frame, text="Please Enter A Valid Email",
                font=("Courier", 18, "bold"), text_color="red"
            )
            self.email_error_label.pack(padx=20, pady=15, anchor="w")
            error = True

        if password == "" or password != confirm_password or (not contains_number or not contains_special):
            self.password_error_label = customtkinter.CTkLabel(
                self.account_frame, text="Please Enter a Valid Password or\ncheck if password entries match",
                font=("Courier", 18, "bold"), text_color="red"
            )
            self.password_error_label.pack(padx=20, pady=15, anchor="w")
            error = True

        if not error:
            # Generate a 2FA secret and store it with the account
            secret = pyotp.random_base32()
            self.mycursor.execute(
                "INSERT INTO Account (Username, Email, Password, TwoFA_Secret) VALUES (%s, %s, %s, %s)",
                (username, email, self.password_hash(password), secret)
            )
            self.login_database.commit()
            self.account_frame.pack_forget()
            self.login_frame.pack(fill="both", expand=True)
            self.new_username_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.new_password_entry.delete(0, "end")
            self.confirm_password_entry.delete(0, "end")
            self.successful_account = customtkinter.CTkLabel(
                self.login_frame, text="Successfully Created Account!",
                font=("Courier", 18, "bold"), text_color="green"
            )
            self.successful_account.pack(padx=20, pady=15, anchor="w")

            # Show the QR code popup for 2FA registration
            self.show_qr_popup(username, secret)

    # Display a popup window with the QR code for Google Authenticator registration
    def show_qr_popup(self, username, secret):
        issuer = "Vaulture"
        totp = pyotp.TOTP(secret)
        uri = totp.provisioning_uri(name=username, issuer_name=issuer)
        qr = qrcode.make(uri)

        popup = customtkinter.CTkToplevel(self)
        popup.title("Scan QR Code for Google Authenticator")
        popup.attributes("-topmost", True)
        popup.lift()
        popup.focus_force()

        qr_photo = ImageTk.PhotoImage(qr)
        label = customtkinter.CTkLabel(popup, image=qr_photo, text="")
        label.image = qr_photo  # Keep a reference to avoid garbage collection
        label.pack(padx=20, pady=20)
        info_label = customtkinter.CTkLabel(popup, text="Scan this code in Google Authenticator")
        info_label.pack(pady=(0,10))

    # Verify login credentials and 2FA code during login
    def confirm_login(self):
        login_username = self.username_entry.get()
        login_password = self.password_entry.get()

        if self.login_username_error is not None:
            self.login_username_error.destroy()
            self.login_username_error = None
        if self.login_password_error is not None:
            self.login_password_error.destroy()
            self.login_password_error = None

        try:
            self.login_database = mysql.connector.connect(
                host="db-mysql-nyc3-37387-do-user-15222509-0.l.db.ondigitalocean.com",
                user="doadmin",
                passwd='AVNS_AK8FErb1DuSyVpZeMZR',
                port='25060',
                database="Vaulturedb"
            )
            self.mycursor = self.login_database.cursor(buffered=True)
            query = "SELECT AccountID, Password, TwoFA_Secret FROM Account WHERE Username = %s"
            self.mycursor.execute(query, (login_username,))
            result = self.mycursor.fetchone()

            if result:
                account_id, stored_password, twofa_secret = result
                if stored_password == self.password_hash(login_password):
                    # Verify the 2FA code entered by the user
                    code_input = self.code_entry.get().strip()
                    totp = pyotp.TOTP(twofa_secret)
                    if totp.verify(code_input, valid_window=1):
                        print("Login successful! Welcome,", login_username)
                        self.destroy()
                        try:
                            for proc in os.popen('tasklist').readlines():
                                if "Dan.py" in proc:
                                    pid = int(proc.split()[1])
                                    os.kill(pid, signal.SIGTERM)
                            # Construct the absolute path to Dan.py based on the current file's directory
                            dan_path = str(Path(__file__).parent / "Dan.py")
                            subprocess.run([sys.executable, dan_path, str(account_id)], check=True)
                            return True
                        except subprocess.CalledProcessError as e:
                            print(f"Error running Dan.py: {e}")
                            return False
                        except Exception as e:
                            print(f"Error managing subprocess: {e}")
                            return False
                    else:
                        self.login_password_error = customtkinter.CTkLabel(
                            self.login_frame, text="Invalid 2FA Code", font=("Courier", 20, "bold"), text_color="red"
                        )
                        self.login_password_error.pack(padx=20, pady=15, anchor="w")
                        return False
                else:
                    self.login_password_error = customtkinter.CTkLabel(
                        self.login_frame, text="Incorrect Password", font=("Courier", 20, "bold"), text_color="red"
                    )
                    self.login_password_error.pack(padx=20, pady=15, anchor="w")
                    return False
            else:
                self.login_username_error = customtkinter.CTkLabel(
                    self.login_frame, text="Username not found", font=("Courier", 20, "bold"), text_color="red"
                )
                self.login_username_error.pack(padx=20, pady=15, anchor="w")
                return False

        except mysql.connector.Error as e:
            print("Error connecting to database:", e)
        finally:
            if self.login_database.is_connected():
                self.mycursor.close()
                self.login_database.close()

if __name__ == "__main__":
    window_login = Login_Page()
    window_login.resizable(False, False)
    try:
        window_login.mainloop()
    except KeyboardInterrupt:
        print("Window Closed")