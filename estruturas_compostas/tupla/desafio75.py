"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

#MEU CODIGO NÃO TERMINADO
# storage = ()
# tot9 = 0
# pos3 = 0
# total_de_pares = 0

# for i in range(1, 5):
#   numeros = int(input(f'Digite o {i}° número: '))
#   storage += (numeros,)

# for index, target in enumerate(storage):
#   if target == 9:
#     tot9 += 1
#   if target == 3:
#     pos3 = index;
#   else:
#     pos3 = 'O valor 3 não foi digitado em nehuma posição'
#   if target % 2 == 0:
#     total_de_pares += 1

# print(f'Você digitou os valores: {storage}')
# print(f'O número 9 apareceu: {tot9} vez(s)')
# print(f'O valor 3 apareceu na {pos3}° posição');
# print(f'O total de números pares: {total_de_pares}')

numeros = (int(input('Digite um número: ')), 
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')),)

print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
  print(f'O valor 3 apareceu na {numeros.index(3) + 1}° posição')
else:
  print('O valor 3 não foi digitado.')
print(f'Os valores pares digitados foram ', end='')
for i in numeros:
  if i % 2 == 0:
    print(i, end=' ')