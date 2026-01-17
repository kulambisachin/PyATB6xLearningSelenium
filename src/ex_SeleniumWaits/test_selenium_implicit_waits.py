import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@allure.title("Implicit Wait")
@allure.description("Working of Implicit Wait")
def test_selenium_implicit_wait():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com/#/login")
    print(driver.current_url)

    # ImplicitWait usage
    driver.implicitly_wait(5)

    # email_address ID is not present, so the implicit wait If element appears in:
    #
    # 1 sec → proceeds immediately
    #
    # 6 sec → fails after 5 sec

    email_address = driver.find_element(By.ID, "login-username1")
    email_address.send_keys("abc@example.com")

    password_field = driver.find_element(By.ID, "login-password")
    password_field.send_keys("password")

    driver.quit()
