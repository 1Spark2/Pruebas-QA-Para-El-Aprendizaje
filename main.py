import selenium

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Firefox()
driver.get('https://demoqa.com/')

driver.execute_script("window.scroll(0, 400)")

elem_form = driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)')
elem_form.click()

element_practice = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1)")
element_practice.click()

element_name =  driver.find_element(By.CSS_SELECTOR, "#firstName")
element_name.send_keys('Blacky')
time.sleep(10)

driver.quit()