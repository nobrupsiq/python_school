# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada #um dos dígitos separados.
# EX: Digite um numero: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

number = int(input('Digite um numero: '))
n = str(number)
print('Analisando o número {}'.format(number))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
