"""
Objective:

URL: https://awesomeqa.com/practice.html
Automate the interaction with select box elements available on the practice page using Selenium WebDriver.

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time
import allure
import pytest


@allure.title("Select box element in URL: https://awesomeqa.com/practice.html")
@allure.description("Automate with select box elements available on the practice page using Selenium WebDriver")
def test_selenium_select_box():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://awesomeqa.com/practice.html")
    print(driver.current_url)

    # Selecting the select box element
    select_box_element = driver.find_element(By.XPATH, "//select[@id='continents']")
    WebDriverWait(driver=driver, timeout=3).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='continents']")))
    select = Select(select_box_element)
    select.select_by_visible_text("Africa")
    time.sleep(3)
    select.select_by_visible_text("Asia")
    driver.quit()
