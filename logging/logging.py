import logging
import os

class LoggingModule:
    def __init__(self, log_file="logs/cassie.log"):
        self.log_file = log_file
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler(self.log_file),
                logging.StreamHandler()
            ]
        )

    def log_info(self, message):
        logging.info(message)

    def log_warning(self, message):
        logging.warning(message)

    def log_error(self, message):
        logging.error(message)

    def get_logs(self):
        """
        Returns the contents of the log file as a string.
        """
        try:
            with open(self.log_file, "r") as log_file:
                return log_file.read()
        except FileNotFoundError:
            return "No logs available."
