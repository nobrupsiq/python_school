"""
Faça um programa que leia 5 valores e guarde-os em uma lista.

No final, mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista.
"""

lista = []
maior_valor = menor_valor = 0

for valor, index in enumerate(range(0, 5)):
  lista.append(int(input(f'Digite um número. Posição {index}: ')))
  
  if index == 1:
    maior_valor = lista[valor]
    menor_valor = lista[valor]

  if lista[valor] < menor_valor:
    menor_valor = lista[valor]
  if lista[valor] > maior_valor:
    maior_valor = lista[valor]
  
print(f'Maior valor: {maior_valor} Posição: {lista.index(maior_valor)}')
print(f'Menor valor: {menor_valor} Posição: {lista.index(menor_valor)}')