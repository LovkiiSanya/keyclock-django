import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from myproject.pages.home_page import HomePage
from myproject.pages.registration_page import RegistrationPage


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver_path = '/home/sanya/django/keyclock/myproject/chromedriver/chromedriver-linux64/chromedriver'
        service = Service(driver_path)
        options = Options()
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.maximize_window()

    def test_login(self):
        self.driver.get('http://127.0.0.1:8000/')
        time.sleep(2)

        reg_page = RegistrationPage(self.driver)
        home_page = HomePage(self.driver)

        reg_page.click_login_button()
        time.sleep(2)

        reg_page.click_first_register_button()
        time.sleep(2)

        reg_page.enter_username("12345")
        reg_page.enter_password("12345")
        reg_page.confirm_password("12345")
        reg_page.enter_email("12345@gmail.com")
        reg_page.first_name("12345")
        reg_page.last_name("12345")

        reg_page.click_register_btn()
        time.sleep(2)

        home_page.click_save_button()
        time.sleep(2)

        self.assertTrue(home_page.is_alert_present(), "Window miss")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
