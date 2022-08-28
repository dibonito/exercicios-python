# **Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:**
# **– O nome com todas as letras maiúsculas e minúsculas.**
# **– Quantas letras ao todo (sem considerar espaços).**
# **– Quantas letras tem o primeiro nome.**

nome = str(input('Digite seu nome completo: ')).strip()
print('Nome em maiúsculo :',nome.upper())
print('Nome em minúsculo :',nome.lower())
print('O nome {} tem ao todo {} letras :'.format(nome,len(nome) - nome.count(' ')))
print('Seu primeiro nome {} tem {} letras '.format(nome[0:6],nome.find(' ')))