# DIFERENTE DAS TUPLAS, LISTAS PODEM SER MUTAVEIS

# lanche = ['hamburguer', 'suco', 'pizza', 'pudim']

# lanche[3] = 'picole'
# lanche.append('cookie')
# lanche.insert(0, 'cachorro-quente')   
# print(lanche)
# lanche.pop(3) # ELIMINA PELO INDEX OU SE VAZIO, ELIMINA O ULTIMO VALOR
# # lanche.remove('pizza') # ELIMINA PELO CONTEUDO
# if 'pizza' in lanche:
#   lanche.remove('pizza')

# for i in lanche:
#   print(i)

# CRIANDO UMA LISTA ATRVES DO RANGE

# valores = list(range(4, 11))
# print(valores)

# valores2 = [8, 2, 5, 4, 9, 3, 0]
# print('valores 2',valores2)
# valores2.sort() # VALORES ORDENADOS
# print('valores 2',valores2)
# valores2.sort(reverse=True) # VALORES ORDENADOS EM ORDEM REVERSA
# print('valores 2',valores2)
# print(len(valores2))

# numeros = [2, 5, 9, 1]
# numeros[2] = 3
# numeros.append(7)
# numeros.sort(reverse=True)
# numeros.insert(2, 2)
# if 5 in numeros:
#   numeros.remove(5)
# else:
#   print('Não achei o número 4')
  
# print(numeros)
# print(f'Essa lista tem {len(numeros)} elementos.')


# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)

# for chave, valor in enumerate(valores):
#   print(f'Chave: {chave}, Valor: {valor}')
# print('Cheguei ao final da lista.')

# valores = list()

# for cont in range(0, 5):
#   valores.append(int(input('Digite um valor: ')))
# print(valores)

# PECULIARIDADE DO PYTHON EM LISTAS

# MODIFICA AS DUAS LISTAS, A PARTIR DE QUANDO EU LIGO UMA LISTA NA OUTRA O PYTHON CRIA UMA LIGAÇÃO ENTRE ELAS
a = [2, 3, 4, 7]
b = a # Desse jeito a variavel A e B estao completamente ligadas
b = a[:] # Desse jeito a variavel B vai recerber uma copia de todos os itens que tem na variavel A
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')