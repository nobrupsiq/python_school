"""
 Crie um programa que caso o número seja divisível por 3, ele imprime fizz, se for divisível por 5 imprime buzz, se for divisível por 3 e 5 imprime fizzBuzz. Se não for nenhuma dessas condições, imprime apenas os valores.
"""

numero = float(input('Digite um número: '))

if numero % 3 == 0 and numero % 5 == 0:
    print('fizzBuzz')
elif numero % 3 == 0:
    print('fizz')
elif numero % 5 == 0:
    print('buzz')
else:
    