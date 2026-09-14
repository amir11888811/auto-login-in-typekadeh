import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def slow_type(element, text, delay=0.1):
    element.clear()
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)
wait = WebDriverWait(driver, 10)