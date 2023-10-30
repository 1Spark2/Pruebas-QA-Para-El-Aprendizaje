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
driver.execute_script("window.scroll(0, 200)")
driver.find_element(By.CSS_SELECTOR, "#dateOfBirthInput").click()
element_bod = driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']")
#assert dob is not None, "El elemento no esta en la pagina"
assert element_bod is not None, "El elemento no se encontró en la página"
driver.find_element(By.CSS_SELECTOR, "option[value='10']").click() #OJO Este elemento si no esta visible en el UI, es decir que no esta ni siquiera abierto la busqueda del elemento no podra ser utilizado. Una opcion en este caso es hacer un assert de el paso anterior requerido para que este sea visible.
time.sleep(5)


year_selected = driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']")
year_selected.click() # HASTA AQUI OKEY
time.sleep(10)
#QUEDA PENDIENTE TENER QUE HACER QUE SE PUEDA SELECCIONAR UNA FECHA YO SE QUE LO VI PERO NO RECUERDO COMOXDDDDDDD
ActionChains(driver).send_keys(Keys.ARROW_UP).perform()
time.sleep(5)
# Hacer clic en la opción de año deseada
driver.quit()