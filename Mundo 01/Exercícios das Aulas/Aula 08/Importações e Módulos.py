from math import sqrt, floor, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}.'.format(num, raiz))
print('A raiz de {} arredondada para baixo é igual a {}.'.format(num, floor(raiz)))
print('A raiz de {} arredondada para cima é igual a {}.'.format(num, ceil(raiz)))
