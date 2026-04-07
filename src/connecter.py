#RC 1st, runs most stuff
import customtkinter as ctk
from user_login import sign_in, sign_up
# Set the appearance and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Main Application")
        self.geometry("800x800") # Adjusted geometry to fit both pages if needed
        self.current_widgets = [] # List to keep track of widgets to destroy

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
        save_bt = ctk.CTkButton(self, text="Save & Return", command=self.get_data(2))
        save_bt.pack(pady=30)
        self.current_widgets.append(save_bt)

                    #CHECK TO SEE IF LABLE AND SING IN STUFF WORKS
        self.data_label = ctk.CTkLabel(self, text="Enter the password you would like\nPassword must be 12 characters long (maximum is 40), have a number, have an uppercase, have a lowercase, have a special character, and NO spaces\n", font=("Helvetica", 14))
        self.data_label.pack(pady=20)
        self.current_widgets.append(self.data_label)
        

    def show_main_page(self):

        self.clear_window()
        self.title("Main Application")

        # Center Button to open the settings view
        self.button = ctk.CTkButton(self, text="Sign in", command=self.show_sign_in_page(1))
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

    def get_data(self,x):
        # Retrieve the values from inputs
        name = self.name_entry.get()
        password = self.password_entry.get()
        print(f"User Name: {name}, Password: {password}")
        
        # Update the main page's label before returning to it
        if x == 1: #Sign in
            current_csv = sign_in(name,password)
            self.show_main_page()  #NEED TO PLUG IN LIZZIES CODE
            self.data_label.configure(text=f"Your username and password do not match, please either create an account or log in correctly...")

        if x == 2: #sign up
            current_csv = sign_up(name, password)
            self.show_main_page()  #NEED TO PLUG IN LIZZIES CODE
            self.data_label.configure(text=f"Your username and password do not match, please either create an account or log in correctly...")
if __name__ == "__main__":
    app = App()
    app.mainloop()

#Lizzie_eevee
#M1stB0rn