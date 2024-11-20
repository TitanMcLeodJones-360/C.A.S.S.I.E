import subprocess
import logging
from web.notifications_communications import Notifications
import os

class HardwareDiagnostics:
    def __init__(self):
        self.notifications = Notifications()

    def scan_devices(self):
        """
        Scans for connected hardware devices and logs their information.
        """
        try:
            if os.name == "nt":
                result = subprocess.check_output("wmic path Win32_PnPEntity get Name", shell=True)
                devices = result.decode().splitlines()
                logging.info("Connected Devices:")
                for device in devices:
                    if device.strip():
                        logging.info(f" - {device.strip()}")
                        self.notifications.add_notification(f"Connected Device: {device.strip()}", "info")
            else:
                result = subprocess.check_output("lshw -short", shell=True)
                logging.info(result.decode())
                self.notifications.add_notification("Device scan completed successfully.", "info")
        except Exception as e:
            logging.error(f"Error scanning hardware devices: {e}")
            self.notifications.add_notification("Error scanning hardware devices.", "error")
