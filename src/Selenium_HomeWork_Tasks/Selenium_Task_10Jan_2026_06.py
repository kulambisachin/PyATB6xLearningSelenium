from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import allure
import time
import pytest


@allure.title("Make my trip practice program")
@allure.description("Searching the flights from New Del to Chandigarh")
def test_makemytrip():
    # chrome_options = Options()
    # chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--incognito")
    # driver = webdriver.Chrome(chrome_options)
    firefox_options = Options()
    firefox_options.add_argument("--start-maximized")
    firefox_options.add_argument("--incognito")
    driver = webdriver.Firefox(firefox_options)
    driver.get("https://www.makemytrip.com/")
    print(driver.current_url)

    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@data-cy='closeModal']")))

    time.sleep(3)

    # Clicking on the close button on login pop-up
    close_button = driver.find_element(By.XPATH, "//span[@data-cy='closeModal']")
    close_button.click()

    # Clicking on the From City
    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.ID, "fromCity")))

    actions = ActionChains(driver=driver)
    (actions.move_to_element(driver.find_element(By.ID, "fromCity"))
     .click().send_keys_to_element(driver.find_element(By.XPATH, "//input[@data-cy='fromCity']"), "DEL")
     .key_down(Keys.ARROW_DOWN)
     .key_down(Keys.ENTER)
     .perform()
     )

    # Clicking on To City
    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.ID, "toCity")))
    actions = ActionChains(driver=driver)
    (actions
     .move_to_element(driver.find_element(By.ID, "toCity"))
     .click().send_keys_to_element(driver.find_element(By.XPATH, "//input[@data-cy='toCity']"), "IXC")
     .key_down(Keys.ARROW_DOWN)
     .key_down(Keys.ENTER)
     .perform()
     )

    driver.quit()
