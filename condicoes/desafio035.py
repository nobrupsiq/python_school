'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

Desigualdade Triangular: A soma dos comprimentos de quaisquer dois lados de um triângulo deve ser maior que o comprimento do terceiro lado.

Aplicando a desigualdade triangular às nossas varetas:

5 cm + 7 cm > 3 cm (Verdadeiro)
5 cm + 3 cm > 7 cm (Verdadeiro)
7 cm + 3 cm > 5 cm (Verdadeiro)
Como todas as desigualdades são verdadeiras, podemos concluir que as três varetas formam um triângulo.

Outro Exemplo:

Vareta A: 2 cm

Vareta B: 4 cm

Vareta C: 7 cm

2 cm + 4 cm = 6 cm, o que não é maior que 7 cm.
'''
print('-='*20)
print('ANALISADOR DE TRIANGULO')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if (r1 + r2 > r3) and (r2 + r3 > r1) and (r3 + r1 > r2):
    print('Triangulo formado!')
else:
    print('Triangulo não formado!')
