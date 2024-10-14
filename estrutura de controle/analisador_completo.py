from datetime import date

acumulador_idade = 0
mais_velho = 0
nome_do_mais_velho = ''
sexo_feminino_total = 0
# ano_atual = date.today().year

for i in range(1, 5):
  print(f'----- {i}° PESSOA -----')
  nome = str(input('Nome: ')).strip()
  idade = int(input('Idade: '))
  sexo = str(input('Sexo [M/F]: ')).strip()

  acumulador_idade += idade
  media_de_idade = acumulador_idade / 4

  if sexo in 'Ff' and idade < 20:
    sexo_feminino_total += 1
  if idade > mais_velho:
    mais_velho = idade
    nome_do_mais_velho = nome

print(f'A média de idade do grupo é de {media_de_idade} anos')
print(f'O homem mais velho tem {mais_velho} anos e se chama {nome_do_mais_velho}')
print(f'Ao todo são {sexo_feminino_total} mulheres com menos de 20 anos')