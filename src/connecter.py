#RC 1st, runs most stuff
import customtkinter as ctk
from saving import *
from user_login import sign_in, sign_up
# Set the appearance and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self, x):
        super().__init__()
        self.title("Main Application")
        self.geometry("800x800") # Adjusted geometry to fit both pages if needed
        self.current_widgets = [] # List to keep track of widgets to destroy
        self.x = x

        self.show_main_page()

    def clear_window(self):
        #Destroys all currently packed widgets in the main window.
        for widget in self.current_widgets:
            widget.destroy()
        self.current_widgets.clear()

    def show_sign_up_page(self):
        self.clear_window()
        self.title("Sign Up")

        header = ctk.CTkLabel(self, text="Enter Your Username and password", font=("Helvetica", 20, "bold"))
        header.pack(pady=(20, 10))
        self.current_widgets.append(header)

        self.name_entry = ctk.CTkEntry(self, placeholder_text="Enter your username...", width=250)
        self.name_entry.pack(pady=10)
        self.current_widgets.append(self.name_entry)

        self.password_entry = ctk.CTkEntry(self, placeholder_text= "Enter your password", width = 250)
        self.password_entry.pack(pady=10)
        self.current_widgets.append(self.password_entry)

        #Create save button that imploys lizzies sing up function
        save_bt = ctk.CTkButton(self, text="Save & Return", command=self.get_data)
        save_bt.pack(pady=30)
        self.current_widgets.append(save_bt)

                    #CHECK TO SEE IF LABLE AND SING IN STUFF WORKS
        self.data_label = ctk.CTkLabel(self, text="Enter the password you would like\nPassword must be 12 characters long (maximum is 40), have a number, have an uppercase, have a lowercase, have a special character, and NO spaces\nIf you want to go back to main, type EXIT in username and EXIT in password", font=("Helvetica", 14))
        self.data_label.pack(pady=20)
        self.current_widgets.append(self.data_label)

        self.x = 2
        


    def view_graphs(self):
        pass



    def edit_budgets(self):
        pass

    def edit_income_and_expenses(self):
        pass

    def view_savings(self):
        self.values = ""
        self.clear_window()
        

        words = ["Create saving plan", "View saving plan", "Go back"]
        self.seg_buttonss = ctk.CTkSegmentedButton(self, values=words, command = self.callback)
        self.seg_buttonss.pack(padx=20, pady=10)
        self.current_widgets.append(self.seg_buttonss)
            


        if self.values == "Create saving plan":
            self.clear_window()
            saving_amount, deposit_often, deposit_amount, monthly_expense, saving_time = create_saving_plan()
            
            self.buttun = ctk.CTkButton(self, text="Go back", command=self.show_button_page)
            self.buttun.pack(expand=True)
            self.current_widgets.append(self.buttun)


        elif self.values == "View saving plan":
            if saving_amount != ""  and deposit_often != "" and deposit_amount != "" and monthly_expense != "" and saving_time != "":
                self.clear_window()
                headerrs = ctk.CTkLabel(self, text=f"""Your current saving plan is:
                            How much are you saving to?: {saving_amount}
                            How often are you adding money?: {deposit_often}
                            How much are you putting in?: {deposit_amount}
                            What is the monthly expense?: {monthly_expense}
                            How long until finished saving?: {saving_time} months
          """, font =("Helvetica", 20, "bold"))
                headerrs.pack(pady=(20, 10))
                self.current_widgets.append(headerrs)

                self.button = ctk.CTkButton(self, text="Go back", command=self.show_button_page)
                self.button.pack(expand=True)
                self.current_widgets.append(self.button)





            else:
                headerr = ctk.CTkLabel(self, text="You have no saving plans", font =("Helvetica", 20, "bold"))
                headerr.pack(pady=(20, 10))
                self.current_widgets.append(headerr)


        elif self.values == "Go back":
            self.show_button_page()
        
        else:
            pass


    def show_button_page(self):
        self.clear_window()
        #View charts of expenses button
        save_bt = ctk.CTkButton(self, text="View Graphs", command=self.view_graphs)
        save_bt.pack(pady=30)
        self.current_widgets.append(save_bt)

        #Savings button (Send to new window)
        save_bt = ctk.CTkButton(self, text="View Savings", command=self.view_savings)
        save_bt.pack(pady=30)
        self.current_widgets.append(save_bt)
        #Deal with budgets button (sent to new window)
        save_bt = ctk.CTkButton(self, text="Edit Budgets", command=self.edit_budgets)
        save_bt.pack(pady=30)
        self.current_widgets.append(save_bt)
        #Edit income and expenses 
        save_bt = ctk.CTkButton(self, text="Edit income and expenses", command=self.edit_income_and_expenses)
        save_bt.pack(pady=30)
        self.current_widgets.append(save_bt)


        #Sign out
        self.button = ctk.CTkButton(self, text="Sign out", command=self.show_main_page)
        self.button.pack(expand=True)
        self.current_widgets.append(self.button)
        



    def show_main_page(self):

        self.clear_window()
        self.title("Main Application")

        # Center Button to open the settings view
        self.button = ctk.CTkButton(self, text="Sign in", command=self.show_sign_in_page)
        self.button.pack(expand=True)
        self.current_widgets.append(self.button) # Track the new widget

        self.button.place(x= 330, y= 200)

        # Center Button to open the sign up page
        self.buttons = ctk.CTkButton(self, text="Create account", command=self.show_sign_up_page)
        self.buttons.pack(expand=True)
        self.current_widgets.append(self.buttons) # Track the new widget
        
        self.buttons.place(x= 330, y= 325)

        # Center Button to exit
        self.butto = ctk.CTkButton(self, text="Exit", command=self.destroy)
        self.butto.pack(expand=True)
        self.current_widgets.append(self.butto) # Track the new widget
        
        self.butto.place(x= 330, y= 450)

        # Optional label to show saved data
        self.data_label = ctk.CTkLabel(self, text="No data saved yet", font=("Helvetica", 14))
        self.data_label.pack(pady=20)
        self.current_widgets.append(self.data_label)

    def show_sign_in_page(self):
        self.clear_window()
        self.title("User Sign in")

        # Header Label
        header = ctk.CTkLabel(self, text="Enter Your Username and password", font=("Helvetica", 20, "bold"))
        header.pack(pady=(20, 10))
        self.current_widgets.append(header)

        # Text Input (Name)
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Enter your username...", width=250)
        self.name_entry.pack(pady=10)
        self.current_widgets.append(self.name_entry)


        #password
        self.password_entry = ctk.CTkEntry(self, placeholder_text= "Enter your password", width = 250)
        self.password_entry.pack(pady=10)
        self.current_widgets.append(self.password_entry)

        # Save Button
        save_btn = ctk.CTkButton(self, text="Save & Return", command=self.get_data)
        save_btn.pack(pady=30)
        self.current_widgets.append(save_btn)

        self.data_label = ctk.CTkLabel(self, text="If you want to go back to main, type EXIT in username and EXIT in password (ALL CAPS)", font=("Helvetica", 14))
        self.data_label.pack(pady=20)
        self.current_widgets.append(self.data_label)
        self.x = 1

    def callback(self, value):
        self.currency = value
        self.show_button_page()

    def show_currency_page(self):
        self.clear_window()
        self.title("Hello, you are singed in")

        self.data_label = ctk.CTkLabel(self, text="Please select your currency", font=("Helvetica", 14))
        self.data_label.pack(pady=20)
        self.current_widgets.append(self.data_label)



        
        words = ["USD", "EUROS", "BRITISH POUND", "JAPANESE YEN", "CHINESE RENMINBI"]
        self.seg_button = ctk.CTkSegmentedButton(self, values=words, command=self.callback)
        self.seg_button.pack(padx=20, pady=10)
        self.current_widgets.append(self.seg_button)






        self.button = ctk.CTkButton(self, text="Sign out", command=self.show_main_page)
        self.button.pack(expand=True)
        self.current_widgets.append(self.button) # Track the new widget

    def get_data(self):
        # Retrieve the values from inputs
        name = self.name_entry.get()
        password = self.password_entry.get()
        print(f"User Name: {name}, Password: {password}")
        
        # Update the main page's label before returning to it
        if self.x == 1: #log in
            if name == "EXIT" and password == "EXIT":
                self.show_main_page()
            else:
                current_csv, check =sign_in(name,password)
                self.check = check
                self.current_csv = current_csv
            if self.check == True:
                self.show_currency_page()
                pass
            else:
                self.show_main_page()
                self.data_label.configure(text=f"Your username and password do not match, please either create an account or log in correctly...")

        if self.x == 2: #sign up
            if name == "EXIT" and password == "EXIT":
                self.show_main_page()
            else:
                self.current_csv, self.check = sign_up(name, password)
                if self.check == True:
                    self.show_currency_page()
                #Create the new menu
                else:
                    self.data_label.configure(text=f"Your username and password do not match the requirments...")




    
#Lizzie_eevee
#M1stB0rn