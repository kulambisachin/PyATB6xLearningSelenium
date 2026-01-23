from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder

import time
import allure
import pytest


@allure.title("Click and hold")
@allure.description("Verifying the click and hold actions")
def test_click_and_hold():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    print(driver.current_url)

    # Click and hold will click and don't release it
    element_to_hold = driver.find_element(By.ID, "draggable")

    actions = ActionChains(driver=driver)
    actions.click_and_hold(on_element=element_to_hold).perform()

    time.sleep(2)
    driver.quit()
