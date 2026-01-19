from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import allure
import pytest


@allure.title("Checkbox with the last element")
@allure.description("Verifying the checkbox element clicked at last checkbox with -1 value")
def test_checkbox_last_element():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    print(driver.current_url)

    # Verifying the checkbox element clicked at last checkbox with -1 value

    checkbox_last_element = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    checkbox_last_element[-1].click()

    assert checkbox_last_element[-1].is_selected() is False, "Checkbox is unselected"

    print("Checkbox is un-selected", "\nValue of checkbox is :", checkbox_last_element[-1].is_selected())

    time.sleep(3)

    driver.quit()
