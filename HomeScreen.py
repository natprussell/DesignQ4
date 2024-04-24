import tkinter as tk
from tkinter import ttk
import random 

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Electronic Health Record System")
        self.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        # Welcome Message
        welcome_label = tk.Label(self, text="Welcome to Golden Oaks Haven!", font=("Arial", 18))
        welcome_label.pack(pady=20)

        # Navigation Menu
        navigation_frame = tk.Frame(self)
        navigation_frame.pack()

        search_button = ttk.Button(navigation_frame, text="Search", command=self.show_search)
        search_button.grid(row=0, column=0, padx=10, pady=10)

        settings_button = ttk.Button(navigation_frame, text="Settings", command=self.show_settings)
        settings_button.grid(row=0, column=1, padx=10, pady=10)

        admission_button = ttk.Button(navigation_frame, text="Admission", command=self.show_admission)
        admission_button.grid(row=0, column=2, padx=10, pady=10)

        # Placeholder panes
        self.search_pane = tk.Frame(self)
        self.search_pane.pack(fill="both", expand=True)
        search_label = tk.Label(self.search_pane, text="Enter Patient ID:")
        search_label.pack(pady=10)
        self.search_entry = tk.Entry(self.search_pane)
        self.search_entry.pack(pady=10)
        search_button = ttk.Button(self.search_pane, text="Search", command=self.search_patient)
        search_button.pack(pady=10)

        self.settings_pane = tk.Frame(self)
        self.settings_pane.pack(pady=10, fill="both", expand=True)

        settings_label = tk.Label(self.settings_pane, text="Settings", font=("Arial", 16, "bold"))
        settings_label.grid(row=0, column=0, columnspan=2, pady=10)

        font_size_label = tk.Label(self.settings_pane, text="Font Size:")
        font_size_label.grid(row=1, column=0, padx=10, pady=5)
        self.font_size_var = tk.StringVar(value="12")
        font_size_entry = tk.Entry(self.settings_pane, textvariable=self.font_size_var, width=10)
        font_size_entry.grid(row=1, column=1, padx=10, pady=5)

        password_button = ttk.Button(self.settings_pane, text="Change Password", command=self.change_password)
        password_button.grid(row=2, column=0, columnspan=2, pady=10)

        tooltip_var = tk.BooleanVar()
        tooltip_checkbutton = tk.Checkbutton(self.settings_pane, text="Show Tooltips", variable=tooltip_var)
        tooltip_checkbutton.grid(row=3, column=0, columnspan=2, pady=5)

        self.admission_pane = tk.Frame(self)
        self.admission_pane.pack(fill="both", expand=True)

        # Create a canvas with a scrollbar
        canvas = tk.Canvas(self.admission_pane)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar = ttk.Scrollbar(self.admission_pane, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the admission form fields
        admission_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=admission_frame, anchor="nw")

        # Add admission form fields
        labels = ["Name:", "Age:", "Gender:", "Date of Birth:", "Current Medications:",
                  "Medical History:", "Insurance Information:", "Admission Date:",
                  "Next of Kin:", "Outpatient Services:"]
        for i, label_text in enumerate(labels):
            label = tk.Label(admission_frame, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(admission_frame)
            entry.grid(row=i, column=1, padx=10, pady=5)

        # Configure the canvas to update scroll region
        admission_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        save_button = ttk.Button(self.admission_pane, text="Save Admission Record", command=self.save_admission)
        save_button.pack(pady=10)

        # Label to display generated PatientID
        self.patient_id_label = tk.Label(self.admission_pane, text="", font=("Arial", 12, "bold"), fg="blue")
        self.patient_id_label.pack(pady=10)


        # Hide all panes initially
        self.hide_all_panes()

    def show_search(self):
        self.hide_all_panes()
        self.search_pane.pack(fill="both", expand=True)

    def show_settings(self):
        self.hide_all_panes()
        self.settings_pane.pack(fill="both", expand=True)

    def show_admission(self):
        self.hide_all_panes()
        self.admission_pane.pack(fill="both", expand=True)

    def hide_all_panes(self):
        self.search_pane.pack_forget()
        self.settings_pane.pack_forget()
        self.admission_pane.pack_forget()

    def search_patient(self):
        patient_id = self.search_entry.get()
        # Implement search functionality using the patient_id
        print("Searching for patient with ID:", patient_id)

    def change_password(self):
        # Implement password change functionality
        print("Changing password...")

    def save_admission(self):
        # Generate a unique PatientID (for demonstration purposes, using a random integer)
        patient_id = random.randint(10000, 99999)
        # Print the admission details and the generated PatientID
        print("Admission Record Saved.")
        print("PatientID:", patient_id)
        # Display the PatientID on the window
        self.patient_id_label.config(text="PatientID: " + str(patient_id))

if __name__ == "__main__":
    app = Application()
    app.mainloop()
