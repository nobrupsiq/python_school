"""
Melhore o jogo do DESAFIO028 onde o computador vai 'pensas' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, ostrando no final quantos palpites foram necessários
"""

from random import randint

total_de_palpites = 0

numero_do_computador = randint(1, 11)

palpite = 0

while palpite != numero_do_computador:
    palpite = int(input('Digite o seu palpite: '))
    total_de_palpites += 1
    if palpite != numero_do_computador:
      print('Você errou!')
    else:
       print(f'Voce acertou! Numero do computador {numero_do_computador}. Seu palpite {palpite}')
print(f'Total de palpites {total_de_palpites}')


