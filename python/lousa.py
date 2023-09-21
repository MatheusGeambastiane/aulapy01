from faker import Faker
import pandas as pd
import random

faker = Faker('pt_br')

def remover_apelido(nome):
    
    nome_fracionado = nome.split()
    apelidos = ['Sra.', 'Sr.', 'Srta.']
    for i in nome_fracionado:
        if i in apelidos:
            nome_fracionado.remove(i)
    novo_nome = ' '.join(nome_fracionado)    
    return novo_nome
    
def gerar_massa(quantidade):
    personas = []

    for i in range(quantidade):
        data = {
            "Nome": remover_apelido(faker.name()),
            "cidade": faker.city(),
            'bio': faker.text(),
            'idade': random.randint(18, 90) # Gerar números aleatorios com o random
        }
        personas.append(data)

    df = pd.DataFrame(personas)

    return df

resultado = gerar_massa(120)



# print(personas)

resultado.to_csv("segunda_massa.csv", index=False)



# print(df)

# df.to_csv("primeira_massa.csv")
