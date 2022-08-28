"""#**Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.**"""

carteira = float(input('Digite quanto dinheiro você tem na carteira: '))
dolar = 5.20
compra = carteira / dolar
print('Você tem na carteira R$ {}\n O valor do dólar hoje está R$ {}\n Você vai poder comprar US$ {:.2f} dólares'. format(carteira, dolar, compra))