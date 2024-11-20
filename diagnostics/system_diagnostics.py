import psutil
import logging
from web.notifications_communications import Notifications

class SystemDiagnostics:
    def __init__(self):
        self.notifications = Notifications()

    def check_cpu_health(self):
        """
        Logs CPU usage and sends a warning if usage is high.
        """
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            logging.info(f"CPU Usage: {cpu_usage}%")
            if cpu_usage > 85:
                self.notifications.add_notification("High CPU usage detected!", "warning")
        except Exception as e:
            logging.error(f"Error checking CPU health: {e}")
            self.notifications.add_notification("Error checking CPU health.", "error")

    def check_battery_health(self):
        """
        Logs battery health and sends a warning if the battery is low.
        """
        try:
            battery = psutil.sensors_battery()
            if battery:
                logging.info(f"Battery Level: {battery.percent}%")
                if battery.percent < 20 and not battery.power_plugged:
                    self.notifications.add_notification("Low battery! Consider plugging in the charger.", "warning")
            else:
                logging.info("Battery information not available.")
        except Exception as e:
            logging.error(f"Error checking battery health: {e}")
            self.notifications.add_notification("Error checking battery health.", "error")
