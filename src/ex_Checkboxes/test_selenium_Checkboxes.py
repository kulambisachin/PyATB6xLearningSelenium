from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time
import allure
import pytest


@allure.title("Checkboxes Program")
@allure.description("Verifying the checkboxes")
def test_selenium_checkboxes():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    print(driver.current_url)

    checkbox = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    checkbox[0].click()

    # Validation of checkboxes selected or not?

    assert checkbox[0].is_selected() is True, "Checkbox is selected"
    assert checkbox[1].is_selected() is True, "Checkbox is already is selected"

    print("checkbox 1 selected:", checkbox[0].is_selected())
    print("checkbox 2 already is selected", checkbox[1].is_selected())

    driver.quit()
