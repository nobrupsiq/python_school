"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = ''

while sexo != 'M' and sexo != 'F':
  sexo_do_usuario = input('Digite o seu Sexo "M" ou "F": ')
  sexo = sexo_do_usuario
  if sexo != 'M' and sexo != 'F':
    print(f'Valor incorreto, você digitou {sexo}.', end=' ')