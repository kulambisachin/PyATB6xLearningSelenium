"""
## **Project 1 - Automating by using the Selenium Python. **

1. Navigate to the URL - [katalon-demo-cura.herokuapp.com](https://katalon-demo-cura.herokuapp.com/profile.php#login)
2. Find the **Make appointment** Button
3. Click on the **Make appointment **Button
4. Next Page will be loaded
5. **Find and Enter **the details **Username and Password** and **Click** on the Login Button
6. Verify current URL - [katalon-demo-cura.herokuapp.com/#appointment](https://katalon-demo-cura.herokuapp.com/#appointment)
"""
import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_selenium_project_1():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print(driver.current_url)

    # Logic to find the Make a appointment and clicking it
    appointment_button = driver.find_element(By.ID, "btn-make-appointment")
    appointment_button.click()
    time.sleep(5)

    # Logic to add the values to Username and Password fields and then clicking on the Login Button

    username = driver.find_element(By.ID, "txt-username")
    username.send_keys("John Doe")
    password = driver.find_element(By.ID, "txt-password")
    password.send_keys("ThisIsNotAPassword")
    login_button = driver.find_element(By.ID, "btn-login")
    login_button.click()
    time.sleep(5)

    # Logic to Verify current URL after clicking on Login button

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    print(driver.current_url)
    driver.quit()
