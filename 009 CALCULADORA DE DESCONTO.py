print('CALCULADORA DE DESCONTO')
p = float(input('Qual o preço atual do produto? '))
d = int(input('Quantos por cento de desconto? '))
r = p - (d * p) / 100
print('O produto com desconto vale R${:.2f}.'.format(r))