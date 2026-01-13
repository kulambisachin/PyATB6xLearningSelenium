import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import allure
import pytest

@allure.title("SVG Image")
@allure.description("Verifying the SVG with Mac Mini search in the flipkart website")

def test_selenium_timeout_exception():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.flipkart.com/")

    # Search field and entering the value by clicking on 'Search' icon
    search_field = driver.find_element(By.NAME, 'q')
    search_field.send_keys("macmini")

    # find_elements are used because there are multiple svg images in the page.
    list_svg_element = driver.find_elements(By.XPATH, "//*[name()='svg']")
    list_svg_element[0].click()


    driver.quit()


