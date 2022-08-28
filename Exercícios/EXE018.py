"""#**Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.**"""

import math

angulo = float(input('Informe o ângulo que você deseja: '))
seno = math.sin( math.radians(angulo))
cosseno = math.cos( math.radians(angulo))
tangente = math.tan( math.radians(angulo))
print('O ângulo de {} tem o seno de {:.2f} '.format(angulo,seno))
print('O ângulo de {} tem o coseno de {:.2f} '.format(angulo,cosseno))
print('O ângulo de {} tem o tangente de {:.2f} '.format(angulo,tangente))