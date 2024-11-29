# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado(entre 0 20) e mostrá-lo por extenso.
contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco','Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

numero_do_usuario = int(input('Digite um número entre 0 e 20: '))

for index, contador in enumerate(contagem):
  if index == numero_do_usuario:
    print(contador)