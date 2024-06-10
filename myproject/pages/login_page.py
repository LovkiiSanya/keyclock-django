
from selenium.webdriver.common.by import By
from myproject.pages.base_page import BasePage


class LoginPage(BasePage):
    login_btn = "Login"
    username_input = "username"
    password_input = "password"
    sign_btn = '//input[@name="login"]'

    def click_login_button(self):
        login_button = self.find_element(By.LINK_TEXT, self.login_btn)
        login_button.click()

    def enter_username(self, username):
        username_input = self.find_element(By.NAME, self.username_input)
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.find_element(By.NAME, self.password_input)
        password_input.send_keys(password)

    def click_sign_in_button(self):
        sign_in_button = self.find_element(By.XPATH, self.sign_btn)
        sign_in_button.click()
