import tkinter as tk
import customtkinter as ctk
import csv
import os
import time
import hashlib
from user_login import sign_in, sign_up
from helper_funcs import is_num, type_print
from income_expense import adding, remove
from get_csv_info import find_stuff_from_date

# Set appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self, x):
        super().__init__()
        self.title("Personal Finance Manager")
        self.geometry("900x700")
        self.current_widgets = []
        self.x = x  # login or signup flow indicator

        # User data
        self.current_csv = ""
        self.username = ""
        self.saving_amount = None
        self.deposit_often = None
        self.amount_per_period = None
        self.period_label = ""

        self.show_main_page()

    def clear_window(self):
        for widget in self.current_widgets:
            widget.destroy()
        self.current_widgets.clear()

    # --- Main Page ---
    def show_main_page(self):
        self.clear_window()
        self.title("Main Page")
        btn_signin = ctk.CTkButton(self, text="Sign in", command=self.show_sign_in_page)
        btn_signin.pack(pady=20)
        self.current_widgets.append(btn_signin)

        btn_signup = ctk.CTkButton(self, text="Create account", command=self.show_sign_up_page)
        btn_signup.pack(pady=20)
        self.current_widgets.append(btn_signup)

        btn_exit = ctk.CTkButton(self, text="Exit", command=self.destroy)
        btn_exit.pack(pady=20)
        self.current_widgets.append(btn_exit)

    # --- Sign In ---
    def show_sign_in_page(self):
        self.clear_window()
        self.title("Sign In")
        lbl = ctk.CTkLabel(self, text="Enter username and password")
        lbl.pack(pady=10)
        self.current_widgets.append(lbl)

        self.entry_username = ctk.CTkEntry(self, placeholder_text="Username")
        self.entry_username.pack(pady=5)
        self.current_widgets.append(self.entry_username)

        self.entry_password = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.entry_password.pack(pady=5)
        self.current_widgets.append(self.entry_password)

        btn_login = ctk.CTkButton(self, text="Log In", command=self.handle_sign_in)
        btn_login.pack(pady=10)
        self.current_widgets.append(btn_login)

        self.message_label = ctk.CTkLabel(self, text="")
        self.message_label.pack(pady=10)
        self.current_widgets.append(self.message_label)

    def handle_sign_in(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        csv_path, success = sign_in(username, password)
        if success:
            self.current_csv = csv_path
            self.username = username
            self.show_user_dashboard()
        else:
            self.message_label.configure(text="Incorrect login. Try again.")

    # --- Sign Up ---
    def show_sign_up_page(self):
        self.clear_window()
        self.title("Sign Up")
        lbl = ctk.CTkLabel(self, text="Create a new account")
        lbl.pack(pady=10)
        self.current_widgets.append(lbl)

        self.entry_new_username = ctk.CTkEntry(self, placeholder_text="New Username")
        self.entry_new_username.pack(pady=5)
        self.current_widgets.append(self.entry_new_username)

        self.entry_new_password = ctk.CTkEntry(self, placeholder_text="New Password", show="*")
        self.entry_new_password.pack(pady=5)
        self.current_widgets.append(self.entry_new_password)

        btn_signup = ctk.CTkButton(self, text="Sign Up", command=self.handle_sign_up)
        btn_signup.pack(pady=10)
        self.current_widgets.append(btn_signup)

        self.signup_message = ctk.CTkLabel(self, text="")
        self.signup_message.pack(pady=10)
        self.current_widgets.append(self.signup_message)

    def handle_sign_up(self):
        username = self.entry_new_username.get()
        password = self.entry_new_password.get()
        csv_path, success = sign_up(username, password)
        if success:
            self.current_csv = csv_path
            self.username = username
            self.show_user_dashboard()
        else:
            self.signup_message.configure(text="Sign-up failed. Try different credentials.")

    # --- User Dashboard ---
    def show_user_dashboard(self):
        self.clear_window()
        self.title(f"Welcome {self.username}")

        btn_create_saving = ctk.CTkButton(self, text="Create Saving Plan", command=self.create_saving_plan)
        btn_create_saving.pack(pady=10)
        self.current_widgets.append(btn_create_saving)

        btn_add_income = ctk.CTkButton(self, text="Add Income", command=self.add_income)
        btn_add_income.pack(pady=10)
        self.current_widgets.append(btn_add_income)

        btn_add_expense = ctk.CTkButton(self, text="Add Expense", command=self.add_expense)
        btn_add_expense.pack(pady=10)
        self.current_widgets.append(btn_add_expense)

        btn_view_data = ctk.CTkButton(self, text="View Data", command=self.view_data)
        btn_view_data.pack(pady=10)
        self.current_widgets.append(btn_view_data)

        btn_signout = ctk.CTkButton(self, text="Sign Out", command=self.show_main_page)
        btn_signout.pack(pady=10)
        self.current_widgets.append(btn_signout)

    # --- Create Saving Plan ---
    def create_saving_plan(self):
        self.clear_window()
        lbl = ctk.CTkLabel(self, text="Enter total savings goal")
        lbl.pack(pady=5)
        self.saving_entry = ctk.CTkEntry(self)
        self.saving_entry.pack(pady=5)

        # Frequency options
        self.freq_var = ctk.StringVar(value="monthly")
        ctk.CTkRadioButton(self, text="Daily", variable=self.freq_var, value="daily").pack()
        ctk.CTkRadioButton(self, text="Weekly", variable=self.freq_var, value="weekly").pack()
        ctk.CTkRadioButton(self, text="Monthly", variable=self.freq_var, value="monthly").pack()

        btn_save = ctk.CTkButton(self, text="Save Plan", command=self.save_saving)
        btn_save.pack(pady=10)

    def save_saving(self):
        amount_str = self.saving_entry.get()
        try:
            amount = float(amount_str)
            self.saving_amount = amount
        except:
            self.message_box("Invalid amount entered")
            return

        self.deposit_often = self.freq_var.get()

        # Set amount per period
        if self.deposit_often == "daily":
            self.amount_per_period = self.saving_amount / 30
            self.period_label = "per day"
        elif self.deposit_often == "weekly":
            self.amount_per_period = self.saving_amount / 4
            self.period_label = "per week"
        elif self.deposit_often == "monthly":
            self.amount_per_period = self.saving_amount / 12
            self.period_label = "per month"
        else:
            self.amount_per_period = None

        self.view_saving()

    def view_saving(self):
        self.clear_window()
        info = f"Your saving plan:\nTotal: ${self.saving_amount}\nFrequency: {self.deposit_often}\nAmount {self.period_label}: ${self.amount_per_period:.2f}"
        lbl = ctk.CTkLabel(self, text=info)
        lbl.pack(pady=10)

        btn_back = ctk.CTkButton(self, text="Back", command=self.show_user_dashboard)
        btn_back.pack(pady=10)
        self.current_widgets.append(lbl)
        self.current_widgets.append(btn_back)

    def message_box(self, message):
        msg = ctk.CTkLabel(self, text=message)
        msg.pack()
        self.current_widgets.append(msg)
        self.after(3000, lambda: self.current_widgets.remove(msg) or msg.destroy())

    # --- Income and Expense ---
    def add_income(self):
        self.clear_window()
        lbl = ctk.CTkLabel(self, text="Add Income")
        lbl.pack(pady=5)
        self.income_entry = ctk.CTkEntry(self)
        self.income_entry.pack(pady=5)

        btn_add = ctk.CTkButton(self, text="Add Income", command=self.save_income)
        btn_add.pack(pady=10)

        btn_back = ctk.CTkButton(self, text="Back", command=self.show_user_dashboard)
        btn_back.pack(pady=10)

    def save_income(self):
        amount_str = self.income_entry.get()
        try:
            amount = float(amount_str)
            # Add to CSV
            adding(self.current_csv, "NA", "NA", "NA", "Income", amount)
            self.message_box("Income added.")
        except:
            self.message_box("Invalid amount.")

    def add_expense(self):
        self.clear_window()
        lbl = ctk.CTkLabel(self, text="Add Expense")
        lbl.pack(pady=5)
        self.expense_entry = ctk.CTkEntry(self)
        self.expense_entry.pack(pady=5)

        btn_add = ctk.CTkButton(self, text="Add Expense", command=self.save_expense)
        btn_add.pack(pady=10)

        btn_back = ctk.CTkButton(self, text="Back", command=self.show_user_dashboard)
        btn_back.pack(pady=10)

    def save_expense(self):
        amount_str = self.expense_entry.get()
        try:
            amount = float(amount_str)
            adding(self.current_csv, "NA", "NA", "NA", "Expense", amount)
            self.message_box("Expense added.")
        except:
            self.message_box("Invalid amount.")

    # --- View Data ---
    def view_data(self):
        self.clear_window()
        lbl = ctk.CTkLabel(self, text="Data from CSV")
        lbl.pack(pady=5)
        self.data_text = ctk.CTkTextbox(self, width=800, height=400)
        self.data_text.pack(pady=5)

        # Read CSV and display
        try:
            with open(self.current_csv, 'r') as f:
                content = f.read()
            self.data_text.insert("0.0", content)
        except:
            self.data_text.insert("0.0", "No data available.")
        btn_back = ctk.CTkButton(self, text="Back", command=self.show_user_dashboard)
        btn_back.pack(pady=10)
        self.current_widgets.append(self.data_text)
        self.current_widgets.append(btn_back)

    # --- Utility ---
    def currency_convert(self, amount_usd, selection):
        symbol, converted = self.convert_money(selection, amount_usd)
        return symbol, converted

    def convert_money(self, selection, usd_amount):
        if selection == "USD":
            symbol = "$"
            return symbol, usd_amount
        elif selection == "EUROS":
            return "€", usd_amount * 0.87
        elif selection == "BRITISH POUND":
            return "£", usd_amount * 0.75
        elif selection == "JAPANESE YEN":
            return "¥", usd_amount * 159.60
        elif selection == "CHINESE RENMINBI":
            return "CN¥", usd_amount * 6.91
        else:
            return "", usd_amount

# --- Run the app ---
if __name__ == "__main__":
    app = App(x=0)
    app.mainloop()