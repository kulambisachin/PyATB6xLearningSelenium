from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import allure
import pytest

@allure.title("Timeout Exception")
@allure.description("Checking the timeout exception")

def test_selenium_timeout_exception():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.google.com/")

    try:
        WebDriverWait(driver=driver, timeout=10).until(EC.element_to_be_clickable((By.ID, 'submit')))
    except TimeoutException as te:
        print(te.msg)
    finally:
        driver.quit()
