numero = int(input("Digite um número: "))

print('-'*30)
print(f'TABUADA DE {numero}')
print('-'*30)
for i in range(1, 11): 
    valor = i * numero
    print(f'{i} X {numero} : {valor}')