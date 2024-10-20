# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

vetor_de_numeros_par = []
vetor_de_numeros_impar = []
numeros_inteiros = []

for i in range(1, 21):
  numeros_inteiros.append(i)
  if i % 2 == 0:
    vetor_de_numeros_par.append(i)
  else:
    vetor_de_numeros_impar.append(i)

print(numeros_inteiros)
print(vetor_de_numeros_par)
print(vetor_de_numeros_impar)