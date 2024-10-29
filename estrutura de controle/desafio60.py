"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
"""

#UTILIZANDO MÓDULO
from math import factorial

numero = int(input('Digite um número para calcular seu fatorial: '))
fatorial = factorial(numero)
print(f'O fatorial de {numero} é {fatorial}')

# MÉTODO TRADICIONAL

numero2 = int(input('Digite um número para calcular seu fatorial: '))
pointer = numero2
acumulador2 = 1

print(f'Calculando {numero2}! = ', end='')
while pointer > 0:
  print(f'{pointer}', end="")
  print(' x ' if pointer > 1 else ' = ', end="")
  acumulador2 *= pointer
  pointer -= 1
print(acumulador2)


# DESAFIO: FAZER TAMBÉM COM O LAÇO 'FOR'
numero3 = int(input('Digite um número para calcular seu fatorial: '))
acumulador3 = 1

for i in range(numero3, -1+1, -1):
  print(f'{i}', end='')
  print(' x ' if i > 1 else ' = ', end='')
  acumulador3 *= i
print(f'{acumulador3}')