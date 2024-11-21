import tkinter as tk
from tkinter import messagebox
from commands.command_input import CommandInput
from commands.command_processor import CommandProcessor
from loading.load_and_config import LoadAndConfig
from diagnostics.software_diagnostics import SoftwareDiagnostics
from diagnostics.system_diagnostics import SystemDiagnostics
from diagnostics.hardware_diagnostics import HardwareDiagnostics
from storage.storage_management import StorageManagement
from web.web_browser import WebBrowser
from web.web_browser_settings import WebBrowserSettings
from web.universal_cookie_storage import UniversalCookieStorage
from web.notifications_communications import Notifications
from tools.tool_manager_gui import ToolManagerGUI
from logging.log_viewer import LogViewer
from standby.standby_mode import StandbyMode
from tools.tool_manager import ToolManager


class Dashboard:
    def __init__(self):
        # Initialize the Tkinter root window
        self.root = tk.Tk()
        self.root.title("C.A.S.S.I.E Dashboard")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        # Loading and Config Module
        self.loader = LoadAndConfig()
        self.loader.perform_loading_tasks()

        # Core Modules
        self.notifications = Notifications()
        self.storage_manager = StorageManagement()
        self.software_diag = SoftwareDiagnostics()
        self.system_diag = SystemDiagnostics()
        self.hardware_diag = HardwareDiagnostics()
        self.browser = WebBrowser(driver_path="path/to/chromedriver")
        self.browser_settings = WebBrowserSettings()
        self.cookie_storage = UniversalCookieStorage()
        self.tool_manager = ToolManager()
        self.tool_manager_gui = ToolManagerGUI(tool_manager=self.tool_manager)
        self.log_viewer = LogViewer()
        self.standby_mode = StandbyMode(inactivity_threshold=300)

        # Command Processor
        self.command_processor = CommandProcessor(dashboard=self)

        # Command Input (checks for microphone and voice mode)
        self.command_input = CommandInput()
        self.command_input.voice_mode = self.loader.mic_detected

    def create_dashboard(self):
        # Header Logo
        logo_label = tk.Label(self.root, text="C.A.S.S.I.E", font=("Arial", 24, "bold"), fg="white", bg="black")
        logo_label.pack(pady=20)

        # Buttons Panel
        buttons_frame = tk.Frame(self.root, bg="black")
        buttons_frame.pack(pady=10)

        button_labels = [
            "Logs/Documents",
            "Storage Systems",
            "System Diagnostics",
            "Hardware Controls",
            "Settings",
            "Browser",
            "Notifications",
            "Toggle Standby"
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

        # Command Input Section
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
        """
        Handles clicks for all buttons on the dashboard.
        """
        if label == "Logs/Documents":
            self.log_viewer.show_logs()
        elif label == "Notifications":
            self.show_notifications()
        elif label == "System Diagnostics":
            self.run_diagnostics()
        elif label == "Storage Systems":
            self.show_storage_management()
        elif label == "Hardware Controls":
            self.tool_manager_gui.show_tool_manager()
        elif label == "Browser":
            self.launch_browser()
        elif label == "Settings":
            self.open_settings()
        elif label == "Toggle Standby":
            self.standby_mode.toggle_standby()
        else:
            messagebox.showinfo("Button Clicked", f"You clicked: {label}")

    def show_notifications(self):
        """
        Displays all notifications.
        """
        notifications = self.notifications.get_notifications()
        if notifications:
            notifications_text = "\n".join([f"[{n['timestamp']}] ({n['level']}) {n['message']}" for n in notifications])
            messagebox.showinfo("Notifications", notifications_text)
        else:
            messagebox.showinfo("Notifications", "No notifications at this time.")

    def run_diagnostics(self):
        """
        Executes all diagnostics.
        """
        self.software_diag.scan_for_malware()
        self.system_diag.run_full_diagnostics()
        self.hardware_diag.scan_devices()
        self.notifications.add_notification("System diagnostics completed.", "info")
        messagebox.showinfo("Diagnostics", "System diagnostics completed. Check notifications for details.")

    def show_storage_management(self):
        """
        Displays storage usage and recommendations.
        """
        self.storage_manager.display_storage_usage()
        self.notifications.add_notification("Storage usage displayed.", "info")
        messagebox.showinfo("Storage Management", "Storage usage displayed in the logs.")

    def launch_browser(self):
        """
        Launches the web browser with the homepage set in settings.
        """
        homepage = self.browser_settings.get_settings()["homepage"]
        self.browser.search(homepage)
        self.notifications.add_notification(f"Browser launched with homepage: {homepage}", "info")
        messagebox.showinfo("Browser", f"Browser launched with homepage: {homepage}")

    def open_settings(self):
        """
        Opens the Settings window to configure APIs and preferences.
        """
        settings_window = tk.Toplevel(self.root)
        settings_window.title("C.A.S.S.I.E Settings")
        settings_window.geometry("500x400")
        settings_window.configure(bg="black")

        api_label = tk.Label(settings_window, text="OpenAI API Key:", font=("Arial", 14), fg="white", bg="black")
        api_label.pack(pady=10)

        api_entry = tk.Entry(settings_window, font=("Arial", 14), width=40)
        api_entry.insert(0, self.browser_settings.get_settings().get("openai_api_key", ""))
        api_entry.pack(pady=10)

        save_button = tk.Button(
            settings_window,
            text="Save",
            font=("Arial", 14),
            bg="gray",
            fg="white",
            command=lambda: self.save_settings(api_entry.get())
        )
        save_button.pack(pady=20)

    def save_settings(self, api_key):
        """
        Saves the OpenAI API key and updates settings.
        """
        self.browser_settings.update_setting("openai_api_key", api_key)
        self.notifications.add_notification("Settings updated successfully.", "info")
        messagebox.showinfo("Settings", "Settings updated successfully.")

    def process_command(self):
        """
        Process user input, either via text or voice.
        """
        if self.command_input.voice_mode:
            command = self.command_input.get_voice_command()
        else:
            command = self.command_input.get_text_command()

        if command.startswith("error:"):
            messagebox.showwarning("Command Error", command)
        else:
            self.command_processor.process_command(command)

    def launch(self):
        """
        Launch the main dashboard and begin standby monitoring.
        """
        self.standby_mode.start_monitoring(parent_gui=self.root)
        self.create_dashboard()
        self.root.mainloop()
