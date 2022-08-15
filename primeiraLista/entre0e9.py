#7.	Efetuar a leitura de um valor entre 0 a 9, caso o programa receba um valor fora desse intervalo deverá apresentar uma mensagem com a seguinte resposta: O valor informado não é válido;
escolhaNum = int(input("Digite um número de 0 a 9: "))
if escolhaNum < 0 or escolhaNum > 9:
  print("O valor informado não é válido")
else:
  print("O número digitado foi", escolhaNum)