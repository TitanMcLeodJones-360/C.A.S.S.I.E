from utils.typewriter import typewriter_effect
import platform
import psutil
import socket

class LoadConfig:
    def load_system_info(self):
        """
        Loads and displays system information with a typewriter effect.
        """
        typewriter_effect("Loading system configuration...\n")

        # System Information
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        os_name = platform.system()
        os_version = platform.version()
        ram = psutil.virtual_memory().total // (1024**3)
        cpu_count = psutil.cpu_count()

        typewriter_effect(f"IP Address: {ip_address}")
        typewriter_effect(f"OS: {os_name} {os_version}")
        typewriter_effect(f"RAM: {ram} GB")
        typewriter_effect(f"CPU Cores: {cpu_count}")
        typewriter_effect("All systems operational.\n")
