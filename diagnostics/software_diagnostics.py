import logging
import subprocess
from web.notifications_communications import Notifications
import os

class SoftwareDiagnostics:
    def __init__(self):
        self.notifications = Notifications()

    def scan_for_malware(self):
        """
        Scans running processes for potential malware signatures.
        """
        try:
            processes = subprocess.check_output("tasklist" if os.name == "nt" else "ps -aux", shell=True)
            suspicious_signatures = ["malware", "virus", "trojan"]
            detected_issues = []

            for line in processes.decode().splitlines():
                for signature in suspicious_signatures:
                    if signature in line.lower():
                        detected_issues.append(line)
                        logging.warning(f"Potential malware detected: {line}")
                        self.notifications.add_notification(f"Potential malware detected: {line}", "warning")

            if not detected_issues:
                self.notifications.add_notification("No suspicious processes detected.", "info")
        except Exception as e:
            logging.error(f"Error during malware scan: {e}")
            self.notifications.add_notification("Error during malware scan.", "error")

    def check_unresponsive_apps(self):
        """
        Checks for unresponsive applications on the system.
        """
        try:
            if os.name == "nt":
                result = subprocess.run(["tasklist", "/fi", "STATUS eq NOT RESPONDING"], capture_output=True, text=True)
                if "No tasks are running" in result.stdout:
                    self.notifications.add_notification("No unresponsive applications detected.", "info")
                else:
                    self.notifications.add_notification("Unresponsive applications detected.", "warning")
            else:
                self.notifications.add_notification("Unresponsive app check not implemented for this OS.", "info")
        except Exception as e:
            logging.error(f"Error checking unresponsive applications: {e}")
            self.notifications.add_notification("Error checking unresponsive applications.", "error")
