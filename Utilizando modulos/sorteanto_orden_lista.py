import random
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')

list_names = [n1, n2, n3, n4]

random.shuffle(list_names)

print('A ordem da apresentação será\n{}'.format(list_names))
