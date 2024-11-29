# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado(entre 0 20) e mostrá-lo por extenso.
contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco','Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
  numero_do_usuario = int(input('Digite um número entre 0 e 20: '))
  while numero_do_usuario > 20 or numero_do_usuario < 0:
    numero_do_usuario = int(input('Tente novamente. Digite um número entre 0 e 20: '))

  for index, contador in enumerate(contagem):
    if index == numero_do_usuario:
      print(contador)
  break