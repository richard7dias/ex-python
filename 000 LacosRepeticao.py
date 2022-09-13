#Laços de repetição e listas
'''
Se eu quiser fazer uma repetição de informações ou impressões na tela, uso a ferramenta range
Ela é usada no modelo range(2,7) - sendo o 2 o início e o 7 o final (lembrando que o range não imprime o último número pedido)
'''
for palavra in range(1,4):
  print('Carregando...')


'''
Outra funcionalidade do range é colocar pulos. Ex.: range(1,6,2) - Aqui a lista será de 1 a 5 pulando 2
'''
for item in range(1,6,2):
  print(item)

'''
Outro exemplo é pedir para o usuário digitar um numero máximo e fazermos uma contagem de 1 ao numero pedido
'''
valor_inicial = 1
valor_maximo = int(input('Digite o valor desejado: '))
for numero in range(valor_inicial, valor_maximo + 1):
  print(numero)