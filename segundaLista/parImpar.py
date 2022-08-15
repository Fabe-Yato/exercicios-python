# 3. Elabore um programa que as listas Pares e Impares recebam os valores pares e ímpares da lista Inteiros e os exibem como:


Inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pares = []
impares = []

for num in range(len(Inteiros)):
  if Inteiros[num] % 2 == 0:
    pares.append( Inteiros[num] )
  
  else:
    impares.append( Inteiros[num] )
    
print("Pares:", pares)
print("Impares", impares)