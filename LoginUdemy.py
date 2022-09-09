from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get('https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F')

btn_google=driver.find_element(By.CLASS_NAME, 'google-auth--social-btn--google--1H6_f')
time.sleep(30)
btn_google.click()
time.sleep(30)

driver.close()