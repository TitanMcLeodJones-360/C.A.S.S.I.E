import logging
import time
from threading import Thread

class StandbyMode:
    def __init__(self, inactivity_threshold=300):
        """
        Initializes the Standby Mode handler.
        :param inactivity_threshold: Time in seconds before entering standby.
        """
        self.inactivity_threshold = inactivity_threshold
        self.last_activity_time = time.time()
        self.standby_active = False

    def reset_activity_timer(self):
        """
        Resets the inactivity timer to the current time.
        """
        self.last_activity_time = time.time()
        if self.standby_active:
            self.exit_standby()

    def enter_standby(self):
        """
        Enters standby mode by reducing resource usage.
        """
        self.standby_active = True
        logging.info("C.A.S.S.I.E has entered Standby Mode.")
        # Add code to disable high-resource modules here
        # e.g., stop diagnostics, pause notifications, etc.

    def exit_standby(self):
        """
        Exits standby mode and resumes normal operation.
        """
        self.standby_active = False
        logging.info("C.A.S.S.I.E has exited Standby Mode.")
        # Add code to re-enable modules here
        # e.g., resume diagnostics, restart notifications, etc.

    def monitor_activity(self):
        """
        Monitors user activity and manages standby state.
        """
        while True:
            time_since_last_activity = time.time() - self.last_activity_time
            if time_since_last_activity > self.inactivity_threshold and not self.standby_active:
                self.enter_standby()
            time.sleep(5)  # Check activity every 5 seconds

    def start_monitoring(self):
        """
        Starts a background thread to monitor activity.
        """
        logging.info("Starting Standby Mode monitoring.")
        Thread(target=self.monitor_activity, daemon=True).start()
