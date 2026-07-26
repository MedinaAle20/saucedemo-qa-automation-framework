from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# Page Object del menu lateral de SauceDemo.
class MenuPage(BasePage):
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    ALL_ITEMS_LINK = (By.CSS_SELECTOR, "[data-test='inventory-sidebar-link']")
    ABOUT_LINK = (By.CSS_SELECTOR, "[data-test='about-sidebar-link']")
    LOGOUT_LINK = (By.CSS_SELECTOR, "[data-test='logout-sidebar-link']")
    RESET_LINK = (By.CSS_SELECTOR, "[data-test='reset-sidebar-link']")
    LOGIN_BUTTON = (By.ID, "login-button")

    def open(self):
        self.click(self.MENU_BUTTON)

    def get_visible_options(self):
        options = [
            self.ALL_ITEMS_LINK,
            self.ABOUT_LINK,
            self.LOGOUT_LINK,
            self.RESET_LINK,
        ]
        return [self.get_text(option) for option in options]

    def logout(self):
        logout_link = self.find_visible(self.LOGOUT_LINK)
        self.driver.execute_script("arguments[0].click();", logout_link)
        self.find_visible(self.LOGIN_BUTTON)
