from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# Page Object del carrito de SauceDemo.
class CartPage(BasePage):
    TITLE = (By.CSS_SELECTOR, ".title")
    CART_ITEM_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def is_loaded(self):
        self.wait_url_contains("cart.html")
        return self.get_title() == "Your Cart"

    def get_title(self):
        return self.get_text(self.TITLE)

    def get_item_names(self):
        return [item.text for item in self.find_all_visible(self.CART_ITEM_NAME)]

    def go_to_checkout(self):
        checkout_button = self.find_clickable(self.CHECKOUT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkout_button)
        self.driver.execute_script("arguments[0].click();", checkout_button)
        self.wait_url_contains("checkout-step-one.html")
