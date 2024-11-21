import logging

class CommandProcessor:
    def __init__(self, dashboard):
        """
        Initialize the CommandProcessor with a reference to the Dashboard.
        :param dashboard: An instance of the Dashboard to trigger actions.
        """
        self.dashboard = dashboard
        self.commands = {
            "open browser": self.dashboard.launch_browser,
            "run diagnostics": self.dashboard.run_diagnostics,
            "show storage": self.dashboard.show_storage_management,
            "show notifications": self.dashboard.show_notifications,
            "exit application": self.exit_application
        }

    def process_command(self, command):
        """
        Process a user command and execute the corresponding action.
        :param command: The input command string.
        """
        command = command.lower().strip()
        action = self.commands.get(command)

        if action:
            logging.info(f"Executing command: {command}")
            action()
        else:
            logging.warning(f"Unknown command: {command}")
            self.dashboard.notifications.add_notification(f"Unknown command: {command}", "warning")
            self.dashboard.show_message("Unknown Command", f"The command '{command}' is not recognized.")

    def exit_application(self):
        """
        Safely exits the application.
        """
        logging.info("Exiting application...")
        self.dashboard.root.destroy()
