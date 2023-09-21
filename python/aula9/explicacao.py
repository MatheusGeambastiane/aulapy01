import pandas as pd # O as é usado para atribuir um apelido a bilioteca

data = {
    'Nome': ['João', "Marta", "Ary", "Matheus", "Michelle"],
    'Idade': [51, 37, 23,24, 33],
} # Gere o conjunto de dados como dicionário

df = pd.DataFrame(data) # USe o método DataFrame para gerar o df, e passe como argumento o data que você criou

print(df) # Para imprimir a tabela
print(df['Idade']) # Pra imprimir um coluna 
print(df[df['Idade'] == 23]) #Pra fazer alguma filtragem ou inteligência

