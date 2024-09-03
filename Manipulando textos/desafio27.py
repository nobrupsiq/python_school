# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

# EX: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza

name = str(input('Enter your full name: ')).strip()

name_split = name.split()
print(name_split[0], name_split[-1])
