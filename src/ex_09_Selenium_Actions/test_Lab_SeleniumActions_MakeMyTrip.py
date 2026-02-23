from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import allure
import pytest
import time


@allure.title("Make My Trip")
@allure.description("Verifying the Make my trip")
def test_make_my_trip():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.makemytrip.com/")
    print(driver.current_url)

    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@data-cy='closeModal']")))

    # Clicking on the close button on login pop-up
    close_button = driver.find_element(By.XPATH, "//span[@data-cy='closeModal']")
    close_button.click()

    # Clicking on From City

    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.ID, "fromCity")))

    actions = ActionChains(driver=driver)
    (actions
     .move_to_element(driver.find_element(By.ID, "fromCity"))
     .click().send_keys_to_element(driver.find_element(By.XPATH, "//input[@data-cy='fromCity']"), "DEL")
     .key_down(Keys.ARROW_DOWN)
     .key_down(Keys.ENTER)
     .perform()
     )
    time.sleep(3)

    # Clicking on To City
    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.ID, "toCity")))
    actions = ActionChains(driver=driver)
    (actions
     .move_to_element(driver.find_element(By.ID, "toCity"))
     .click().send_keys_to_element(driver.find_element(By.XPATH, "//input[@data-cy='toCity']"), "BLR")
     .key_down(Keys.ARROW_DOWN)
     .key_down(Keys.ENTER)
     .perform()
     )
    time.sleep(3)

    # Clicking outside From and To City
    regulardates = driver.find_element(By.XPATH, "//img[@alt='minimize']")
    regulardates.click()
    time.sleep(2)

    #outtoandfromcity = driver.find_element(By.XPATH, "//body[class='desktop in']")
    #uttoandfromcity.click()

    time.sleep(3)

