from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

"""
Tarefa: 
Entrar no site do IJJ, trocar idioma e verificar se o texto foi alterado
"""

navegador = Firefox()

navegador.get("https://jogajuntoinstituto.org")

change_lang = navegador.find_element(By.XPATH, "/html/body/div[1]/div[1]/button").click()

lang_options = navegador.find_elements(By.TAG_NAME, "li")

for lang_opt in lang_options:
    valor = lang_opt.get_attribute('data-value')
    if valor is not None:
        print(valor)
        if valor == "en":
            lang_opt.click()

banner_title = navegador.find_element(By.XPATH, "/html/body/div[1]/div[2]/section[1]/div/div/div[2]/h1")

print(banner_title.text)

assert "Step into the Field" in banner_title.text


