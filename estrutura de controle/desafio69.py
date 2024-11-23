"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados
C) Quantas mulheres tem menos de 20 anos
"""

maior_de_idade = 0
homens_cadastrados = 0
mulheres_menos_20 = 0
total_cadastrados = 0

while True:
  print('-'*23)
  print('  CADASTRE UMA PESSOA')
  print('-'*23)
  idade_da_pessoa = int(input('Idade: '))
  sexo_da_pessoa = str(input('Sexo [M/F]: ')).upper().strip()

  while sexo_da_pessoa != 'M' and sexo_da_pessoa != 'F':
    sexo_da_pessoa = str(input('Sexo [M/F]: ')).upper().strip()
  total_cadastrados += 1

  if idade_da_pessoa > 18:
    maior_de_idade += 1
  if sexo_da_pessoa == 'M':
    homens_cadastrados += 1
  if sexo_da_pessoa == 'F' and idade_da_pessoa < 20:
    mulheres_menos_20 += 1

  deseja_continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()
  if deseja_continuar == 'N':
    break
print(f"""
                  FIM DO PROGRAMA
---------------------------------------------------
| Total cadastrado: {total_cadastrados}'                            |
| Você cadastrou {maior_de_idade} pessoas com mais de 18 anos'   |
| {homens_cadastrados} Homens'                                       |
| {mulheres_menos_20} Mulheres com menos de 20 anos'                |
---------------------------------------------------
""")
