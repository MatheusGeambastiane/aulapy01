email_check = False
dominio = "jogajuntoinstituto.org"

while email_check == False:
    email = input("Digite o seu email: ")

    if dominio in email:
        print("Este é um email joga junto")
        email_check = True
    else:
        print("Este não é um email do instituto")