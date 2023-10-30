from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


#Esta funcion nos permite usar los datos como el elemento que estamos buscado dentro de ella y que realice las siguientes acciones
#Primero necesita el driver, la cantidad que quieres bajar si no encuentras y el identificador. (Se usa "*" para que
# podamos colocar mas parametros y que no se rompa el programa porque le sobran, uno de mas para ser exactos)
 

def find_and_scroll(driver, scroll_quantity, *element_identificator):
    max_attempts = 3  # Número máximo de intentos
    attempts = 0

    while attempts < max_attempts:
        try:
            elemento = driver.find_element(*element_identificator)
            # if elemento is not None:
            #     print("ESTOY VIVO")
            # else:
            #     print("muertotoy")
            return elemento  # Si se encuentra el elemento, lo retorna
        except NoSuchElementException:
            # Si no se encuentra el elemento, realiza un desplazamiento hacia abajo
            driver.execute_script(f"window.scrollBy(0, {scroll_quantity})")
            attempts += 1

    return None 


#PD: solo sirve si directament el elemento no esta visible, en caso de que aparezca pero tenga algo como un anuncio delante, este dara error en la ejecucion del mismo