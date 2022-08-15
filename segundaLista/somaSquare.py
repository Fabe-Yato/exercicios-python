#4. Faça um programa que leia uma lista A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos da lista.


numeros = [1,2,3,4]
soma = 0
for posicao in range(len(numeros)):
  soma += numeros[posicao] * numeros[posicao]
print("A soma do quadrado dos números na lista é:", soma)