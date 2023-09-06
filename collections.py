# INDEX DAS COLLECTIONS:
#              0          1      2        3 
frutas = [ 'Maracuja',  'uva', 'uva', 'Morango']
#a LISTA É MUTÁVEL E ORDENADA
print(30*'-' + "Lista" + '-'*30)
# frutas.remove('Maracuja')# É possível remover qualquer item passando o nome
# frutas.clear() # limpa totalmente a lista
# frutas.pop() # remove o último item da lista
print(frutas)


#A TUPLA É IMUTÁVEL E ORDENADA
automoveis = ('Carro', 'moto', 'aviao')
print(30*'-' + "Tupla" + '-'*30)
print(automoveis[0])

#O DICIONÁRIO É MUTÁVEL E ORDENADO E ESTRUTURADO POR CHAVE:VALOR. OS VALORES NÃO PODERÃO SER REPETIDOS
pessoa = {
    "nome": "Matheus",
    "idade": 24,
    "Cidade": "Salvador"
}
print(30*'-' + "Dicionário" + '-'*30)
print(pessoa['Cidade'])# PARA ACESSARMOS O VALOR DE UM DICIONÁRIO, UTILIZAMOS A CHAVE DELE. 

# OS SETES SÃO DESORDENADOS, MUTÁVEIS E PODEM SER REPETIDOS.
cores = {'azul', 'amarelo', 'rosa'}
print(30*'-' + "sets" + '-'*30)
print(cores)
