#1.   	Dada uma lista de strings, retorna a contagem do número de strings onde o comprimento da string é 2. Nota: python não tem um operador ++, mas += funciona.

#Exemplo de teste e saída:
#lista_textos = [“abc”, “ab”, “ola”, “la”, “le”]
#saída: 3
#Explicação: Na lista, lista_textos possuímos ao todo 5 itens, porém somente 3 desses itens possuem 2 caracteres

listaTextos = ['abc', 'ab', 'ola', 'la', 'le']
duasLetras = 0
for letras in range(len(listaTextos)):
  if len(listaTextos[letras]) == 2:
    duasLetras += 1

print("A quantidade de vezes que aparecem duas letras é:", duasLetras)