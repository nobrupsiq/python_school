"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo_do_usuario = str(input('Digite o seu Sexo "M" ou "F": ')).strip().upper()[0]
while sexo_do_usuario not in 'MmFf':
    sexo_do_usuario = str(input(f'Valor incorreto! Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo_do_usuario} registrado com sucesso')