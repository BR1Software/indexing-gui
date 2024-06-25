import customtkinter
import os
from dotenv import load_dotenv

load_dotenv()

server_url = os.getenv("SERVER_URL")

class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="grey30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10,0), sticky="ew")
        
        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)
    
    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get():
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes
        
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Indexer GUI")
        self.geometry("800x600")
        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure(0)

        # Search Label
        self.search_label = customtkinter.CTkLabel(self, text="Enter your search", fg_color="transparent")
        self.search_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        # Search Box
        self.search_entry = customtkinter.CTkEntry(self, placeholder_text="enter your search term")
        self.search_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
        # Search Button
        self.search_button = customtkinter.CTkButton(self, text="Search", command=self.search_button_callback)
        self.search_button.grid(row=0, column=2, padx=10, pady=10, sticky="ew")
        
        # Include Emails
        switch_var = customtkinter.StringVar(value="off")
        self.inc_emails = customtkinter.CTkSwitch(self, text="Inc. Emails", command=self.switch_event, 
                                                variable=switch_var, onvalue="on", offvalue="off")
        self.inc_emails.grid(row=0, column=3, padx=10, pady=10, sticky="ew")
        
        self.checkbox_frame_1 = MyCheckboxFrame(self, "Values", values=["value 1", "value 2", "value 3"])
        self.checkbox_frame_1.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.checkbox_frame_2 = MyCheckboxFrame(self, "Options", values=["option 1", "option 2"])
        self.checkbox_frame_2.grid(row=1, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=2, column=0, padx=10, pady=10, sticky="sew", columnspan=2)
        
    def search_button_callback(self):
        print("Search:", self.search_entry.get())
    
    def button_callback(self):
        print("checkbox_frame_1:", self.checkbox_frame_1.get())
        print("checkbox_frame_2:", self.checkbox_frame_2.get())
        
    def switch_event(self):
        print("Switch event:", self.inc_emails.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()