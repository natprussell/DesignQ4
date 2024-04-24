import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Patient Information")
        self.geometry("1000x600")

        self.create_widgets()

    def create_widgets(self):
        # Label to display PatientID
        self.patient_id_label = tk.Label(self, text="PatientID: ", font=("Arial", 12, "bold"))
        self.patient_id_label.pack(pady=10)

        # Notebook widget to organize panes
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        # Panes for vital signs, medication, treatment, and order requests
        self.vital_signs_frame = tk.Frame(notebook)
        medication_frame = tk.Frame(notebook)
        treatment_frame = tk.Frame(notebook)
        order_requests_frame = tk.Frame(notebook)

        notebook.add(self.vital_signs_frame, text="Vital Signs")
        notebook.add(medication_frame, text="Medication")
        notebook.add(treatment_frame, text="Treatment")
        notebook.add(order_requests_frame, text="Order Requests")

        # Placeholder labels in each pane
        vital_signs_label = tk.Label(self.vital_signs_frame, text="Enter Vital Signs", font=("Arial", 14, "bold"))
        vital_signs_label.pack(pady=20)

        # Entry fields for vital signs
        self.temperature_entry = self.create_entry_with_label(self.vital_signs_frame, "Temperature:")
        self.blood_pressure_entry = self.create_entry_with_label(self.vital_signs_frame, "Blood Pressure:")
        self.pulse_rate_entry = self.create_entry_with_label(self.vital_signs_frame, "Pulse Rate:")
        self.respiratory_rate_entry = self.create_entry_with_label(self.vital_signs_frame, "Respiratory Rate:")

        # Buttons to save or discard changes
        save_button = tk.Button(self.vital_signs_frame, text="Save Changes", command=self.save_vital_signs)
        save_button.pack(pady=10)
        discard_button = tk.Button(self.vital_signs_frame, text="Discard Changes", command=self.discard_vital_signs)
        discard_button.pack(pady=5)

        # Create a frame for medication details and entry fields
        medication_details_frame = tk.Frame(medication_frame)
        medication_details_frame.pack(fill="both", expand=True)

        # Placeholder text in medication details
        medication_details_text = """
        Medication Details:
        
        1. Medication A - Dosage: 10mg, Frequency: 2 times daily
        2. Medication B - Dosage: 20mg, Frequency: Once daily
        3. Medication C - Dosage: 5mg, Frequency: Every 6 hours
        """

        # Create a text widget for medication details
        medication_details_text_widget = tk.Text(medication_details_frame, wrap="word", font=("Arial", 12))
        medication_details_text_widget.insert(tk.END, medication_details_text)
        medication_details_text_widget.configure(state='disabled')
        medication_details_text_widget.pack(side=tk.LEFT, fill="both", expand=True)

        # Entry fields for medication details
        medication_entry_frame = tk.Frame(medication_details_frame)
        medication_entry_frame.pack(side=tk.RIGHT, padx=10)

        medication_label = tk.Label(medication_entry_frame, text="Record Medication Outputs", font=("Arial", 14, "bold"))
        medication_label.pack(pady=20)

        self.medication_entry = self.create_entry_with_label(medication_entry_frame, "Medication:")
        self.dosage_entry = self.create_entry_with_label(medication_entry_frame, "Dosage:")

        # Buttons to save or discard changes
        save_button = tk.Button(medication_frame, text="Save Changes", command=self.save_medication)
        save_button.pack(pady=10)
        discard_button = tk.Button(medication_frame, text="Discard Changes", command=self.discard_medication)
        discard_button.pack(pady=5)

    
         # Placeholder labels in each pane
        treatment_label = tk.Label(treatment_frame, text="Enter Treatment Details", font=("Arial", 14, "bold"))
        treatment_label.pack(pady=20)

        # Entry fields for treatment details
        self.diagnosis_entry = self.create_entry_with_label(treatment_frame, "Diagnosis:")
        self.goals_entry = self.create_entry_with_label(treatment_frame, "Goals:")
        self.treatment_plans_entry = self.create_entry_with_label(treatment_frame, "Treatment Plans:")
        self.progress_notes_entry = self.create_entry_with_label(treatment_frame, "Progress Notes:")

        # Buttons to save or discard changes
        save_button = tk.Button(treatment_frame, text="Save Changes", command=self.save_treatment)
        save_button.pack(side="right", pady=10)
        discard_button = tk.Button(treatment_frame, text="Discard Changes", command=self.discard_treatment)
        discard_button.pack(pady=5)

         # Placeholder labels in each pane
        order_requests_label = tk.Label(order_requests_frame, text="Enter Order Requests", font=("Arial", 14, "bold"))
        order_requests_label.pack(pady=20)

        # Entry fields for order requests
        self.medication_order_entry = self.create_entry_with_label(order_requests_frame, "Medication Order:")
        self.dietary_order_entry = self.create_entry_with_label(order_requests_frame, "Dietary Order:")
        self.lab_order_entry = self.create_entry_with_label(order_requests_frame, "Lab Order:")

        # Button to send orders
        send_button = tk.Button(order_requests_frame, text="Send Orders", command=self.send_orders)
        send_button.pack(pady=10)

    def create_entry_with_label(self, parent, label_text):
        frame = tk.Frame(parent)
        frame.pack(pady=5)
        label = tk.Label(frame, text=label_text)
        label.pack(side="left")
        entry = tk.Entry(frame)
        entry.pack(side="right")
        return entry

    def save_vital_signs(self):
        # Get vital sign values from entry fields
        temperature = self.temperature_entry.get()
        blood_pressure = self.blood_pressure_entry.get()
        pulse_rate = self.pulse_rate_entry.get()
        respiratory_rate = self.respiratory_rate_entry.get()

        # Validate vital sign values (add your validation logic here)

        # For demonstration purposes, generate a unique VitalSignsID (random integer)
        vital_signs_id = random.randint(10000, 99999)

        # Confirm update and link to PatientID
        confirmation = tk.messagebox.askyesno("Confirm Update", "Are you sure you want to save changes?")
        if confirmation:
            # For demonstration, print confirmation and assign unique VitalSignsID
            print("Vital Signs Updated and Linked to PatientID.")
            print("VitalSignsID:", vital_signs_id)
        else:
            print("Changes discarded.")

    def discard_vital_signs(self):
        # Prompt user to confirm discarding changes
        confirmation = tk.messagebox.askyesno("Confirm Discard", "Are you sure you want to discard changes?")
        if confirmation:
            # Clear entry fields
            self.temperature_entry.delete(0, tk.END)
            self.blood_pressure_entry.delete(0, tk.END)
            self.pulse_rate_entry.delete(0, tk.END)
            self.respiratory_rate_entry.delete(0, tk.END)
            print("Changes discarded.")
        else:
            print("Discard operation cancelled.")

    def save_medication(self):
        # Get medication details from entry fields
        medication = self.medication_entry.get()
        dosage = self.dosage_entry.get()
        frequency = self.frequency_entry.get()

        # Validate medication details (add your validation logic here)

        # For demonstration purposes, generate a unique MedicationID (random integer)
        medication_id = random.randint(10000, 99999)

        # Confirm update and link to PatientID
        confirmation = tk.messagebox.askyesno("Confirm Update", "Are you sure you want to save changes?")
        if confirmation:
            # For demonstration, print confirmation and assign unique MedicationID
            print("Medication Updated and Linked to PatientID.")
            print("MedicationID:", medication_id)
        else:
            print("Changes discarded.")

    def discard_medication(self):
        # Prompt user to confirm discarding changes
        confirmation = tk.messagebox.askyesno("Confirm Discard", "Are you sure you want to discard changes?")
        if confirmation:
            # Clear entry fields
            self.medication_entry.delete(0, tk.END)
            self.dosage_entry.delete(0, tk.END)
            self.frequency_entry.delete(0, tk.END)
            print("Changes discarded.")
        else:
            print("Discard operation cancelled.")

    def save_treatment(self):
        # Get treatment details from entry fields
        diagnosis = self.diagnosis_entry.get()
        goals = self.goals_entry.get()
        treatment_plans = self.treatment_plans_entry.get()
        progress_notes = self.progress_notes_entry.get()

        # Validate treatment details (add your validation logic here)

        # For demonstration purposes, generate a unique TreatmentID (random integer)
        treatment_id = random.randint(10000, 99999)

        # Confirm update and link to PatientID and PhysicianID
        confirmation = tk.messagebox.askyesno("Confirm Update", "Are you sure you want to save changes?")
        if confirmation:
            # For demonstration, print confirmation and assign unique TreatmentID
            print("Treatment Updated and Linked to PatientID and PhysicianID.")
            print("TreatmentID:", treatment_id)
        else:
            print("Changes discarded.")

    def discard_treatment(self):
        # Prompt user to confirm discarding changes
        confirmation = tk.messagebox.askyesno("Confirm Discard", "Are you sure you want to discard changes?")
        if confirmation:
            # Clear entry fields
            self.diagnosis_entry.delete(0, tk.END)
            self.goals_entry.delete(0, tk.END)
            self.treatment_plans_entry.delete(0, tk.END)
            self.progress_notes_entry.delete(0, tk.END)
            print("Changes discarded.")
        else:
            print("Discard operation cancelled.")

    def send_orders(self):
        # Get order details from entry fields
        medication_order = self.medication_order_entry.get()
        dietary_order = self.dietary_order_entry.get()
        lab_order = self.lab_order_entry.get()

        # Timestamp orders
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Send orders to specified providers (add your sending logic here)

        # For demonstration purposes, print orders and timestamp
        print("Medication Order:", medication_order)
        print("Dietary Order:", dietary_order)
        print("Lab Order:", lab_order)
        print("Orders Sent at:", timestamp)


    def set_patient_id(self, patient_id):
        self.patient_id_label.config(text="PatientID: " + str(patient_id))

if __name__ == "__main__":
    app = Application()
    app.mainloop()

