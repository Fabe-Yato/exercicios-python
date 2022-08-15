#Formule um programa que dada uma lista de strings, retorna a contagem do número de strings onde o comprimento da string é de 2 ou mais e o primeiro e os últimos caracteres da string são os mesmos.

listaTextos = ['aba', 'ab', 'ola', 'la', 'le','e']
letrasIguais = 0
for letras in range(len(listaTextos)):
  if len(listaTextos[letras]) >= 2:
    
    if listaTextos[letras][0] == listaTextos[letras][-1]:
        letrasIguais += 1
print("A quantidade de vezes que aparecem duas letras é:", letrasIguais)