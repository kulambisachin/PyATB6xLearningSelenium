"""
Verify if the email and password is wrong for the given credentials

"""
import time
import allure
import pytest
from allure_pytest.utils import allure_title, allure_description

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@allure.title("Negative test case - App vwo.com login with Wrong Email and password and verify the wrong error message")
@allure.description("Verify the error message with credentials")
def test_vwo_login():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com/#/login")
    print(driver.current_url)

    # Find the element of the email address and password fields and clicking on SignIn button
    email_address = driver.find_element(By.XPATH, "//input[@id='login-username']")
    email_address.send_keys("test@example.com")
    password = driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys("Test12345")
    sign_in = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    sign_in.click()

    # Verifying the error message after submitting the invalid credentials
    error_message = driver.find_element(By.XPATH, "//div[@id='js-notification-box-msg']")
    print(error_message.text)
    time.sleep(5)
    assert "Your email, password, IP address or location did not match" == error_message.text
    time.sleep(5)

    driver.quit()
