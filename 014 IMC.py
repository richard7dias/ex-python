print('\n CALCULADORA DE IMC')
p = float(input('Qual o seu peso? '))
a = float(input('Qual a sua altura? '))
imc = p / (a * a)
print('Seu IMC é de {:.2f}.'.format(imc))