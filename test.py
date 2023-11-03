import selenium 
import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from element_scroll import find_and_scroll



#Crear el driver para poder darle uso a el navegador y realizar acciones en el mismo.
driver = webdriver.Firefox()

#Se hace uso del .get para poder pasarle una URL y que sea enviado a la misma
driver.get('https://demoqa.com/')
elemento = find_and_scroll(driver, 200, (By.CSS_SELECTOR, "body > div:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"))
elemento.click()

element_practice_form = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1)")
element_practice_form.click()


driver.find_element(By.CSS_SELECTOR, "#firstName").send_keys('Blacky')
driver.find_element(By.CSS_SELECTOR, "#lastName").send_keys('Perez')
driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys('Blackyperez@gmail.com')
driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-3']").click()
driver.find_element(By.CSS_SELECTOR, "#userNumber").send_keys("1234567")
driver.quit()