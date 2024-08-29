# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
nome_completo = 'Bruno pires de siqueira'
nome_completo.upper()
# O nome com todas minusculas
nome_completo.lower()
# Quantas letras ao todo (sem considerar espacos)
split_name = nome_completo.split()
string_sem_espaco = ''.join(split_name)
len(string_sem_espaco)
# Quantas letras tem o primeiro nome
first_name = nome_completo[0:5]
len(first_name)
