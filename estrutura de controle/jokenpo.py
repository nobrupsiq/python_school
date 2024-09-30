from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')

print("""
[0] PEDRA
[1] PAPEL
[2] TESOURA
""")

computador = randint(0, 2)
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(0.5)

print('-='*14)
print(f'O computador escolheu {itens[computador]}')
print(f'O jogador escolheu {itens[jogador]}')
print('-='*14)

if computador == 0:
  if jogador == 0:
    print('EMPATE')
  elif jogador == 1:
    print('JOGADOR VENCE')
  elif jogador == 2:
    print('COMPUTADOR VENCE')
  else:
    print('JOGADA INVÁLIDA')  
elif computador == 1:
  if jogador == 0:
    print('COMPUTADOR VENCE')
  elif jogador == 1:
    print('EMPATE')
  elif jogador == 2:
    print('JOGADOR VENCE')
  else:
    print('JOGADA INVÁLIDA')  
elif computador == 2:
    if jogador == 0:
      print('JOGADOR VENCE')
    elif jogador == 1:
      print('COMPUTADOR VENCE')
    elif jogador == 2:
      print('EMPATE')
    else:
      print('JOGADA INVÁLIDA')