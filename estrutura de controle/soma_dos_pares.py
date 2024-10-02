total = 0
contador = 0
for i in range(1, 7):
  numeros = int(input(f'{i}° número: '))
  if numeros % 2 == 0:
    total += numeros
    contador += 1
print(f'Você informou {contador} número(s) PARES!\nE a soma dos números pares é {total}')
