from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Construccion centralizada del navegador usado por las pruebas UI.
def get_driver(headless=False):
    local_chrome = Path("C:/Program Files/Google/Chrome/Application/chrome.exe")
    options = Options()
    if local_chrome.exists():
        options.binary_location = str(local_chrome)

    options.add_argument("--window-size=1366,768")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    if headless:
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver
