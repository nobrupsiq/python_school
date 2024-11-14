"""
Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
from time import sleep
contador = 0
resultado_computador = 0

while True:
  escolha_do_jogador = str(input('ÍMPAR OU PAR? ')).upper().strip()
  escolha_do_computador = 'IMPAR' if escolha_do_jogador == 'PAR' else 'PAR'
  print(f'Então o computador vai ser: {escolha_do_computador}')

  numero_do_jogador = int(input('Escolha um número de 1 a 10: '))
  numero_do_computador = randint(1, 10)
  sleep(.5)
  print(f'Jogador escolheu: {numero_do_jogador}')
  sleep(.5)
  print(f'Computador escolheu: {numero_do_computador}')
  sleep(.5)
  soma = numero_do_jogador + numero_do_computador

  if soma % 2 == 0:
    if escolha_do_jogador == 'PAR':
      print('O RESULTADO É PAR! JOGADOR VENCEU!')
      contador += 1
    else:
      print('O RESULTADO É PAR! O COMPUTADOR VENCEU!')
      resultado_computador += 1
  if soma % 2 != 0:
    if escolha_do_jogador == 'IMPAR':
      print('O RESULTADO É IMPAR! O JOGADOR VENCEU!')
      contador += 1
    else:
      print('O RESULTADO É IMPAR! O COMPUTADOR VENCEU!')
      resultado_computador += 1
  if resultado_computador == 1:
    break
print(f'Você conseguiu {contador} vitória(s) consecutivas. PARABÉNS!')

