print('='*20)
print("10 TERMOS DE UMA PA")
print('='*20)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
for i in range(primeiro_termo, decimo_termo + razao, razao):
  print(f'{i} ', end='→ ')
print('ACABOU')