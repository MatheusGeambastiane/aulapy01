from atv1 import escolha_de_time

matriculas = []

while len(matriculas) < 5:
    matricula = int(input("Digite o numero da sua matrícula"))
    matriculas.append(matricula)

   


print(matriculas)

for matricula in matriculas:
    time = (escolha_de_time(matricula))
    print(time)