"""
Mini Project #2 (Selenium)

// Locators - Find the Web elements

// Open the URL: www.idrive360.com/enterprise/account?upgradenow=true

// Find the Email id** and enter the email as augtest_040823@idrive.com

// Find the Pass inputbox** and enter password as 123456.

// Find and Click on the Sigin button

// Verify that the message is shown "Your free trail has expired"

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
import allure
import pytest


def test_selenium_homework_task2():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.idrive360.com/enterprise/account?upgradenow=true")
    time.sleep(5)
    print(driver.current_url)

    # Find the element of the email address and password fields and clicking on SignIn button
    email_address = driver.find_element(By.ID, "username")
    email_address.send_keys("augtest_040823@idrive.com")
    password = driver.find_element(By.ID, "password")
    password.send_keys("123456")
    sign_in = driver.find_element(By.ID, "frm-btn")
    sign_in.click()
    time.sleep(20)

    # Verifying the Free trial expired message in the Upgrade Account Tab
    message_verify = driver.find_element(By.CLASS_NAME, "id-card-title")
    print(message_verify.text)
    assert "Your free trial has expired!" == message_verify.text
    time.sleep(2)

    # Verify the Free trial expired message in the Header section
    message_verify_header = driver.find_element(By.XPATH, "//span[text()='Your free trial has expired']")
    print(message_verify_header.text)
    assert "Your free trial has expired" == message_verify_header.text

    # Verifying the Upgrade Now button in header section
    upgrade_now_button = driver.find_element(By.CSS_SELECTOR, "button.id-btn.id-warning-btn-drk.id-tkn-btn")
    print(upgrade_now_button.text)
    assert "Upgrade Now!" == upgrade_now_button.text
    driver.quit()
