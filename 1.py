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

driver.get("https://typekadeh.com")
time.sleep(2)

btn1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "header button.tk-btn")))
driver.execute_script("arguments[0].click();", btn1)
time.sleep(1.5)

btn2 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "iranYekan-14--bold")))
driver.execute_script("arguments[0].click();", btn2)
time.sleep(2)

inputs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card-dialog input, .card-dialog .tk-input__dense")))
