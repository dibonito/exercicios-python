"""#**Exercício Python 06: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.**"""

num = int(input('Digite um número inteiro: '))
dobro = num * 2
triplo = num * 3
raiz_quadrada = num ** (1/2)
print('O número digitado foi {} . O dobro dele é {} o triplo {} .'.format(num,dobro,triplo))
print('A raiz quadrada de {} é {} . '.format(num,raiz_quadrada))