"""#**Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.**"""

# USANDO 'TRUNC'

from math import trunc

num = float(input('Digite um número real: '))
parte_inteira = trunc(num)
print('O número {}, tem a parte inteira {} '.format(num, parte_inteira))

# USANDO 'FLOOR'

from math import floor

num = float(input('Digite um número real: '))
parte_inteira = floor(num)
print('O número {}, tem a parte inteira {} '.format(num, parte_inteira))

# USANDO 'INT'

num = float(input('Digite um número real: '))
parte_inteira = int(num)
print('O número {}, tem a parte inteira {} '.format(num, parte_inteira))