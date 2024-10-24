"""
Crie um programa que caso o número seja divisível por 3, ele imprime fizz, se for divisível por 5 imprime buzz, se for divisível por 3 e 5 imprime fizzBuzz. Se não for nenhuma dessas condições, imprime o numero. Será de 1 a 15
"""

for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print(f'{i} fizzBuzz')
    elif i % 3 == 0:
        print(f'{i} fizz')
    elif i % 5 == 0:
        print(f'{i} buzz')
    else:
        print(f'{i}')
    