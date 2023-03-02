#faça um programa que peça a temperatura em graus fahrenheit, transforme e mostre a temperatura em graus celsuis.
#°C = 5 ((°F-32) / 9).
#Entrada
temperatura_fahrenheit = float (input ('temperatura em fahrenheit: '))

#processamento
#°F = (9 * °C)/5 + 32
temperatura_celcius = 5 * (temperatura_fahrenheit - 32) / 9

#saída
print('A temperatura {:.1f}°F é igual a {:.1f}°C'.format(temperatura_fahrenheit, temperatura_celcius))