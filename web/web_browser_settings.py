class WebBrowserSettings:
    def __init__(self):
        self.settings = {
            "homepage": "https://www.google.com",
            "default_search_engine": "Google",
            "enable_notifications": False
        }

    def update_setting(self, key, value):
        """
        Updates a browser setting.
        :param key: The setting key (e.g., "homepage").
        :param value: The new value for the setting.
        """
        if key in self.settings:
            self.settings[key] = value
            logging.info(f"Browser setting updated: {key} = {value}")
        else:
            logging.warning(f"Invalid setting key: {key}")

    def get_settings(self):
        """
        Returns the current browser settings.
        """
        return self.settings
