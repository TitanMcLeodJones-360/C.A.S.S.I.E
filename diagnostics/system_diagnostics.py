import psutil
import logging

class SystemDiagnostics:
    def check_cpu_health(self):
        """
        Logs CPU usage and health.
        """
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            logging.info(f"CPU Usage: {cpu_usage}%")
            if cpu_usage > 85:
                logging.warning("High CPU usage detected! Consider closing unnecessary applications.")
        except Exception as e:
            logging.error(f"Error checking CPU health: {e}")

    def check_battery_health(self):
        """
        Logs battery health and status.
        """
        try:
            battery = psutil.sensors_battery()
            if battery:
                logging.info(f"Battery Level: {battery.percent}%")
                logging.info(f"Charging Status: {'Charging' if battery.power_plugged else 'Not Charging'}")
                if battery.percent < 20 and not battery.power_plugged:
                    logging.warning("Low battery! Consider plugging in the charger.")
            else:
                logging.info("Battery information not available.")
        except Exception as e:
            logging.error(f"Error checking battery health: {e}")

    def periodic_check(self):
        """
        Periodically runs system diagnostics.
        """
        self.check_cpu_health()
        self.check_battery_health()
        Timer(3600, self.periodic_check).start()  # Check every hour
