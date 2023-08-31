'''
Leiam o caso abaixo e executem usando Python.

A loja "ROUPAS SA" tem 2000 clientes e quer enviar mensagens nominais a cada um. A mensagem seria a seguinte:

Olá, PAULA MARTINS. Em JANEIRO você realizou uma compra no valor de R$500,00 e ganhou um desconto de 10% em sua próxima compra. Use o cupom PAULAÉ10.


'''
nome = input('Digite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
mes = 'JANEIRO'
n1 = int(input('Digite o sua 1 nota: '))
n2 = int(input('Digite o sua 2 nota: '))
# desconto = int('10')
# cupom = nome + "É" + desconto
# tipo_nome = type(desconto)
# print(tipo_nome)
soma = n1 + n2 

print(f" O nome é: {nome} {sobrenome} a primeira nota é {n1} e a segunda é {n2} a minha nota geral é {soma}")


# print('meu nome é {a}, meu sobrenome é {b}'.format(a=nome,b=sobrenome) )
# print(f'meu nome é {nome}, meu sobrenome é {sobrenome}' )



# print("Olá," + nome + sobrenome + ". Em " + mes + " você realizou uma compra no valor de R$" + valor + " e ganhou um desconto de " + desconto +  "% em sua próxima compra. Use o cupom " + nome + "É" + desconto + " .")


