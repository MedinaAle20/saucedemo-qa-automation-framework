from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


# Page Object del catalogo de productos de SauceDemo.
class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, ".title")
    PRODUCT_ITEM = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    def is_loaded(self):
        return "inventory.html" in self.driver.current_url and self.get_title() == "Products"

    def get_title(self):
        return self.get_text(self.TITLE)

    def get_product_names(self):
        return [product.text for product in self.find_all_visible(self.PRODUCT_NAME)]

    def get_product_prices(self):
        return [price.text for price in self.find_all_visible(self.PRODUCT_PRICE)]

    def get_product_count(self):
        return len(self.find_all_visible(self.PRODUCT_ITEM))

    def add_product_by_name(self, product_name):
        if product_name not in self.get_product_names():
            raise AssertionError(f"No se encontro el producto: {product_name}")

        slug = self._product_slug(product_name)
        button = self.find_clickable((By.CSS_SELECTOR, f"[data-test='add-to-cart-{slug}']"))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        self.driver.execute_script("arguments[0].click();", button)
        self.find_visible((By.CSS_SELECTOR, f"[data-test='remove-{slug}']"))

    def add_products_by_name(self, product_names):
        for index, product_name in enumerate(product_names, start=1):
            self.add_product_by_name(product_name)
            self.wait_until_cart_badge_count(index)

    def get_cart_badge_count(self):
        return int(self.get_text(self.CART_BADGE))

    def wait_until_cart_badge_count(self, expected_count):
        self.wait.until(EC.text_to_be_present_in_element(self.CART_BADGE, str(expected_count)))

    def _product_slug(self, product_name):
        return product_name.lower().replace(" ", "-")

    def go_to_cart(self):
        cart_link = self.find_clickable(self.CART_LINK)
        self.driver.execute_script("arguments[0].click();", cart_link)
        self.wait_url_contains("cart.html")
