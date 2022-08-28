"""#**Exercício Python 08: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.**"""

metros = int(input('Digite o valor em metros a serem convertidos: '))
centimetros = metros*100
milimetros = metros*1000
print('{} metros convertido em centímetros é {} centímetros e convertido em milímetros é {} milímetros .'.format(metros,centimetros,milimetros))