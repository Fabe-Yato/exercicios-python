#6.	Efetuar a leitura de um valor positivo ou negativo e apresentar sempre como positivo. Por exemplo, se for menor do que 0, então multiplique por -1 (Uma das possíveis soluções).

num1 = int(input("Digite um número: "))

if num1 < 0:
  print("O valor é:", -num1)
else:
  print("O valor é:", num1)