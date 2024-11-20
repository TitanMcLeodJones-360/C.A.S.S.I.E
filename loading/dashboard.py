import tkinter as tk
from tkinter import messagebox
from diagnostics.software_diagnostics import SoftwareDiagnostics
from diagnostics.system_diagnostics import SystemDiagnostics
from diagnostics.hardware_diagnostics import HardwareDiagnostics
from storage.storage_management import StorageManagement

class Dashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("C.A.S.S.I.E Dashboard")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

    def create_dashboard(self):
        # Logo
        logo_label = tk.Label(self.root, text="C.A.S.S.I.E", font=("Arial", 24, "bold"), fg="white", bg="black")
        logo_label.pack(pady=20)

        # Buttons
        buttons_frame = tk.Frame(self.root, bg="black")
        buttons_frame.pack(pady=10)

        button_labels = [
            "Logs/Documents",
            "Storage Systems",
            "System Diagnostics",
            "Hardware Controls",
            "Settings",
            "Browser"
        ]
        for label in button_labels:
            btn = tk.Button(
                buttons_frame,
                text=label,
                font=("Arial", 14),
                bg="gray",
                fg="white",
                width=20,
                height=2,
                command=lambda l=label: self.handle_button_click(l)
            )
            btn.pack(pady=5)

        # Text Input for Commands
        command_label = tk.Label(self.root, text="Command Input:", font=("Arial", 14), fg="white", bg="black")
        command_label.pack(pady=10)

        self.command_entry = tk.Entry(self.root, font=("Arial", 14), width=50)
        self.command_entry.pack(pady=10)

        submit_button = tk.Button(
            self.root,
            text="Submit",
            font=("Arial", 14),
            bg="gray",
            fg="white",
            command=self.process_command
        )
        submit_button.pack(pady=10)

    def handle_button_click(self, label):
        if label == "System Diagnostics":
            self.run_diagnostics()
        elif label == "Storage Systems":
            self.show_storage_management()
        else:
            messagebox.showinfo("Button Clicked", f"You clicked: {label}")

    def run_diagnostics(self):
        software_diag = SoftwareDiagnostics()
        system_diag = SystemDiagnostics()
        hardware_diag = HardwareDiagnostics()

        software_diag.scan_for_malware()
        system_diag.check_cpu_health()
        hardware_diag.scan_devices()

        messagebox.showinfo("Diagnostics Complete", "System diagnostics have been completed.")

    def show_storage_management(self):
        storage_manager = StorageManagement()
        storage_manager.display_storage_usage()
        messagebox.showinfo("Storage Management", "Storage usage displayed in the logs.")

    def process_command(self):
        command = self.command_entry.get()
        if not command.strip():
            messagebox.showwarning("Empty Command", "Please enter a command!")
        else:
            messagebox.showinfo("Command Received", f"Processing: {command}")

    def launch(self):
        self.create_dashboard()
        self.root.mainloop()
