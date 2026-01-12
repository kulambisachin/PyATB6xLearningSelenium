from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import allure
import pytest


@allure.title("Selenium Popup")
@allure.description("Verifying the the selenium pop in the make my trip website")
def test_selenium_popup():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.makemytrip.com/")
    print(driver.current_url)

    # Two square bracket is used in the visibility of element located parameter is a tuple
    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@data-cy='closeModal']")))
    close_button = driver.find_element(By.XPATH, "//span[@data-cy='closeModal']")
    close_button.click()

    driver.quit()
