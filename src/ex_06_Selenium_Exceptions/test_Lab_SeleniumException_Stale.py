from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import pytest
import allure


@allure.title("Stale Exception")
@allure.description("Stale Exception with driver.refresh() function")
def test_selenium_exception_stale():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.google.com/")
    print(driver.current_url)
    text_area_element = driver.find_element(By.XPATH, "//textarea[@name='q']")
    driver.refresh()  # Stale exception example

    # Catching the exception try and except block
    try:
        text_area_element.send_keys("Sachin K M")
    except StaleElementReferenceException as ser:
        print(ser.msg)

    driver.quit()
