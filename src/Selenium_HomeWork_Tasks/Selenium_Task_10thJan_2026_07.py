from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import allure
import pytest
import time


@allure.title("Open the Spicejet website and search delhi to chandigarh flights")
@allure.description("Searching flight from Del to IXC")
def test_spicejet():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.spicejet.com/")
    print(driver.current_url)

    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//div[normalize-space()='Flights']")))

    # Clicking on the From Flights
    actions = ActionChains(driver=driver)
    (actions.send_keys_to_element(driver.find_element(By.XPATH, "//div[normalize-space()='Flights']//following::input[@type='text'][1]"), "DEL")
     .key_down(Keys.ARROW_DOWN)
     .key_down(Keys.ENTER)
     .perform()
     )

    # Clicking on the To flights

    actions = ActionChains(driver=driver)
    (actions.send_keys_to_element(driver.find_element(By.XPATH, "//div[normalize-space()='Flights']//following::input[@type='text'][2]"), "IXC")
     .key_down(Keys.ARROW_DOWN)
     .key_down(Keys.ENTER)
     .perform()
     )

    time.sleep(3)