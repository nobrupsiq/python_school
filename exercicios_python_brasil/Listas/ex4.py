# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

caracters = ['a', 'e', 'r', 'q', 'u', 'c', 'z', 'a', 'q', 'i']
vogais  =  ['a', 'e', 'i', 'o', 'u']

vetor_consoantes = []
total_consoantes = 0

for i in caracters:
  if i not in vogais:
    print(i)
    vetor_consoantes.append(i)
    total_consoantes += 1

print(f'Total de consoantes: {total_consoantes}')



