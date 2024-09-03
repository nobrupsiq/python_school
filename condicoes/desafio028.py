# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

number_computer = randint(0, 5)
print(
    "----------------------\n| 🔥 VAMOS JOGAR? 🔥 |\n----------------------"
)
user = int(input('Adivinhe o número: '))
print('----------------------\n')
if user == number_computer:
    print('O número aleatório: {}\nA sua resposta: {}\n\n----------------------\n\nPARABÉNS! VOCÊ VENCEU! 🎉'.format(
        number_computer, user))
else:
    print('O número aleatório: {}\nA sua resposta: {}\n\n----------------------\n\nNão foi dessa vez 🙁 Tente de novo.'.format(
        number_computer, user))
