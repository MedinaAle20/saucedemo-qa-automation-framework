from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# Page Object del flujo de checkout de SauceDemo.
class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")
    SUMMARY_TOTAL = (By.CSS_SELECTOR, "[data-test='total-label']")

    def fill_information(self, first_name, last_name, postal_code):
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)

    def continue_checkout(self):
        continue_button = self.find_clickable(self.CONTINUE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", continue_button)
        self.driver.execute_script("arguments[0].click();", continue_button)
        self.wait_url_contains("checkout-step-two.html")

    def finish_checkout(self):
        finish_button = self.find_clickable(self.FINISH_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", finish_button)
        self.driver.execute_script("arguments[0].click();", finish_button)
        self.wait_url_contains("checkout-complete.html")

    def get_total_text(self):
        return self.get_text(self.SUMMARY_TOTAL)

    def get_complete_message(self):
        return self.get_text(self.COMPLETE_HEADER)
