numero = int(input('Digite um número: '))

contador = 0

for i in range(1, numero + 1):
  if numero % i == 0:
    contador += 1
    print('\033[33m', end=' ')
  else:
    print('\033[31m', end=' ')
  print(f'{i}', end=' ')

print(f'\n\033[mO número {numero} foi divisível {contador} vezes')
if contador == 2:
  print(f'Número PRIMO!')
else:
  print(f'E por isso ele NÃO É PRIMO!')