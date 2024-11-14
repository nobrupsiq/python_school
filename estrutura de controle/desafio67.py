"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, pada cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

while True:
  print('-'*36)
  numero_da_tabuada = int(input('Quer ver a tabuada de qual valor?: '))
  print('-'*36)
  if numero_da_tabuada < 0:
    print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
    break
  for i in range(1, 11):
    multiplicacao = numero_da_tabuada * i
    print(f'{numero_da_tabuada} x {i} = {multiplicacao}')
  