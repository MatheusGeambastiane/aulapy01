"""
com idade maior que 40 anos
com renda maior de 5 mil
com renda maior de 15 mi
"""

import pandas as pd

df = pd.read_csv('dados_ficticios.csv')

for i, linha in df.iterrows():
    print(linha['nome'], linha['renda'])

