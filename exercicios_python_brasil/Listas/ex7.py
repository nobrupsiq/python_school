"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""
total_soma = 0
total_multiplicacao = 1
vetor_de_numeros_inteiros = [7,9,3,4,2]


for index in vetor_de_numeros_inteiros:
  total_soma += index
  total_multiplicacao *= index

print(f'\nTotal dos números SOMADOS: {total_soma}')
print(f'Total dos números MULTIPLICADOS: {total_multiplicacao}')
print(*vetor_de_numeros_inteiros, sep=', ', end='.')