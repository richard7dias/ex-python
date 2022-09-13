print('CALCULADORA DE AUMENTO SALARIAL')
s = float(input('Qual o seu salário? '))
a = int(input('Quanto receberá de aumento? '))
r = s + (a * s) / 100
print('O seu novo salário com o aumento de {}% é de R${:.2f}'.format(a, r))
