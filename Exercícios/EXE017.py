"""#**Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.**"""

#EXEMPLO 1
cateto_oposto = float(input('Informe o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 +  cateto_adjacente ** 2) ** (1/2) # (cateto_oposto elevado a 2 + cateto_adjacente elevado a 2) elevado a (meio)
print('O valor da hipotenusa é: {:.2f}'.format(hipotenusa))

#EXEMPLO 2 - USANDO BIBLIOTECA MATH

import math

cateto_oposto = float(input('Informe o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print('O valor da hipotenusa é: {:.2f}'.format(hipotenusa))