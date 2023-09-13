"""
Nome, idade e cidade. Sendo 3 pessoas moradoras de Recife, 2 de Salvador, 1 de são paulo e 1 de Manaus

Depois, filtre os dados para exibir na tela apenas os moradores do Recife. 
"""

import pandas as pd

data = {
    "Nome": ["Ester", "Uelton", "Katie", "Luana", "Giovanna", "Lean", "Sara"],
    "Idade": [23,25,32,62,52,55,35],
    "Cidade": ["Recife","Recife","Recife", "Salvador", "Salvador", "Sao Paulo", "Manaus"],
}

df = pd.DataFrame(data)

# print(df)
print(df[df['Cidade'] == "Recife"])

df.to_excel("minhaprimeiratabelaexcel.xlsx") # Para salvar como excel


df2 = pd.read_csv('minhaprimeiratabela.csv') # Para ler o csv
print('---- tabela nova -----')
print(df2)