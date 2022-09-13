#Coleções (listas)
'''
O segredo de juntar em uma lista é usar o colchetes []
'''
precos = [14, 20, 33]
print(precos[2])
'''
Pra achar algo dentro da lista, por exemplo, quero saber qual é a ordem da lista do número 20, eu uso o código index, como abaixo
'''
print(precos.index (20))

'''
Se eu quiser usar a lista e imprimir um abaixo do outro, segue o exemplo abixo:
'''
for preco in precos:
  print(preco)

'''
Para fazer a soma de todos os numeros dentro de uma lista precisa se usar o for ... in ...
'''
idades = [15, 46, 75, 34, 23]
total = 0
for idade in idades:
  total = total + idade
print(total)