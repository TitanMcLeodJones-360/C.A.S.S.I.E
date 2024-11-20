import logging
from loading.dashboard import Dashboard
from loading.load_config import LoadConfig
from utils.auth import Auth

def main():
    logging.info("Starting CASSIE...")

    # Initialize Loading and Configuration
    config_loader = LoadConfig()
    config_loader.load_system_info()  # Load system details and show typewriter effect

    # User Authentication
    auth = Auth()
    if not auth.authenticate_user():
        logging.critical("Authentication failed. Exiting...")
        return

    # Launch Dashboard
    dashboard = Dashboard()
    dashboard.launch()  # Start the GUI dashboard

if __name__ == "__main__":
    main()
