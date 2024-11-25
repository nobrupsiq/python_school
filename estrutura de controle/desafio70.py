"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:

A - Qual é o total gasto na compra.
B - Quantos produtos custam mais de R$1000.
C - Qual é o nome do produto mais barato.
"""
contador = 0
total_gasto = 0
produto_mais_de_mil = 0
produto_de_menor_valor = 0
nome_do_produto_de_menor_valor = ''

while True:
  nome_do_produto = str(input('Nome do produto: '))
  valor_do_produto = float(input('Preco: R$'))
  contador += 1
  total_gasto += valor_do_produto

  if valor_do_produto > 1000:
      produto_mais_de_mil += 1

  if contador == 1:
    produto_de_menor_valor = valor_do_produto
  else:
    if valor_do_produto < produto_de_menor_valor:
      produto_de_menor_valor = valor_do_produto
      nome_do_produto_de_menor_valor = nome_do_produto
  
  continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
  
  while continuar != 'S' and continuar != 'N':
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
  if continuar == 'N':
    break
print('\n-------------- FIM DO PROGRAMA --------------')
print(f'O total da compra foi R${total_gasto:.2f}')
print(f'Temos {produto_mais_de_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_do_produto_de_menor_valor} que custa R${produto_de_menor_valor:.2f}')