#10. Elaborar um programa de tabuada de um número inteiro. A tabulação deve ser da maneira tradicional. Por exemplo: 1 x 0 = 0; 1 x 1 = 1; ...; 1 x 10 = 10. Obs: O valor deverá ser informado pelo usuário.

tabuada = int(input("Digite um número para a tabuada: "))
i = 1
while(i <= 10):
  print(str(tabuada), " X ", str(i), " = ", tabuada * i)
  i += 1
