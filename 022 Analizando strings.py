'''
len(nc) #contar caracteres
nc.count() #contar caracteres
nc.find() #encontrar palavra ou letra
nc.replace() #trocar palavra ou letra
nc.upper() #colocar em maísculas
nc.lower() #colocar em minúsculas
nc.capitalize() 
nc.title()
nc.strip() #cortar os espaços
nc.lstrip() #cortar os espaços à esquerda
nc.rstrip() #cortar os espaços à direita

'''

nc = input('Qual seu nome completo? ').strip()
print('Analizando seu nome...')
print('Seu nome em maúsculas é {}.'.format(nc.upper()))
print('Seu nome em minúsculas é {}.'.format(nc.lower()))
print('Seu nome tem {} caracteres.'.format(len(nc) - nc.count(' ')))
#print('Seu primeiro nome tem {} caracteres.'.format(nc.find(' ')))     ou
ns = nc.split()
print('Seu primeiro nome tem {} caracteres'. format(len(ns[0])))