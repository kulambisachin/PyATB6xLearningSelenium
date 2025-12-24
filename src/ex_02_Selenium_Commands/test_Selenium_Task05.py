from selenium import webdriver
import allure
import pytest


@allure.title("verify that this text exists on the page")
@allure.description("Text to be verified CURA Healthcare Service")
def test_seleniumTask05():
    # Selenium 4
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print(driver.get)
    page_source = driver.page_source
    print(page_source)
    print(driver.current_url)
    print(driver.title)
    assert "CURA Healthcare Service" in page_source
    driver.quit()
