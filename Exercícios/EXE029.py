#**Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.**

vel = float(input('Qual a velocidade atual do carro? '))
multa = (vel-80)*7.00
if vel <= 80:
    print('Bom dia! Dirija com segurança...')
else:
    print('MULTADO! Você excedeu o limite permitido que é de 80 km/h')
    print('Você deve pagar uma multa de R$ {:.2f} '.format(multa))