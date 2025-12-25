from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure
import pytest


def test_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=400,500")
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print(driver.title)
    driver.quit()
