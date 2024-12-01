'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla

Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla
'''

import random

storage = ()
menor_valor = 0
maior_valor = 0

for i in range(1, 6):
  numero_aleatorio = random.randint(1, 50)
  storage += (numero_aleatorio,)
  if i == 1:
    menor_valor = storage[0]
    maior_valor = storage[0]
  for index, numero in enumerate(storage):
    if numero < menor_valor:
      menor_valor = numero
    if numero > maior_valor:
      maior_valor = numero

print(storage)
print(menor_valor, maior_valor)