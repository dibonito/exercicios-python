"""#**Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.**"""

from random import choice

aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Nome do terceiro aluno: '))
aluno4 = str(input('Nome do quarto aluno: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
print('Alunos:',alunos)
aluno_escolhido = choice(alunos)
print('O aluno escolhido foi {}'.format(aluno_escolhido))