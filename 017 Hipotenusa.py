# Hipotenusa
'''
#Jeito 1:
co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa é {:.2f}.'.format(hi))
'''
#Jeito 2:
import math
co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))
hi = math.hypot(co, ca)
print('A hipotenusa é {:.2f}'.format(hi))
