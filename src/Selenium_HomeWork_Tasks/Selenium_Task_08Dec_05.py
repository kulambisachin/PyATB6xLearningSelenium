"""
Task 3:
Action to Perform

Try to locate a state that does NOT exist

Example:

"Atlantis"
"ABCState"
Code will trigger NoSuchElementException
Goal :- Your goal is to handle that exception.

"""

import allure
import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


@allure.title(" No Such Element Exception [https://www.amcharts.com/svg-maps/?map=india]")
@allure.description("Try to locate a state that does NOT exist with NoSuchElementException")
def test_selenium_nosuchexception():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    print(driver.current_url)

    # handling the no such element exception
    try:
        list_of_states = driver.find_element(By.ID, "Atlantis")
        list_of_states.click()
    except NoSuchElementException as nse:
        print(nse.msg)

    driver.quit()
