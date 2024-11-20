from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging

class WebBrowser:
    def __init__(self, driver_path=None):
        """
        Initialize the web browser.
        :param driver_path: Path to ChromeDriver executable. If None, assumes it's in PATH.
        """
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")

        try:
            if driver_path:
                self.driver = webdriver.Chrome(service=Service(driver_path), options=options)
            else:
                self.driver = webdriver.Chrome(options=options)
            logging.info("Browser initialized successfully.")
        except Exception as e:
            logging.error(f"Error initializing browser: {e}")
            self.driver = None

    def search(self, query):
        """
        Perform a Google search for the given query.
        :param query: The search query string.
        """
        if not self.driver:
            logging.warning("Browser is not initialized. Cannot perform search.")
            return
        try:
            self.driver.get("https://www.google.com")
            search_bar = self.driver.find_element("name", "q")
            search_bar.send_keys(query)
            search_bar.send_keys(Keys.RETURN)
            logging.info(f"Search performed for: {query}")
        except Exception as e:
            logging.error(f"Error performing search: {e}")

    def close_browser(self):
        """
        Close the browser window.
        """
        if self.driver:
            self.driver.quit()
            logging.info("Browser closed successfully.")
