"""#**Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.**"""

km = float(input('informe o km percorrido: '))
dia = int(input('Informe quantos dias foram utilizados: '))
valor_km = km*0.15
diaria = dia*60
total = valor_km + diaria
print('A distância percorrida foi: {:.0f} Km  e o valor total do Km foi R$ {:.0f}\nForam utilizados: {} dias  e o valor total dos dias utilizados foram R$ {:.0f} '.format(km, valor_km, dia, total))