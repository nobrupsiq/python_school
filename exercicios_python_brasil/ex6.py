# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

nota_dos_alunos = []
total_media = 0
soma_das_4_notas = 0

for alunos in range(1, 11):
  print(f'\nDigite as 4 notas do {alunos}° aluno!\n')
  for aluno in range(1, 5):
    nota = float(input(f'Digite a {aluno}° nota: '))
    soma_das_4_notas += nota
  total_media = soma_das_4_notas / 4
  nota_dos_alunos.append(total_media)

for i in range(0, len(nota_dos_alunos)):
  print(f'\nMédia do {i + 1}° Aluno: {nota_dos_alunos[i]}', end='')