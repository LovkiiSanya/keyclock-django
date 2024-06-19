from selenium.webdriver.common.by import By
from myproject.pages.base_page import BasePage
from myproject.pages.home_page import HomePage


class RegistrationPage(BasePage):
    login_btn = "/html/body/header/nav/ul/li[1]/a"
    register_start_btn = "Register"
    username_input = '//input[@name="username"]'
    password_input = '//input[@name="password"]'
    password_confirm_input = '//input[@name="password-confirm"]'
    email_input = '//input[@name="email"]'
    first_name_input = '//input[@name="firstName"]'
    last_name_input = '//input[@name="lastName"]'
    register_btn = '//input[@value="Register"]'

    def click_login_button(self):
        login_button = self.find_element(By.XPATH, self.login_btn)
        login_button.click()

    def click_first_register_button(self):
        register_button = self.find_element(By.LINK_TEXT, self.register_start_btn)
        register_button.click()

    def enter_username(self, username):
        username_input = self.find_element(By.XPATH, self.username_input)
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.find_element(By.XPATH, self.password_input)
        password_input.send_keys(password)

    def confirm_password(self, password):
        confirm_input = self.find_element(By.XPATH, self.password_confirm_input)
        confirm_input.send_keys(password)

    def enter_email(self, email):
        email_input = self.find_element(By.XPATH, self.email_input)
        email_input.send_keys(email)

    def first_name(self, first):
        first_name = self.find_element(By.XPATH, self.first_name_input)
        first_name.send_keys(first)

    def last_name(self, last):
        last_name = self.find_element(By.XPATH, self.last_name_input)
        last_name.send_keys(last)

    def click_register_btn(self):
        register_btn = self.find_element(By.XPATH, self.register_btn)
        register_btn.click()
