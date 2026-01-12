from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException

import allure
import pytest
import time

@allure.title("All Selenium Exception Handling")
@allure.description("Selenium Exception handling cases")

def test_selenium_exception():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com/#/login")
    print(driver.current_url)
    try:
        element = driver.find_element(By.ID, "this is value doesn't exist")
    except NoSuchElementException as nse:
        print(nse.msg)
    driver.quit()