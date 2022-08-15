#9. Fazer a leitura de dois valores e realizar a soma entre eles. Caso o valor ultrapasse 50, o programa deverá retornar como verdadeiro (True) caso contrário como falso (False)

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

soma = num1 + num2
if(soma > 50):
  print(True)
else:
  print(False)