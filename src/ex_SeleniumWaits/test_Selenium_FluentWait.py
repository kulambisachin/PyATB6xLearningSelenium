from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import allure
import time
import pytest

@allure.title("Fluent Waits")
@allure.description("Working of Fluent Waits")

def test_fluent_wait_explicit():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com/#/login")
    print(driver.current_url)

    # Adding the details for username and password field

    email_address = driver.find_element(By.ID, "login-username")
    email_address.send_keys("abc@gmail.com")

    password_field = driver.find_element(By.ID, "login-password")
    password_field.send_keys("password@123")

    sign_in_button = driver.find_element(By.XPATH, "//span[@data-qa='ezazsuguuy']")
    sign_in_button.click()

    # Fluent Explicit Wait Example
    WebDriverWait(driver=driver, poll_frequency=1, timeout=5).until(EC.visibility_of_element_located((By.ID,'js-notification-box-msg')))

    # Verifying the error message which is displayed
    error_message = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_message.text)

    assert "Your email, password, IP address or location did not match" == error_message.text

    driver.quit()