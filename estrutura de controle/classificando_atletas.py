ano_nascimento = int(input('Ano de nascimento: '))

from datetime import date
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade > 0 and idade <= 9:
  print(f'Idade: {idade}\nClassificação: MIRIM')
elif idade > 9 and idade <= 14:
  print(f'Idade: {idade}\nClassificação: INFANTIL') 
elif idade > 14 and idade <= 19:
  print(f'Idade: {idade}\nClassificação: JUNIOR')
elif idade > 19 and idade <= 25:
  print(f'Idade: {idade}\nClassificação: SÊNIOR')
else:
  print(f'Idade: {idade}\nClassificação: MASTER')
