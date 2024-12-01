'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiro colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética
D) Em que posição na tabela está o time da Juventude
'''
times = (
    "Botafogo", "Palmeiras", "Internacional", "Fortaleza", "Flamengo",
    "São Paulo", "Bahia", "Corinthians", "Cruzeiro", "Atlético Mineiro",
    "Vasco da Gama", "Vitória", "Juventude", "Grêmio", "Athletico-PR",
    "Fluminense", "Criciúma", "Bragantino", "Cuiabá", "Atlético-GO"
)

for index, time in enumerate(times):
  if index == 5:
    break
  print(time)

for index, time in enumerate(reversed(times)):
  if index == 5:
    break
  print(time)

for i in sorted(times):
  print(i)

for index, time in enumerate(times):
  if time == 'Juventude':
    print(f'Posição: {index} Time: {time}')