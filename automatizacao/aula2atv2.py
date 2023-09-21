from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep


#ABRIR NAVEGADOR
navegador = Firefox()

url = "https://www.jogajuntoinstituto.org/"

#ACESSAR SITE
navegador.get(url)

# IDENTIFICAR A BARRA DE PESQUISA
# barra_de_pesquisa = navegador.find_element(By.NAME, "q")
#REALIZAR A PESQUISA
# barra_de_pesquisa.click()
# barra_de_pesquisa.send_keys("Instituto Joga Junto")
# barra_de_pesquisa.send_keys(Keys.ENTER)


def verify_title(title):
    
    assert title in navegador.title
    print("Este é o titulo correto")
    return

def find_element_by_name(nome):
    return navegador.find_element(By.NAME, nome)


verify_title("Instituto Joga Junto")
form_name = find_element_by_name("nome")

form_name.send_keys("Matheus")

form_email = find_element_by_name("email").send_keys("mgeambastiane@gmail.com")
form_body = find_element_by_name("body").send_keys("Automação com Selenium Web Driver")
form_select = find_element_by_name("assunto")


select = Select(form_select)

select.select_by_visible_text("Contratar profissionais")

form_btn = navegador.find_element(By.XPATH, "/html/body/div[1]/div[2]/section[8]/div[1]/form/button")

print(form_btn)

form_btn.submit()


sleep(8)
navegador.quit()


# resultados.click()

