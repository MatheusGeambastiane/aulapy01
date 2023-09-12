import requests

squad = {
    "matheus": "40140260",
    "michelle": "40155250",
    "viviane": "40155810"
}

for nome, cep in squad.items():
    # print(f'{nome} e {cep}')

    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

    data = response.json()
    cidade = data['localidade']
    print(f'{nome} mora em {cidade}')