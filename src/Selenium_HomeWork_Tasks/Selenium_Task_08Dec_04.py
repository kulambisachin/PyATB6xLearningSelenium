"""
Task 2: Click on a Specific State (Example: Maharashtra)

      URL :- https://www.amcharts.com/svg-maps/?map=india

Locate Maharashtra using SVG path
Click on Maharashtra
Validate:
Tooltip OR
State name is displayed OR
Any visual highlight happens
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import allure
import pytest


@allure.title("Finding the Maharashtra State from URL :- https://www.amcharts.com/svg-maps/?map=india")
@allure.description("Click on a Specific State (Example: Maharashtra) from the India Maps")
def test_svg_img():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    print(driver.current_url)

    # Clicking on 'I understand and agree' button
    understand_button = driver.find_element(By.XPATH, "//button[normalize-space()='I understand and agree']")
    understand_button.click()

    # Finding the list of states in the maps
    list_of_states = driver.find_elements(By.XPATH,
                                          "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")

    for state in list_of_states:
        print(state.get_attribute("aria-label"))

        if "Maharashtra" in state.get_attribute("aria-label"):
            state.click()
            break

    driver.quit()
