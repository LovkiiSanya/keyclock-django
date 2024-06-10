from selenium.webdriver.common.by import By
from myproject.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    save_btn = "save-btn"
    alert_group = (By.CSS_SELECTOR, 'ul.pf-c-alert-group.pf-m-toast[data-testid="alerts"]')

    def click_save_button(self):
        save_button = self.find_element(By.ID, self.save_btn)
        save_button.click()

    def is_alert_present(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.alert_group)
        )
