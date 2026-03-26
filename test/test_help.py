import customtkinter as ctk

# Set the appearance and color theme
ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Main Application")
        self.geometry("400x300")

        # Center Button to open the popup
        self.button = ctk.CTkButton(self, text="Open Input Popup", command=self.open_input_dialog)
        self.button.pack(expand=True)

    def open_input_dialog(self):
        # Create a new top-level window
        self.popup = ctk.CTkToplevel(self)
        self.popup.title("User Settings")
        self.popup.geometry("350x400")
        self.popup.attributes("-topmost", True) # Keep popup on top

        # 1. Header Label
        header = ctk.CTkLabel(self.popup, text="Enter Your Details", font=("Helvetica", 20, "bold"))
        header.pack(pady=(20, 10))

        # 2. Text Input (Name)
        self.name_entry = ctk.CTkEntry(self.popup, placeholder_text="Enter your name...", width=250)
        self.name_entry.pack(pady=10)

        # 3. Number Input (Age)
        age_label = ctk.CTkLabel(self.popup, text="Select Age Range:", font=("Helvetica", 12))
        age_label.pack(pady=(10, 0))
        
        self.age_option = ctk.CTkSegmentedButton(self.popup, values=["18-25", "26-40", "41-60", "60+"])
        self.age_option.set("26-40") # Default value
        self.age_option.pack(pady=10)

        # 4. Save Button
        save_btn = ctk.CTkButton(self.popup, text="Save & Close", command=self.get_data)
        save_btn.pack(pady=30)

    def get_data(self):
        # Retrieve the values from inputs
        name = self.name_entry.get()
        age = self.age_option.get()
        print(f"User Name: {name}, Age Category: {age}")
        self.popup.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
