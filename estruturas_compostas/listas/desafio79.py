"""
Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número ja exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
continuar = 'S'
lista_de_valores = [] 

while continuar in 'Ss':
  numero_usuario = int(input('Digite um valor: '))

  if numero_usuario not in lista_de_valores:
    lista_de_valores.append(numero_usuario)
    print('Valor adicionado com sucesso...')
  else:
    print('Valor ja existente, não adicionado.')
  continuar = str(input('Quer continuar? [S/N]: ')).strip()[0]

print(f'Você digitou os valores {sorted(lista_de_valores)}')