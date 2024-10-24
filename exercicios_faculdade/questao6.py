"""
Dado uma lista de valores notas = [10, 8, 7, 2, 4, 9] imprima apenas notas aprovados e informe quantos aprovados.
"""

notas = [10, 8, 7, 2, 4, 9]

contador_de_aprovados = 0

for i in notas:
    if i >= 7:
        contador_de_aprovados += 1
        print(f'Nota {i} APROVADO!')

print(f'A quantidade de aprovados foi: {contador_de_aprovados}')