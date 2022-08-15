#5.	Efetuar a leitura de dois valores numéricos inteiros e apresentar o resultado da diferença entre o maior valor pelo menor valor

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

diferenca = num1 - num2
if diferenca < 0:
  print("A diferença é:", -diferenca)
else:
  print("A diferença é:", diferenca)