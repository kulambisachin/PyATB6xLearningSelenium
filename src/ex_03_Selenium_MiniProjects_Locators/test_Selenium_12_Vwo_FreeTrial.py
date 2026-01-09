"""
Write a program to Free trial text in the URL on Free trial page
"""

import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@allure.title("Navigating to Free Trial page and searching for free trial text in the URL")
@allure.description("Verifying the free trial text in the URL on Free trial page")
def test_free_trial_page():
    chrome_options = Options()
    chrome_options.add_argument("--start_maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com/#/login")
    print(driver.current_url)

    # Navigating to Free trial page from vwo login page
    #free_trial = driver.find_element(By.XPATH, "//a[@data-qa='bericafeqo']")

    # Learning the concept of Link text and Partial link text:
    # free_trial = driver.find_element(By.LINK_TEXT, "Start a free trial")

    # Partial link text -> Matches contains text
    free_trial = driver.find_element(By.PARTIAL_LINK_TEXT, "Start")
    free_trial.click()
    print(driver.current_url)
    time.sleep(3)
    assert "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage" == driver.current_url

    driver.quit()


