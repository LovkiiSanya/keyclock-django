from selenium.webdriver.common.by import By
from myproject.pages.base_page import BasePage


class DeletePage(BasePage):
    username_input = "username"
    password_input = "password"
    sign_btn = '//input[@name="login"]'
    users_btn = '//a[@id="nav-item-users"]'
    table_xpath = '//*[@id="pf-tab-section-/my_blog/users/list-list"]/table'
    email = "12345@gmail.com"
    delete_btn = '//button[@data-testid="delete-user-btn"]'
    delete_confirm_btn = '//button[@data-testid="confirm"]'

    def enter_username(self, username):
        username_input = self.find_element(By.NAME, self.username_input)
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.find_element(By.NAME, self.password_input)
        password_input.send_keys(password)

    def click_sign_in_button(self):
        sign_in_button = self.find_element(By.XPATH, self.sign_btn)
        sign_in_button.click()

    def click_users_btn(self):
        users_btn = self.find_element(By.XPATH, self.users_btn)
        users_btn.click()

    def select_user_by_email(self, email):
        table = self.find_element(By.XPATH, self.table_xpath)

        rows = table.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            for cell in cells:
                if cell.text == email:
                    checkbox = row.find_element(By.XPATH, './td[1]/label/input')
                    checkbox.click()
                    return

    def click_delete_btn(self):
        delete_btn = self.find_element(By.XPATH, self.delete_btn)
        delete_btn.click()

    def click_delete_confirm_btn(self):
        delete_confirm_btn = self.find_element(By.XPATH, self.delete_confirm_btn)
        delete_confirm_btn.click()
