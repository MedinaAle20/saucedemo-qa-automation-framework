import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.menu_page import MenuPage


# Pruebas UI end-to-end de SauceDemo sobre login, catalogo, carrito, checkout y logout.
def iniciar_sesion(driver, test_data):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(
        test_data["valid_user"]["username"],
        test_data["valid_user"]["password"],
    )
    return InventoryPage(driver)


def test_login_exitoso(driver, test_data):
    inventory_page = iniciar_sesion(driver, test_data)

    assert inventory_page.is_loaded()


@pytest.mark.parametrize("invalid_user_index", [0, 1])
def test_login_invalido(driver, test_data, invalid_user_index):
    user = test_data["invalid_users"][invalid_user_index]
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(user["username"], user["password"])

    assert "Epic sadface" in login_page.get_error_message()


def test_catalogo_productos(driver, test_data):
    inventory_page = iniciar_sesion(driver, test_data)

    assert inventory_page.get_title() == "Products"
    assert inventory_page.get_product_count() == 6
    assert inventory_page.get_product_names() == test_data["expected_products"]
    assert all(price.startswith("$") for price in inventory_page.get_product_prices())


def test_agregar_productos_al_carrito(driver, test_data):
    inventory_page = iniciar_sesion(driver, test_data)
    selected_products = test_data["expected_products"][:3]

    inventory_page.add_products_by_name(selected_products)
    assert inventory_page.get_cart_badge_count() == len(selected_products)

    inventory_page.go_to_cart()
    cart_page = CartPage(driver)

    assert cart_page.is_loaded()
    assert cart_page.get_item_names() == selected_products


def test_checkout_completo(driver, test_data):
    inventory_page = iniciar_sesion(driver, test_data)
    selected_products = test_data["expected_products"][:2]
    checkout_data = test_data["checkout"]

    inventory_page.add_products_by_name(selected_products)
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_information(
        checkout_data["first_name"],
        checkout_data["last_name"],
        checkout_data["postal_code"],
    )
    checkout_page.continue_checkout()

    assert checkout_page.get_total_text().startswith("Total: $")

    checkout_page.finish_checkout()
    assert checkout_page.get_complete_message() == "Thank you for your order!"


def test_menu_lateral_y_logout(driver, test_data):
    inventory_page = iniciar_sesion(driver, test_data)
    assert inventory_page.is_loaded()

    menu_page = MenuPage(driver)
    menu_page.open()

    assert menu_page.get_visible_options() == [
        "All Items",
        "About",
        "Logout",
        "Reset App State",
    ]

    menu_page.logout()
    assert "saucedemo.com" in driver.current_url
    assert LoginPage(driver).is_visible(LoginPage.LOGIN_BUTTON)
