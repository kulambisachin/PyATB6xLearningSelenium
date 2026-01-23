from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time
import allure
import pytest


@allure.title("Click and Hold")
@allure.description("Verifying the click and hold")
def test_actions_click_and_hold():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    print(driver.current_url)

    # Find the click for results link

    click_results_page = driver.find_element(By.ID, 'click')
    click_results_page.click()

    # Mouse Back event from action builder

    action_builder = ActionBuilder(driver=driver)
    action_builder.pointer_action.pointer_up(MouseButton.BACK)
    action_builder.perform()

    time.sleep(5)
    driver.quit()