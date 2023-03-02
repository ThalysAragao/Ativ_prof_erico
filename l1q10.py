#Faça um programa que peça a temperatura em graus celsius, transforme e mostre em graus fahrenheit.
#°F = (9 * °C)/5 + 32
#entrada
temperatura_celsius = float (input ('temperatura em celsius: '))

#processamento
#°C = 5 ((°F-32) / 9)
temperatura_fahrenheit = 9 * (temperatura_celsius) / 5 + 32

#saída
print('A temperatura {:.1f}°C é igual a {:.1f}°F'. format(temperatura_celsius, temperatura_fahrenheit))