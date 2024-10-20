"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
"""

idades = []
alturas = []

for i in range(1, 6):
  print(f'{i}° Pessoa:')
  idade = int(input('Idade: '))
  altura = float(input('Altura: '))

  idades.append(idade)
  alturas.append(altura)

for i in range(len(idades)-1,-1,-1):
  print('Idade:', idades[i], "Altura:", alturas[i])
