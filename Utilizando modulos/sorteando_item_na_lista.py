import random
first_student = input('Primeiro aluno: ')
second_student = input('Segundo aluno: ')
third_student = input('Terceiro aluno: ')
fourth_student = input('Quarto aluno: ')

list_names = [first_student, second_student, third_student, fourth_student]


result = random.choice(list_names)

print('O aluno escolhido foi {}.'.format(result))
