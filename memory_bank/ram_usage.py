import psutil
import logging

class RamUsage:
    def allocate_ram(self, min_ram_mb):
        """
        Ensures a minimum RAM allocation for the program by checking available memory.
        """
        available_ram_mb = psutil.virtual_memory().available / (1024 * 1024)
        if available_ram_mb < min_ram_mb:
            logging.warning(f"Low available RAM: {available_ram_mb:.2f} MB. Consider closing unused programs.")
        else:
            logging.info(f"RAM available: {available_ram_mb:.2f} MB. Allocation sufficient.")
