from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException



#Esta funcion nos permite usar los datos como el elemento que estamos buscado dentro de ella y que realice las siguientes acciones
#Primero necesita el driver, la cantidad que quieres bajar si no encuentras y el identificador. (Se usa "*" para que
# podamos colocar mas parametros y que no se rompa el programa porque le sobran, uno de mas para ser exactos)
 


def find_and_scroll(driver, scroll_quantity, element_identificator, max_attempts=3):
        if WebDriverWait(driver, 10).until(EC.presence_of_element_located(element_identificator)):
            elemento_to_be_clickable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(element_identificator))
            if elemento_to_be_clickable is not None:
                elemento = driver.find_element(*element_identificator)
                return elemento
            else:
                driver.execute_script(f"window.scrollBy(0, {scroll_quantity})")
                return find_and_scroll(driver, scroll_quantity, element_identificator, max_attempts - 1)
        




# def find_and_scroll(driver, scroll_quantity, element_identificator, max_attempts=3):
#     for _ in range(max_attempts):
#         try:
#             WebDriverWait(driver, 10).until(EC.presence_of_element_located(element_identificator))
#             elemento_to_be_clickable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(element_identificator))
#             if elemento_to_be_clickable:
#                 return elemento_to_be_clickable
#             else:
#                 driver.execute_script(f"window.scrollBy(0, {scroll_quantity})")
#         except (NoSuchElementException, StaleElementReferenceException):
#             driver.execute_script(f"window.scrollBy(0, {scroll_quantity})")

#     return None



# def find_and_scroll(driver, scroll_quantity, element_identificator, max_attempts=3):
#     try:
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located(element_identificator))
#         elemento_to_be_clickable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(element_identificator))
#         if elemento_to_be_clickable is not None:
#             elemento = driver.find_element(*element_identificator)
#             return elemento
#         else:
#             driver.execute_script(f"window.scrollBy(0, {scroll_quantity}")
#             return find_and_scroll(driver, scroll_quantity, element_identificator, max_attempts - 1)
#     except (NoSuchElementException, StaleElementReferenceException):
#         if max_attempts > 0:
#             driver.execute_script(f"window.scrollBy(0, {scroll_quantity})")
#             # Llamada recursiva para volver a verificar después del desplazamiento
#             return find_and_scroll(driver, scroll_quantity, element_identificator, max_attempts - 1)
#     return None



# def find_and_scroll(driver, scroll_quantity, element_identificator):
#     try:
#         # Esperar a que el elemento esté presente y clickeable
#         elemento = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(element_identificator))
#         return elemento
#     except (NoSuchElementException, StaleElementReferenceException):
#         # Si no se encuentra el elemento, realiza un desplazamiento hacia abajo
#         driver.execute_script(f"window.scrollBy(0, {scroll_quantity})")
#         return None



# ESTE SI SIRVE
def find_and_scroll(driver, scroll_quantity, element_identificator):
    max_attemps=3

    while max_attemps > 0:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(element_identificator))
            # Esperar a que el elemento sea clickeable y visible
        elemento_to_be_clickable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(element_identificator))
        # driver.execute_script(f"window.scrollBy(0, {scroll_quantity})")
        if elemento_to_be_clickable is not None:
            elemento = driver.find_element(*element_identificator)
            return elemento # Si se encuentra el elemento y es clickeable, lo retorna
        elif elemento_to_be_clickable is None:
            driver.execute_script(f"window.scrollBy(0, {scroll_quantity})")
        elif elemento_to_be_clickable is not None:
            elemento = driver.find_element(*element_identificator)
            return elemento
        else:
            print("LAPUTAMADRENOFUNCIONA ESA VERGAAA")

 
    return elemento


#PD: solo sirve si directament el elemento no esta visible, en caso de que aparezca pero tenga algo como un anuncio delante, este dara error en la ejecucion del mismo