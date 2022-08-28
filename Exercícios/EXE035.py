#**Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.**

print('-=-'*15)
print('Analisador de triângulos ')
print('-=-'*15)

p1 = float(input('Primeiro segmento: '))
p2 = float(input('Segindo segmento: '))
p3 = float(input('Terceiro segmento: '))

if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    print('Os segmentos acima podem formar um triângulo! ')
else:
    print('Os segmentos acima não podem formar um triângulo! ')
