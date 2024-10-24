"""
Crie um programa que armazena 6 notas e informa a média das notas.
"""
total_notas = 0

for i in range(1, 7):
    notas = float(input(f'Digite a {i}° nota: '))
    total_notas += notas
    media = total_notas / 6
print(f'A media das 6 notas é: {media}')