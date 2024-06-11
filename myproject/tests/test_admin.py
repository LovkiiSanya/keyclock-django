import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from myproject.pages.home_page import HomePage
from myproject.pages.delete_page import DeletePage

page = ("http://0.0.0.0:8080/realms/master/protocol/openid-connect/auth?client_id=security-admin-console&redirect_uri"
        "=http%3A%2F%2F0.0.0.0%3A8080%2Fadmin%2Fmaster%2Fconsole%2F%23%2Fmy_blog%2Fusers&state=569e366a-baf1-4446"
        "-9344-be44afea984a&response_mode=fragment&response_type=code&scope=openid&nonce=7ded5fa7-47b7-445c-9069"
        "-ede4b2586502&code_challenge=NI5u-6lD4YfxmWkhyu0rAclDDaST5WljXU5KpLfsFHE&code_challenge_method=S256")


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver_path = '/home/sanya/django/keyclock/myproject/chromedriver/chromedriver-linux64/chromedriver'
        service = Service(driver_path)
        options = Options()
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.maximize_window()

    def test_login(self):
        self.driver.get(page)
        time.sleep(2)

        admin_page = DeletePage(self.driver)

        admin_page.enter_username("admin")
        admin_page.enter_password("admin")
        admin_page.click_sign_in_button()
        time.sleep(2)
        admin_page.click_users_btn()
        admin_page.select_user_by_email("12345@gmail.com")
        time.sleep(2)
        admin_page.click_delete_btn()
        time.sleep(1)
        admin_page.click_delete_confirm_btn()
        time.sleep(1)
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
