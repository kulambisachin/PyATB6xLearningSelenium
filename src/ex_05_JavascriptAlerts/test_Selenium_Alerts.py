from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import allure
import pytest


@allure.title("Javascript Alerts")
@allure.description("Working all types of Javascript Alerts")
def test_selenium_alerts():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    print(driver.current_url)
    javascript_button = driver.find_element(By.XPATH, "//button[contains(text(),'Alert')]")
    javascript_button.click()

    # javascript alert accept case:
    alert = driver.switch_to.alert

    # Explicit Wait example
    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())
    alert.accept()

    assert_message = driver.find_element(By.XPATH, "//p[@id='result']")
    print(assert_message.text)

    assert "You successfully clicked an alert" == assert_message.text


def test_javascript_confirm_alerts():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    print(driver.current_url)
    javascript_confirm_button = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    javascript_confirm_button.click()
    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())
    # javascript confirm alert accept case:
    js_alert2 = driver.switch_to.alert
    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())
    js_alert2.accept()

    assert_js_message_alert2 = driver.find_element(By.XPATH, "//p[@style='color:green']")
    print(assert_js_message_alert2.text)

    assert "You clicked: Ok" == assert_js_message_alert2.text


def test_javascript_prompt_alerts():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    print(driver.current_url)

    # javascript prompt alert input the value:
    javascript_prompt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    javascript_prompt.click()
    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())

    js_prompt_alert3 = driver.switch_to.alert
    js_prompt_alert3.send_keys("Sachin K M")
    js_prompt_alert3.accept()

    assert_js_prompt_message_alert3 = driver.find_element(By.ID, "result")
    print(assert_js_prompt_message_alert3.text)

    assert "You entered: Sachin K M" == assert_js_prompt_message_alert3.text
    driver.quit()
