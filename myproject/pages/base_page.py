
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))
