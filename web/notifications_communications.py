import logging
import time
from threading import Timer

class Notifications:
    def __init__(self):
        self.notifications = []

    def add_notification(self, message, level="info"):
        """
        Adds a new notification to the system.
        :param message: The notification message.
        :param level: The severity level (info, warning, error).
        """
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.notifications.append({"timestamp": timestamp, "message": message, "level": level})

        # Log the notification
        if level == "info":
            logging.info(f"Notification: {message}")
        elif level == "warning":
            logging.warning(f"Notification: {message}")
        elif level == "error":
            logging.error(f"Notification: {message}")

    def get_notifications(self):
        """
        Returns the list of notifications.
        """
        return self.notifications

    def periodic_check(self):
        """
        Sends periodic health-check notifications (e.g., storage, RAM usage).
        """
        self.add_notification("Periodic system health check completed.", "info")
        Timer(3600, self.periodic_check).start()  # Run every hour
