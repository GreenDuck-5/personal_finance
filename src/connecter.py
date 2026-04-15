import customtkinter as ctk
from user_login import sign_in, sign_up
import os

from data_manager import DataManager
from visual import Visualizer
from savings import SavingsTracker

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Main Application")
        self.geometry("900x700")
        self.current_widgets = []

        self.after_id = None
        self.budget_limits = {}

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # User info
        self.current_csv = None
        self.username = None

        # Data
        self.data_manager = None
        self.visualizer = Visualizer()
        self.savings_tracker = None

        self.show_main_page()

    def on_closing(self):
        self.cancel_pending_callbacks()
        self.destroy()

    def cancel_pending_callbacks(self):
        if hasattr(self, 'after_id') and self.after_id is not None:
            try:
                self.after_cancel(self.after_id)
            except:
                pass
            self.after_id = None

    def clear_window(self):
        for widget in self.current_widgets:
            widget.destroy()
        self.current_widgets.clear()

    # Main page
    def show_main_page(self):
        self.cancel_pending_callbacks()
        self.clear_window()
        btn_sign_in = ctk.CTkButton(self, text="Sign in", command=self.show_sign_in_page)
        btn_sign_in.pack(pady=20)
        self.current_widgets.append(btn_sign_in)

        btn_sign_up = ctk.CTkButton(self, text="Create account", command=self.show_sign_up_page)
        btn_sign_up.pack(pady=20)
        self.current_widgets.append(btn_sign_up)

        btn_exit = ctk.CTkButton(self, text="Exit", command=self.destroy)
        btn_exit.pack(pady=20)
        self.current_widgets.append(btn_exit)

    # Sign in
    def show_sign_in_page(self):
        self.cancel_pending_callbacks()
        self.clear_window()
        header = ctk.CTkLabel(self, text="Sign In", font=("Helvetica", 20, "bold"))
        header.pack(pady=10)
        self.current_widgets.append(header)

        self.name_entry = ctk.CTkEntry(self, placeholder_text="Username")
        self.name_entry.pack(pady=5)
        self.current_widgets.append(self.name_entry)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=5)
        self.current_widgets.append(self.password_entry)

        btn_sign_in = ctk.CTkButton(self, text="Sign In", command=self.get_sign_in_data)
        btn_sign_in.pack(pady=10)
        self.current_widgets.append(btn_sign_in)

        self.signin_message = ctk.CTkLabel(self, text="")
        self.signin_message.pack(pady=5)
        self.current_widgets.append(self.signin_message)

    def get_sign_in_data(self):
        name = self.name_entry.get()
        password = self.password_entry.get()
        self.current_csv, check = sign_in(name, password)
        if check:
            self.username = name
            self.data_manager = DataManager(self.current_csv)
            self.show_button_page()
        else:
            self.signin_message.configure(text="Invalid username or password.")

    # Sign up
    def show_sign_up_page(self):
        self.cancel_pending_callbacks()
        self.clear_window()
        header = ctk.CTkLabel(self, text="Sign Up", font=("Helvetica", 20, "bold"))
        header.pack(pady=10)
        self.current_widgets.append(header)

        self.name_entry = ctk.CTkEntry(self, placeholder_text="New Username")
        self.name_entry.pack(pady=5)
        self.current_widgets.append(self.name_entry)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="New Password", show="*")
        self.password_entry.pack(pady=5)
        self.current_widgets.append(self.password_entry)

        btn_sign_up = ctk.CTkButton(self, text="Register", command=self.get_sign_up_data)
        btn_sign_up.pack(pady=10)
        self.current_widgets.append(btn_sign_up)

        self.signup_message = ctk.CTkLabel(self, text="")
        self.signup_message.pack(pady=5)
        self.current_widgets.append(self.signup_message)

    def get_sign_up_data(self):
        name = self.name_entry.get()
        password = self.password_entry.get()
        self.current_csv, check = sign_up(name, password)
        if check:
            self.username = name
            self.data_manager = DataManager(self.current_csv)
            self.show_button_page()
        else:
            self.signup_message.configure(text="Sign-up failed.")

    # Main menu
    def show_button_page(self):
        self.cancel_pending_callbacks()
        self.clear_window()
        lbl_welcome = ctk.CTkLabel(self, text=f"Welcome, {self.username}!", font=("Helvetica", 16))
        lbl_welcome.pack(pady=10)
        self.current_widgets.append(lbl_welcome)

        btn_graphs = ctk.CTkButton(self, text="View Expense Graphs", command=self.view_graphs)
        btn_graphs.pack(pady=10)
        self.current_widgets.append(btn_graphs)

        btn_savings = ctk.CTkButton(self, text="View Savings", command=self.view_saving)
        btn_savings.pack(pady=10)
        self.current_widgets.append(btn_savings)

        btn_budgets = ctk.CTkButton(self, text="Edit Budgets", command=self.edit_budgets)
        btn_budgets.pack(pady=10)
        self.current_widgets.append(btn_budgets)

        btn_income_exp = ctk.CTkButton(self, text="Edit Income/Expenses", command=self.edit_income_and_expenses)
        btn_income_exp.pack(pady=10)
        self.current_widgets.append(btn_income_exp)

        btn_signout = ctk.CTkButton(self, text="Sign Out", command=self.show_main_page)
        btn_signout.pack(pady=10)
        self.current_widgets.append(btn_signout)

    def view_graphs(self):
        expenses = self.data_manager.get_expenses_by_category()
        categories = list(expenses.keys())
        amounts = list(expenses.values())
        self.visualizer.expense_pie_chart(categories, amounts)

    def view_saving(self):
        self.cancel_pending_callbacks()
        self.clear_window()
        lbl_title = ctk.CTkLabel(self, text="Your Savings Progress", font=("Helvetica", 16))
        lbl_title.pack(pady=10)
        self.current_widgets.append(lbl_title)

        if self.savings_tracker:
            progress = self.savings_tracker.progress()
            current = self.savings_tracker.current
            goal = self.savings_tracker.goal
        else:
            progress = 0
            current = 0
            goal = 0

        self.savings_current_lbl = ctk.CTkLabel(self, text=f"Current Savings: ${current}")
        self.savings_current_lbl.pack(pady=5)
        self.current_widgets.append(self.savings_current_lbl)

        self.savings_goal_lbl = ctk.CTkLabel(self, text=f"Goal: ${goal}")
        self.savings_goal_lbl.pack(pady=5)
        self.current_widgets.append(self.savings_goal_lbl)

        self.savings_progress_lbl = ctk.CTkLabel(self, text=f"Progress: {progress:.2f}%")
        self.savings_progress_lbl.pack(pady=5)
        self.current_widgets.append(self.savings_progress_lbl)

        btn_create = ctk.CTkButton(self, text="Create Savings Plan", command=self.create_saving)
        btn_create.pack(pady=10)
        self.current_widgets.append(btn_create)

        btn_back = ctk.CTkButton(self, text="Back", command=self.show_button_page)
        btn_back.pack(pady=10)
        self.current_widgets.append(btn_back)

    def create_saving(self):
        self.cancel_pending_callbacks()
        self.clear_window()
        ctk.CTkLabel(self, text="Enter Total Savings Goal").pack(pady=10)
        # Re-create the entry widget each time
        self.saving_entry = ctk.CTkEntry(self)
        self.saving_entry.pack(pady=5)
        self.current_widgets.append(self.saving_entry)

        self.deposit_often_var = ctk.StringVar(value="monthly")
        ctk.CTkLabel(self, text="Select frequency:").pack(pady=5)
        

        rb_daily = ctk.CTkRadioButton(self, text="Daily", variable=self.deposit_often_var, value="daily")
        rb_daily.pack()
        self.current_widgets.append(rb_daily)

        rb_weekly = ctk.CTkRadioButton(self, text="Weekly", variable=self.deposit_often_var, value="weekly")
        rb_weekly.pack()
        self.current_widgets.append(rb_weekly)

        rb_monthly = ctk.CTkRadioButton(self, text="Monthly", variable=self.deposit_often_var, value="monthly")
        rb_monthly.pack()
        self.current_widgets.append(rb_monthly)

        save_btn = ctk.CTkButton(self, text="Save Plan", command=self.save_saving)
        save_btn.pack(pady=10)
        self.current_widgets.append(save_btn)

        btn_back = ctk.CTkButton(self, text="Back", command=self.show_button_page)
        btn_back.pack(pady=10)
        self.current_widgets.append(btn_back)

    def save_saving(self):
        if hasattr(self, 'saving_entry'):
            amt_str = self.saving_entry.get()
        else:
            return
        try:
            amount = float(amt_str)
        except:
            return

        # Save the amount
        self.saving_amount = amount

        # Get selected frequency
        freq = self.deposit_often_var.get()

        # Calculate per-period amount based on frequency
        if freq == "daily":
            self.period_label = "per day"
            self.amount_per_period = self.saving_amount / 30
        elif freq == "weekly":
            self.period_label = "per week"
            self.amount_per_period = self.saving_amount / 4
        elif freq == "monthly":
            self.period_label = "per month"
            self.amount_per_period = self.saving_amount / 12
        else:
            self.period_label = ""
            self.amount_per_period = None

        # Initialize savings tracker and set goal
        self.savings_tracker = SavingsTracker()
        self.savings_tracker.set_goal(self.saving_amount)

        # After creating the plan, immediately go back to main menu
        self.show_button_page()

    def edit_budgets(self):
        self.cancel_pending_callbacks()
        self.clear_window()

        # Create the label for displaying budgets
        self.budget_display = ctk.CTkLabel(self, text="Budget limits:")
        self.budget_display.pack(pady=10)
        self.current_widgets.append(self.budget_display)

        self.budget_category_entry = ctk.CTkEntry(self, placeholder_text="Category")
        self.budget_category_entry.pack(pady=5)
        self.current_widgets.append(self.budget_category_entry)

        self.budget_amount_entry = ctk.CTkEntry(self, placeholder_text="Limit")
        self.budget_amount_entry.pack(pady=5)
        self.current_widgets.append(self.budget_amount_entry)

        save_btn = ctk.CTkButton(self, text="Set Limit", command=self.save_budget_limit)
        save_btn.pack(pady=10)
        self.current_widgets.append(save_btn)

        # Load existing budgets if any
        self.load_budgets()

        # Add a "Back" button
        back_button = ctk.CTkButton(self, text="Back", command=self.show_button_page)
        back_button.pack(pady=10)
        self.current_widgets.append(back_button)

    def save_budget_limit(self):
        category = self.budget_category_entry.get()
        amount_str = self.budget_amount_entry.get()
        try:
            amount = float(amount_str)
        except:
            return
        self.budget_limits[category] = amount
        if hasattr(self, 'budget_display'):
            self.budget_display.configure(text=f"{category}: ${amount}")
        self.budget_category_entry.delete(0, 'end')
        self.budget_amount_entry.delete(0, 'end')

    def load_budgets(self):
        # Implement loading budgets if needed
        pass

    def edit_income_and_expenses(self):
        self.cancel_pending_callbacks()
        self.clear_window()

        # Add Income
        lbl_income = ctk.CTkLabel(self, text="Add Income")
        lbl_income.pack(pady=10)
        self.current_widgets.append(lbl_income)

        self.income_entry = ctk.CTkEntry(self, placeholder_text="Income amount")
        self.income_entry.pack(pady=5)
        self.current_widgets.append(self.income_entry)

        btn_add_income = ctk.CTkButton(self, text="Add Income", command=self.add_income)
        btn_add_income.pack(pady=5)
        self.current_widgets.append(btn_add_income)

        # Add Expense
        lbl_expense = ctk.CTkLabel(self, text="Add Expense")
        lbl_expense.pack(pady=10)
        self.current_widgets.append(lbl_expense)

        self.expense_entry = ctk.CTkEntry(self, placeholder_text="Expense amount")
        self.expense_entry.pack(pady=5)
        self.current_widgets.append(self.expense_entry)

        btn_add_expense = ctk.CTkButton(self, text="Add Expense", command=self.add_expense)
        btn_add_expense.pack(pady=5)
        self.current_widgets.append(btn_add_expense)

        # Back button
        back_btn = ctk.CTkButton(self, text="Back", command=self.show_button_page)
        back_btn.pack(pady=10)
        self.current_widgets.append(back_btn)

    def add_income(self):
        amt = self.income_entry.get()
        try:
            amount = float(amt)
            self.data_manager.add_transaction("Income", amount)
        except:
            pass
        self.show_button_page()

    def add_expense(self):
        amt = self.expense_entry.get()
        try:
            amount = float(amt)
            self.data_manager.add_transaction("Expense", amount)
        except:
            pass
        self.show_button_page()