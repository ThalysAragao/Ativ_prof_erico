#Faça um programa que peça quatro notas bimestrais e mostre a média
#Somar as 4 notas dividir por 4
#entrada das notad
nota_1 = float (input ('Digite sua primeira nota: '))
nota_2 = float (input ('Digite sua segunda nota: '))
nota_3 = float (input ('Digite sua terceira nota: '))
nota_4 = float (input ('Digite sua quarta nota: '))

#cálculo da média
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

#exibir o resultado
print('A média das {} {} {} {} notas é {:.2f}'.format(nota_1, nota_2, nota_3, nota_4, media))