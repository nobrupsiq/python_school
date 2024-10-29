"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
"""

#UTILIZANDO MÓDULO
# from math import factorial

# numero = int(input('Digite um número para calcular seu fatorial: '))
# fatorial = factorial(numero)
# print(f'O fatorial de {numero} é {fatorial}')

# MÉTODO TRADICIONAL

numero = int(input('Digite um número para calcular seu fatorial: '))
pointer = numero
acumulador = 1

print(f'Calculando {numero}! = ', end='')
while pointer > 0:
  print(f'{pointer}', end="")
  print(' x ' if pointer > 1 else ' = ', end="")
  acumulador *= pointer
  pointer -= 1
print(acumulador)