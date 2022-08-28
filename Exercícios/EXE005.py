"""#**Exercício Python 05: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.**"""

num = int(input('Digite um número inteiro: '))
sucessor = num + 1
antecessor = num - 1
print('O número é {} seu sucessor é {} e seu antecessor é {}'.format(num,sucessor,antecessor))