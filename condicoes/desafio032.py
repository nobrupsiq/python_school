# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

ano = int(input('Digite o ano: EX: 1995 -> '))

if ano % 4 == 0:
    print('{} é um ano Bissexto!'.format(ano))
else:
    print('{} não é ano Bissexto!'.format(ano))
