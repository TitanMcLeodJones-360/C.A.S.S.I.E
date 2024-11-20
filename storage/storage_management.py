import os
import shutil
import logging
import time
from threading import Timer

class StorageManagement:
    def __init__(self, perm_path="storage/perm", ce_path="storage/ce", temp_path="storage/temp"):
        self.perm_path = perm_path
        self.ce_path = ce_path
        self.temp_path = temp_path

        # Ensure directories exist
        os.makedirs(self.perm_path, exist_ok=True)
        os.makedirs(self.ce_path, exist_ok=True)
        os.makedirs(self.temp_path, exist_ok=True)

    def organize_files_by_size(self, source_folder):
        """
        Organizes files into perm, ce, and temp folders based on size thresholds.
        """
        try:
            for filename in os.listdir(source_folder):
                filepath = os.path.join(source_folder, filename)

                if os.path.isfile(filepath):
                    file_size_mb = os.path.getsize(filepath) / (1024 * 1024)  # File size in MB

                    if file_size_mb < 200:
                        target_folder = self.temp_path
                    elif 200 <= file_size_mb < 1000:
                        target_folder = self.ce_path
                    else:
                        target_folder = self.perm_path

                    shutil.move(filepath, os.path.join(target_folder, filename))
                    logging.info(f"Moved {filename} to {target_folder}")
        except Exception as e:
            logging.error(f"Error organizing files: {e}")

    def display_storage_usage(self):
        """
        Displays storage usage for perm, ce, and temp folders.
        """
        for folder, name in [(self.perm_path, "Permanent Storage"),
                             (self.ce_path, "Current Activities Storage"),
                             (self.temp_path, "Temporary Storage")]:
            total_size = sum(os.path.getsize(os.path.join(folder, f)) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)))
            logging.info(f"{name} Usage: {total_size / (1024 * 1024):.2f} MB")

    def periodic_check(self):
        """
        Periodically checks storage usage and logs recommendations.
        """
        self.display_storage_usage()
        Timer(21600, self.periodic_check).start()  # Check every 6 hours
