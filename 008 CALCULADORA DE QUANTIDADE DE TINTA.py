print('CALCULADORA DE QUANTIDADE DE TINTA')
al = float(input('Qual a altura (em metros)? '))
l = float(input('Qual a largura (em metros)? '))
ql = (al * l) / 2
print('A quantidade de tinta para pintar esta parede é de {:.2f}l.'.format(ql))