continuar = 'S'
contador = acumulador = media = maior = menor = 0 

while continuar in 'Ss':
  numero = int(input('Digite um número: '))
  valor_continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
  continuar = valor_continuar
  acumulador += numero 
  contador += 1
  if contador == 1:
    maior = menor = numero
  else:
    if numero > maior:
      maior = numero
    if numero < menor:
      menor = numero
media = acumulador / contador
print(f'Você digitou {contador} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')