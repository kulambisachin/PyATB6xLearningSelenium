from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import allure
import pytest
import time


@allure.title("Static Select Dropdown")
@allure.description("Verifying the dropdown fields")
def test_selenium_svg_maps():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://the-internet.herokuapp.com/dropdown")
    print(driver.current_url)

    # Clicking on the Select dropdown
    select_dropdown = driver.find_element(By.XPATH, "//select[@id='dropdown']")
    select = Select(select_dropdown)

    select.select_by_visible_text("Option 2")

    time.sleep(2)

    driver.quit()