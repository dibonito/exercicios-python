#**Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.**

nome = str(input('Digite seu nome: ')).strip()
c = 'SILVA' in nome.upper()
print('Seu nome tem Silva? {}'.format(c))