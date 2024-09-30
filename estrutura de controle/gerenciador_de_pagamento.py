print('\n{:=^40}'.format('LOJAS GUANABARA'))

valor_compra = float(input('\nPreço das compras: R$'))

print("""
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
""")
opcao = int(input('Qual é a opção? '))

if opcao == 1:
  total = valor_compra - (valor_compra * 10 / 100)
  print(f'Sua compra de R${valor_compra} vai custar R${total:.2f} no final.')
elif opcao == 2:
  total = valor_compra - (valor_compra * 5 / 100)
  print(f'Sua compra de R${valor_compra} vai custar R${total:.2f} no final.')
elif opcao == 3:
  parcelas = valor_compra / 2
  print(f'Sua compra será parcelada em 2x de R${parcelas:.2f} SEM JUROS')
  print(f'Sua compra de R${valor_compra} vai custar R${valor_compra:.2f} no final.')
else:
  total = valor_compra + (valor_compra * 20 / 100)
  total_parcelas = int(input("Quantas parcelas? "))
  parcelas = valor_compra / total_parcelas
  print(f'Sua compra será parcelada em {total_parcelas}x de R${parcelas:.2f}')
  print(f'Sua compra de R${valor_compra} vai custar R${total:.2f} no final.')