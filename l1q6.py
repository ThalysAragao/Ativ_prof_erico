#importa o valor de pi e a função de potencia (pow) da biblioteca math
from math import pi, pow

#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
#área do circulo = 2 * pi * r * r
#Entrada
raio_do_circulo = float (input('Informe o tamanho do raio do circulo: '))

#processamento
area_do_circulo = 2 * pi * pow(raio_do_circulo,2)

#resposta
print('A área do circulo é {:.2f}'.format(area_do_circulo))