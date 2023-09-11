palavra = input("Digite uma palavra")

vogais = ['a', 'e', 'i', 'o', 'u']

for letra in palavra:
    if letra in vogais:
        print(letra.upper())
        print(letra.lower())