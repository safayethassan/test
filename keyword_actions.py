from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class KeywordActions:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Initialize your WebDriver

    def open_browser(self, url):
        self.driver.get(url)

    def click(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()

    def type(self, locator, value):
        element = self.driver.find_element(By.XPATH, locator)
        element.send_keys(value)

    def assert_text(self, locator, expected_text):
        element = self.driver.find_element(By.XPATH, locator)
        assert element.text == expected_text, f"Expected '{expected_text}' but got '{element.text}'"

    def close_browser(self):
        self.driver.quit()