"""#**Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.**"""

prod = str(input('Digite um produto: '))
preco = float(input('Digite o valor atual do produto '))
desconto = preco*5/100
total = preco - desconto
print('O produto {} que custava R$ {} está na promoção com 5% de desconto e custará R$ {} '.format(prod, preco, total))