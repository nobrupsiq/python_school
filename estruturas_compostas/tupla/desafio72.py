# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado(entre 0 20) e mostrá-lo por extenso.
contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco','Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')



while True:
  continuar = 'S'
  while continuar in 'Ss':
    numero_do_usuario = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero_do_usuario <= 20:
        break
    print('Tente novamente. ', end='')
  print(f'Você digitou o número {contagem[numero_do_usuario]}')
  continuar = str(input('Quer continuar? [S, N]: ')).upper().strip()[0]
  if continuar != 'S':
     print('Até logo!')
     break