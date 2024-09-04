# Faça um programa que leia três números e mostre qual é o maior e qual é o menor
n1 = int(input('Digite 1° número: '))
n2 = int(input('Digite 2° número: '))
n3 = int(input('Digite 3° número: '))

# Verificando quem é menor
menor = n1

# Logica do menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Verificando quem é o maior
maior = n1
# Logica do maior
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor valor digitado foi {}\nO maior valor digitado foi {}'.format(menor, maior))
