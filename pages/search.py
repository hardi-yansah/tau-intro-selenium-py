"""
This module constains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:
    # URL
    URL = "https://www.duckduckgo.com"

    # Locators
    SEARCH_INPUT = (By.NAME, "q")

    def __init__(self, browser) -> None:
        self.browser = browser

    # Interaction methods
    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.ENTER)