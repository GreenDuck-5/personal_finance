import customtkinter as ctk

# Set the appearance and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Main Application")
        self.geometry("400x400") # Adjusted geometry to fit both pages if needed
        self.current_widgets = [] # List to keep track of widgets to destroy

        self.show_main_page()

    def clear_window(self):
        """Destroys all currently packed widgets in the main window."""
        for widget in self.current_widgets:
            widget.destroy()
        self.current_widgets.clear()

    def show_main_page(self):
        self.clear_window()
        self.title("Main Application")

        # Center Button to open the settings view
        self.button = ctk.CTkButton(self, text="Sign in", command=self.show_settings_page)
        self.button.pack(expand=True)
        self.current_widgets.append(self.button) # Track the new widget

        # Optional label to show saved data
        self.data_label = ctk.CTkLabel(self, text="No data saved yet", font=("Helvetica", 14))
        self.data_label.pack(pady=20)
        self.current_widgets.append(self.data_label)

    def show_settings_page(self):
        self.clear_window()
        self.title("User Sign in")

        # Header Label
        header = ctk.CTkLabel(self, text="Enter Your Username and password", font=("Helvetica", 20, "bold"))
        header.pack(pady=(20, 10))
        self.current_widgets.append(header)

        # Text Input (Name)
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Enter your name...", width=250)
        self.name_entry.pack(pady=10)
        self.current_widgets.append(self.name_entry)


        #password
        self.age_option = ctk.CTkEntry(self, placeholder_text= "Enter your password", width = 250)
        self.age_option.pack(pady=10)
        self.current_widgets.append(self.age_option)

        # Save Button
        save_btn = ctk.CTkButton(self, text="Save & Return", command=self.get_data)
        save_btn.pack(pady=30)
        self.current_widgets.append(save_btn)

    def get_data(self):
        # Retrieve the values from inputs
        name = self.name_entry.get()
        age = self.age_option.get()
        print(f"User Name: {name}, Age Category: {age}")
        
        # Update the main page's label before returning to it
        self.show_main_page()
        self.data_label.configure(text=f"Last saved: Name: {name}, Age: {age}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
