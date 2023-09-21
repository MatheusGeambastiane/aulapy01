from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
# from time import sleep
from time import sleep

navegador = Firefox()


navegador.get("https://page-test-selenium.s3.sa-east-1.amazonaws.com/index.html")
# url= ""


adicionar = navegador.find_element(By.TAG_NAME, "a")

contador = 0
while contador <= 10:
    adicionar.click()
    contador += 1


# navegador.get(url)

# adicionar = navegador.find_element(By.TAG_NAME, "a")
# contador = 0
# while contador <= 10: 
#     adicionar.click()
#     contador += 1 

# input = navegador.find_elements(By.TAG_NAME, "input")
# for check in input:
#     check.click()

checkbox = navegador.find_elements(By.TAG_NAME, "input")

for check in checkbox:

    check.click()


sleep(5)
# navegador.quit()