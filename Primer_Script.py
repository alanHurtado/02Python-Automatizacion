from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get('http://licon-app.herokuapp.com/sign-up')

name = driver.find_element('name','name')
name.send_keys('Alan Astorga Hurtado')
time.sleep(20)

driver.close()
