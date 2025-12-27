from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import allure
import pytest
import time

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