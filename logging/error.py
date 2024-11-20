import logging
from web.notifications_communications import Notifications

class ErrorHandler:
    def __init__(self):
        self.notifications = Notifications()
        self.error_table = {
            "001": "Unauthorized User",
            "002": "Storage Management Error",
            "003": "Diagnostics Module Error",
            "004": "Browser Error",
            "005": "Hardware Connection Failure"
        }

    def log_error(self, error_code):
        """
        Logs the error based on its code and sends a notification.
        :param error_code: The code of the error to log.
        """
        if error_code in self.error_table:
            error_message = self.error_table[error_code]
            logging.error(f"Error [{error_code}]: {error_message}")
            self.notifications.add_notification(f"Critical Error [{error_code}]: {error_message}", "error")
        else:
            logging.error(f"Unknown Error [{error_code}] occurred.")
            self.notifications.add_notification(f"Unknown Error [{error_code}] occurred.", "error")

    def handle_critical_error(self, error_code):
        """
        Handles critical errors by logging and alerting the user.
        :param error_code: The critical error code.
        """
        self.log_error(error_code)
        # Additional actions can be added here, such as shutting down the program.
