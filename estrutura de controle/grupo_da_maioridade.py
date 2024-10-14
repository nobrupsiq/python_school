from datetime import date

ano_atual = date.today().year
maior_de_idade = 0
menor_de_idade = 0

for i in range(1, 8):
  ano_nascimento = int(input(f'Em que ano a {i}° pessoa nasceu? '))

  idade = ano_atual - ano_nascimento

  if idade >= 18:
    maior_de_idade += 1
  else:
    menor_de_idade += 1

print(f'\nAo todo tivemos {maior_de_idade} pessoas maiores de idade\nE também tivemos {menor_de_idade} pessoas menores de idade')