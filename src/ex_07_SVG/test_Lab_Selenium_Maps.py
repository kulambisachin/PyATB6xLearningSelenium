from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import allure
import pytest
import time


@allure.title("SVG Tripura State")
@allure.description("Finding the Tripura state from the list of states")
def test_selenium_svg_maps():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    print(driver.current_url)

    # Finding the list of states in the India map and print the output
    list_of_states = driver.find_elements(By.XPATH,
                                          "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")

    for state in list_of_states:
        print(state.get_attribute("aria-label"))

        # Finding the tripura state from the Map

        if "Tripura" in state.get_attribute("aria-label"):
            state.click()
            break

    time.sleep(5)

    driver.quit()
