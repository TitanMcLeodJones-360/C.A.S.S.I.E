import psutil
import logging
from web.notifications_communications import Notifications
from logging.error import ErrorHandler

class SystemDiagnostics:
    def __init__(self):
        self.notifications = Notifications()
        self.error_handler = ErrorHandler()

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
            self.error_handler.log_error("003")  # Diagnostics Module Error

    def check_battery_health(self):
        """
        Logs battery health and sends a warning if the battery is low.
        """
        try:
            battery = psutil.sensors_battery()
            if battery:
                battery_level = battery.percent
                charging_status = "Charging" if battery.power_plugged else "Not Charging"
                logging.info(f"Battery Level: {battery_level}% - {charging_status}")
                self.notifications.add_notification(f"Battery Level: {battery_level}% - {charging_status}", "info")

                if battery_level < 20 and not battery.power_plugged:
                    self.notifications.add_notification("Low battery! Consider plugging in the charger.", "warning")
            else:
                logging.info("Battery information not available.")
        except Exception as e:
            logging.error(f"Error checking battery health: {e}")
            self.error_handler.log_error("003")  # Diagnostics Module Error

    def check_storage_health(self):
        """
        Logs disk usage and sends a warning if storage is low.
        """
        try:
            disk_usage = psutil.disk_usage('/')
            total_space_gb = disk_usage.total / (1024**3)
            used_space_gb = disk_usage.used / (1024**3)
            free_space_gb = disk_usage.free / (1024**3)
            percent_used = disk_usage.percent

            logging.info(f"Disk Usage: {percent_used}% - Free: {free_space_gb:.2f} GB")
            self.notifications.add_notification(f"Disk Usage: {percent_used}% - Free: {free_space_gb:.2f} GB", "info")

            if percent_used > 90:
                self.notifications.add_notification("Low storage space! Consider freeing up space.", "warning")
        except Exception as e:
            logging.error(f"Error checking storage health: {e}")
            self.error_handler.log_error("003")  # Diagnostics Module Error

    def check_ram_health(self):
        """
        Logs RAM usage and sends a warning if RAM usage is high.
        """
        try:
            memory = psutil.virtual_memory()
            total_ram_gb = memory.total / (1024**3)
            used_ram_gb = memory.used / (1024**3)
            free_ram_gb = memory.available / (1024**3)
            percent_used = memory.percent

            logging.info(f"RAM Usage: {percent_used}% - Free: {free_ram_gb:.2f} GB")
            self.notifications.add_notification(f"RAM Usage: {percent_used}% - Free: {free_ram_gb:.2f} GB", "info")

            if percent_used > 85:
                self.notifications.add_notification("High RAM usage detected!", "warning")
        except Exception as e:
            logging.error(f"Error checking RAM health: {e}")
            self.error_handler.log_error("003")  # Diagnostics Module Error

    def run_full_diagnostics(self):
        """
        Runs all diagnostic checks and logs results.
        """
        logging.info("Running full system diagnostics...")
        self.notifications.add_notification("Running full system diagnostics...", "info")

        self.check_cpu_health()
        self.check_battery_health()
        self.check_storage_health()
        self.check_ram_health()

        logging.info("System diagnostics completed.")
        self.notifications.add_notification("System diagnostics completed.", "info")
