#8.	Efetuar a leitura da idade de uma pessoa como um inteiro positivo, caso for maior que 18 anos exibir uma mensagem de texto dizendo que a pessoa pode entrar, senão se for menor ou igual a 18 exibir uma mensagem dizendo que a pessoa não pode entrar e se a idade for maior ou igual a 80 anos exibir uma mensagem dizendo que a pessoa não pode entrar. O programa deverá possuir as seguintes restrições: para que a idade seja válida o valor informado deverá estar entre 0 e 120 anos, fora desse intervalo o programa deverá retornar com uma mensagem dizendo que é uma idade inválida.

idade = int(input("Digite a sua idade: "))
if(idade < 0 or idade > 120):
  print("Essa idade é inválida")
elif(idade >= 80):
  print("Você pode entrar com restrições")
elif(idade < 18):
  print("Você não pode entrar")
elif(idade >= 18):
  print("Pode entrar")
