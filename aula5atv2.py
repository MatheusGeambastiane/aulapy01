valor_da_compra = float(input("Digite o valor da compra: "))


if valor_da_compra >= 250 and valor_da_compra < 500:
    print("PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00")

elif valor_da_compra >= 500:
    print("PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%")

else:
    print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")