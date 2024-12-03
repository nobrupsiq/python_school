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
print(f'Lista de times do Brasileirão: {times}')
print(f'Os 5 primeiros são: {times[0:5]}')
print(f'Os 4 últimos são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
