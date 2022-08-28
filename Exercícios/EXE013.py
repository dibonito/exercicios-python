"""#**Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.**"""

salario = float(input('Digite seu salário atual: '))

aumento = salario * 15 / 100
total = salario + aumento
print('O salário atual é R$ {} . Com o aumento de 15 % ficará R$ {:.2f}. '.format(salario, total))