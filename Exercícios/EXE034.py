#**Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.**

salario = float(input('Qual o salário do funcionário? '))

reajuste1 = salario + salario * 15 / 100
reajuste2 = salario + salario * 10 / 100

if salario <= 1250:
    print('Quem ganhava R$ {}, passa a ganhar R$ {:.2f} agora'.format(salario, reajuste1))

else:
    salario > 1250
    print('Quem ganhava R$ {}, passa a ganhar R$ {:.2f} agora'.format(salario, reajuste2))
