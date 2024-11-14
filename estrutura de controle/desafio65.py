continuar = 'S'
contador = acumulador = media = 0 

while continuar in 'Ss':
  numero = int(input('Digite um número: '))
  valor_continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
  continuar = valor_continuar
  acumulador += numero
  contador += 1
media = acumulador / contador
print(f'Você digitou {contador} números e a média foi {media}')