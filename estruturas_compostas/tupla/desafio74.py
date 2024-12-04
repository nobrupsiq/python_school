'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla

Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla
'''

 # MEU CODIGO
from random import randint

# storage = ()
# menor_valor = 0
# maior_valor = 0

# for i in range(1, 6):
#   numero_aleatorio = randint(1, 10)
#   storage += (numero_aleatorio,)
#   if i == 1:
#     menor_valor = storage[0]
#     maior_valor = storage[0]
#   for index, numero in enumerate(storage):
#     if numero < menor_valor:
#       menor_valor = numero
#     if numero > maior_valor:
#       maior_valor = numero

# print(storage)
# print(f'O maior valor sorteado foi {maior_valor}')
# print(f'O menor valor sorteado foi {menor_valor}')

# CODIGO DO GUANABARA
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os valores sorteados foram: ', end='')
for index in numeros:
  print(f'{index} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
