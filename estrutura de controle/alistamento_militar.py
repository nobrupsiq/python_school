# ano_nascimento = int(input('Ano de nascimento: '))

# idade = 2024 - ano_nascimento
# anos_para_alistamento = 18 - idade


# print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em 2024')
# if idade < 18:
#   print(f'Ainda faltam {anos_para_alistamento} anos para o alistamento\nSeu alistamento será em {(anos_para_alistamento + idade) + ano_nascimento}.')
# elif idade > 18:
#   print(f'Voce ja deveria ter se alistado há {idade - 18} anos.\nSeu alistamento foi em {ano_nascimento + 18}.')

# CODIGO IMPORTANDO MODULOS

from datetime import date

atual = date.today().year
ano_de_nascimento = int(input('Ano de nascimento: '))
idade = atual - ano_de_nascimento

print(f'Quem nasceu em {ano_de_nascimento} tem {idade} anos em {atual}')

if idade == 18:
  print('Voce tem que se alistar IMEDIATAMENTE')
elif idade < 18:
  saldo = 18 - idade
  print(f'Ainda faltam {saldo} anos para o alistamento.')
  ano = atual + saldo
  print(f'Seu alistamento será em {ano}')
elif idade > 18:
  saldo = idade - 18
  ano = atual - saldo
  print(f'Você já deveria ter se alistado a {saldo} anos.')
  print(f'Seu alistamento foi em {ano}')