#**Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.**

n = str(input('Digite seu nome completo: ')).upper().strip()
nome = n.split()
print('{} é seu primeiro nome '.format(nome[0]))
print('{} é seu útimo sobrenome '.format(nome[len(nome)-1]))