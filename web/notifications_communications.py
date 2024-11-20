import logging
import time

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

    def get_notifications(self, level=None):
        """
        Returns the list of notifications, optionally filtered by severity level.
        :param level: Severity level to filter by (info, warning, error).
        """
        if level:
            return [n for n in self.notifications if n["level"] == level]
        return self.notifications

    def clear_notifications(self):
        """
        Clears all notifications.
        """
        self.notifications = []
        logging.info("All notifications cleared.")

    def export_notifications(self, file_path="notifications_log.txt"):
        """
        Exports notifications to a text file.
        :param file_path: Path to the file to save notifications.
        """
        try:
            with open(file_path, "w") as file:
                for notification in self.notifications:
                    file.write(f"[{notification['timestamp']}] ({notification['level']}) {notification['message']}\n")
            logging.info(f"Notifications exported to {file_path}.")
        except Exception as e:
            logging.error(f"Error exporting notifications: {e}")
