print('Gerador de PA')
print('-='*10)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))

termo = primeiro_termo
contador = 1
total = 0
mais_termos = 10

while mais_termos != 0:
  total += mais_termos
  while contador <= total:
    print(f'{termo} → ', end="")
    termo += razao
    contador += 1
  print('PAUSA')
  mais_termos = int(input('Quantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {total} termos mostrados.')  

    