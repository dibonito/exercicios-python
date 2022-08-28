"""#**Exercício Python 07: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.**"""

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
soma_nota = (nota1 + nota2 + nota3)
media = soma_nota /3
print('A média final do aluno é {:.1f}'.format(media))