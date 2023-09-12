import requests


squad ={
    "matheus": "40140620",
    "michelle": "40155250"
}

response = requests.get(f'https://viacep.com.br/ws/40140620/json/')
data = response.json()
bairro = data['bairro']
print(data)
# for nome, cep in squad.items():
#     print(f' {nome} Mora em {bairro}')