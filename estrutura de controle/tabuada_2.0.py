numero = int(input('Digite um número para ver sua tabuada: '))

for i in range(1, 11):
  calculo = numero * i
  print(f'{numero} x {i} = {calculo}')