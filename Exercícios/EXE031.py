#**Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200 Km e R$ 0,45 parta viagens mais longas.**

km = float(input('Qual a distância da sua viagem? '))
res1 = km * 0.50
res2 = km * 0.45

if km <= 200:
    print('A passagem da sua viagem custará R$ {:.2f}'.format(res1))

else:
    print('A passagem da sua viagem custará R$ {:.2f}'.format(res2))
print('BOA VIAGEM! ')