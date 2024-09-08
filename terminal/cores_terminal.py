'''
STYLE
0 = none
1 = bold
4 = underline
7 = negative

TEXTO
30 = branco
31 = vermelho
32 = verde
33 = amarelo
34 = azul marinho
35 = Roxo
36 = azul claro
37 = cinza

BACKGROUNd
40 = branco
41 = vermelho
42 = verde
43 = amarelo
44 = azul marinho
45 = roxo
46 = azul claro
47 = cinza
'''

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
