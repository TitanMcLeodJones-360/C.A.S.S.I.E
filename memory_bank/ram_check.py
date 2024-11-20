import psutil
import logging

class RamCheck:
    def check_ram_usage(self):
        """
        Checks the total and used RAM of the system.
        """
        memory = psutil.virtual_memory()
        total_ram_mb = memory.total / (1024 * 1024)
        used_ram_mb = memory.used / (1024 * 1024)
        logging.info(f"Total RAM: {total_ram_mb:.2f} MB")
        logging.info(f"Used RAM: {used_ram_mb:.2f} MB")

    def periodic_check(self):
        """
        Periodically checks RAM usage and logs the information.
        """
        self.check_ram_usage()
        Timer(3600, self.periodic_check).start()  # Check every hour
