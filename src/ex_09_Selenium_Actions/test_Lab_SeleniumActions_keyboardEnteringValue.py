from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time
import allure
import pytest


@allure.title("Keyboard events")
@allure.description("Actions chains and keyboard events")
def test_actions_keyboard_events():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://awesomeqa.com/practice.html")
    print(driver.current_url)

    # Shift key down and release the key
    first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
    actions = ActionChains(driver=driver)

    # Entering the value with capital letters
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name, "Sachin").key_up(Keys.SHIFT).perform()

    # Entering the value with normal letters with send_keys_to_element
    # actions.send_keys_to_element(first_name, "Sachin").perform()

    time.sleep(3)
    driver.quit()
