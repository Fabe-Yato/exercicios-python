#1. Efetuar o cálculo e apresentar o valor de uma prestação em atraso, utilizando a seguinte fórmula:

#Prestação = valor + (valor * (taxa / 100) * tempo_em_dias)


valor = float(input("Digite o valor: "))
dias = 30
taxa = 10
prestacao = valor + (valor * (taxa/100) * dias)

print("O valor da prestação em atraso é: R$", round(prestacao, 2))