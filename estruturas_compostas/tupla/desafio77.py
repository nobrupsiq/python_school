"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('aprender', 'programar', 'linguagem', 'python', 'Curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programar', 'futuro')

for index in palavras: 
  print(f'\nNa palavra {index.upper()} temos as vogais ', end='')
  for letra in index:
    if letra.lower() in 'aeiou':
      print(letra, end=' ')