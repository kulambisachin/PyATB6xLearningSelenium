"""

## **Project 1 (Negative Case) - Automating by using the Selenium Python. **

1. Navigate to the URL - [katalon-demo-cura.herokuapp.com](https://katalon-demo-cura.herokuapp.com/profile.php#login)
2. Find the **Make appointment** Button
3. Click on the **Make appointment **Button
4. Next Page will be loaded
5. **Find and Enter **the details **Username and Password** and **Click** on the Login Button, Wrong Creditnals
6. Verify the error message : Login failed! Please ensure the username and password are valid.

"""
import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



def test_selenium_newproject_negative_case():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print(driver.current_url)

    # Logic to find the Make a appointment and clicking it
    appointment_button = driver.find_element(By.ID, "btn-make-appointment")
    appointment_button.click()

    # Logic to add the values to Username and Password fields and then clicking on the Login Button
    username = driver.find_element(By.ID, "txt-username")
    username.send_keys("Sachin K M")
    password = driver.find_element(By.ID, "txt-password")
    password.send_keys("test12345")
    login_button = driver.find_element(By.ID, "btn-login")
    login_button.click()
    time.sleep(5)

    # Verifying the error message displayed for invalid login
    error_message = driver.find_element(By.CLASS_NAME, "text-danger")
    print(error_message.text)

    assert "Login failed! Please ensure the username and password are valid." == error_message.text
    time.sleep(2)
    driver.quit()
