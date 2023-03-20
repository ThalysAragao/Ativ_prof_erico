#tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:(72.7*altura)-58.
#Para homens: (72.7*h) - 58
#entrada

h = float(input('Altura:'))
peso = float(input('Peso:'))

peso_ideal = (72.7*h) - 58

if peso < peso_ideal:
	print('Abaixo do peso ideal!')
elif peso == peso_ideal:
	print('Dentro do peso ideal!')
else:
	print('Acima do peso ideal!')
print ('Peso: %.2f / Peso ideal: %.2f' %(peso, peso_ideal))