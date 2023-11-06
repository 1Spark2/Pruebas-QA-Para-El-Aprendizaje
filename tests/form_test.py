import selenium 
import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from element_scroll import find_and_scroll




#Crear el driver para poder darle uso a el navegador y realizar acciones en el mismo.
driver = webdriver.Firefox()
wait = WebDriverWait(driver, timeout=10)
#Se hace uso del .get para poder pasarle una URL y que sea enviado a la misma
driver.get('https://demoqa.com/')


#realizamos acciones necesarias para el uso correcto, por ejemplo en la resolucion que estoy usando no me permite ver en primera instancia
#el elemento de Formulario que quiero hacerle click por lo que bajo el navegador para que aparezca y poder usarlo 
driver.execute_script("window.scroll(0, 400)")

#Una vez el elemento sea visible y puedas encontrarle su selector, sea css, xpath o id puedes hacer uso del mismo colocando ese elemento en una variable
elem_form = driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)')

#Luego de ello podemos realizar acciones sobre ese elemento como:
elem_form.click()

#Asi mismo con los demas elementos que quieras usar:
element_practice_form = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1)")
element_practice_form.click()

#Tambien podemos hacer uso de los elementos directamente sin necesidad de guardarlos en una variable, esto es util para cuando tenemos
#elementos que seran usados una sola vez por script, es decir que no se repite su uso, en caso contrario, si usamos muchas veces un mismo elemento
#si seria escencial usarlo en una variable para que tenga buena reutilizacion.
driver.find_element(By.CSS_SELECTOR, "#firstName").send_keys('Blacky')
driver.find_element(By.CSS_SELECTOR, "#lastName").send_keys('Perez')
driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys('Blackyperez@gmail.com')
driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-3']").click()
driver.find_element(By.CSS_SELECTOR, "#userNumber").send_keys("1234567")

driver.execute_script("window.scroll(0, 400)") 

#Bloque para la Fecha
element_bod = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dateOfBirthInput")))
element_bod.click()
element_month_select = driver.find_element(By.CSS_SELECTOR, ".react-datepicker__month-select")
element_month_select.click()
driver.find_element(By.CSS_SELECTOR, "option[value='9']").click() #OJO Este elemento si no esta visible en el UI, es decir que no esta ni siquiera abierto la busqueda del elemento no podra ser utilizado. Una opcion en este caso es hacer un assert de el paso anterior requerido para que este sea visible.
driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']").click()
driver.find_element(By.CSS_SELECTOR, "option[value='2015']").click()
driver.find_element(By.XPATH, "//div[@aria-label='Choose Wednesday, October 21st, 2015']").click()


element_subject = driver.find_element(By.CSS_SELECTOR, "#subjectsInput")
element_subject.click()
element_subject.send_keys("E") #Este se puede hacer modular para poder actualizar la variable
element_subject.send_keys(Keys.ARROW_DOWN) # Y este tambien para cambiar la posicion segun se requiera (Hacer esas dos cosas)
element_subject.send_keys(Keys.ENTER)

driver.execute_script("window.scroll(0, 400)") 

element_h_clickeable = driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
wait.until(lambda d : element_h_clickeable.is_enabled())
element_h_clickeable.click()


upload_photo = driver.find_element(By.CSS_SELECTOR, "#uploadPicture")


driver.quit()