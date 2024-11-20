import json
import os

class UniversalCookieStorage:
    def __init__(self, cookie_file="cookies.json"):
        self.cookie_file = cookie_file
        if not os.path.exists(self.cookie_file):
            with open(self.cookie_file, "w") as f:
                json.dump({}, f)

    def save_cookies(self, cookies):
        """
        Save cookies to a JSON file.
        :param cookies: A dictionary of cookies.
        """
        with open(self.cookie_file, "w") as f:
            json.dump(cookies, f)
        logging.info("Cookies saved successfully.")

    def load_cookies(self):
        """
        Load cookies from a JSON file.
        :return: A dictionary of cookies.
        """
        with open(self.cookie_file, "r") as f:
            cookies = json.load(f)
        logging.info("Cookies loaded successfully.")
        return cookies
