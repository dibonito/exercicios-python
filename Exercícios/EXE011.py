"""#**Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.**"""

l = float(input('Digite a largura da parede '))
a = float(input('Digite a altura da parede '))
area = l*a
lt = area / 2
print('Sua parede tem a dimensão de {} largura x {} altura e sua área é de {:.2f}m²'.format(l,a,area))
print('Para pintar essa parede, você precisará de {:.2f} litros de tinta'.format(lt))