#**Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.**



from random import randint
from time import sleep


print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('-=-'*20)
print('Pensando...')
sleep(3)
pc = randint(0, 5)
pen = int(input('Em que número pensei? '))
if pen == pc:
    print('Parabéns você acertou! ')
else:
    print('Que pena! Eu pensei no número {}.'.format(pc))