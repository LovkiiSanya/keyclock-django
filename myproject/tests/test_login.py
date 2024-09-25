import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from myproject.pages.home_page import HomePage
from myproject.pages.login_page import LoginPage

#LOX
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver_path = '/Users/evlezkov/PycharmProjects/keyclock-djangoclone/myproject/grivepaht/chromedriver'
        service = Service(driver_path)
        options = Options()
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.maximize_window()

    def test_login(self):
        self.driver.get('https://web.telegram.org/')
        time.sleep(2)

        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)

        login_page.click_login_button()
        time.sleep(2)

        login_page.enter_username("Test")
        time.sleep(1)

        login_page.enter_password("test1")
        time.sleep(1)

        login_page.click_sign_in_button()
        time.sleep(1)

        home_page.click_save_button()
        time.sleep(2)

        self.assertTrue(home_page.is_alert_present(), "Window miss")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
