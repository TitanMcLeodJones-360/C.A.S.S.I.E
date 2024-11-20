import tkinter as tk
from tkinter import messagebox
from diagnostics.software_diagnostics import SoftwareDiagnostics
from diagnostics.system_diagnostics import SystemDiagnostics
from diagnostics.hardware_diagnostics import HardwareDiagnostics
from storage.storage_management import StorageManagement
from web.notifications_communications import Notifications

class Dashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("C.A.S.S.I.E Dashboard")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        # Modules
        self.notifications = Notifications()
        self.storage_manager = StorageManagement()
        self.software_diag = SoftwareDiagnostics()
        self.system_diag = SystemDiagnostics()
        self.hardware_diag = HardwareDiagnostics()

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
            "Browser",
            "Notifications"
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
        if label == "Notifications":
            self.show_notifications()
        elif label == "System Diagnostics":
            self.run_diagnostics()
        elif label == "Storage Systems":
            self.show_storage_management()
        else:
            messagebox.showinfo("Button Clicked", f"You clicked: {label}")

    def show_notifications(self):
        notifications = self.notifications.get_notifications()
        if notifications:
            notifications_text = "\n".join([f"[{n['timestamp']}] ({n['level']}) {n['message']}" for n in notifications])
            messagebox.showinfo("Notifications", notifications_text)
        else:
            messagebox.showinfo("Notifications", "No notifications at this time.")

    def run_diagnostics(self):
        self.software_diag.scan_for_malware()
        self.system_diag.check_cpu_health()
        self.hardware_diag.scan_devices()
        self.notifications.add_notification("System diagnostics completed.", "info")
        messagebox.showinfo("Diagnostics", "System diagnostics completed. Check notifications for details.")

    def show_storage_management(self):
        self.storage_manager.display_storage_usage()
        self.notifications.add_notification("Storage usage displayed.", "info")
        messagebox.showinfo("Storage Management", "Storage usage displayed in the logs.")

    def process_command(self):
        command = self.command_entry.get()
        if not command.strip():
            messagebox.showwarning("Empty Command", "Please enter a command!")
        else:
            self.notifications.add_notification(f"Command received: {command}", "info")
            messagebox.showinfo("Command Received", f"Processing: {command}")

    def launch(self):
        self.create_dashboard()
        self.root.mainloop()
