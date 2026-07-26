from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Acciones comunes para Page Objects, con esperas explicitas y fallbacks para UI dinamica.
class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_url(self, url):
        self.driver.get(url)

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all_visible(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def wait_url_contains(self, text):
        return self.wait.until(EC.url_contains(text))

    def click(self, locator):
        element = self.find_clickable(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except (ElementClickInterceptedException, ElementNotInteractableException):
            self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text):
        element = self.find_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()
        element.clear()
        element.send_keys(text)

        if element.get_attribute("value") != text:
            self.driver.execute_script(
                """
                const element = arguments[0];
                const value = arguments[1];
                const setter = Object.getOwnPropertyDescriptor(
                    window.HTMLInputElement.prototype,
                    'value'
                ).set;
                setter.call(element, value);
                element.dispatchEvent(new Event('input', { bubbles: true }));
                """,
                element,
                text,
            )

        self.wait.until(lambda driver: element.get_attribute("value") == text)

    def get_text(self, locator):
        return self.find_visible(locator).text

    def is_visible(self, locator):
        return self.find_visible(locator).is_displayed()
