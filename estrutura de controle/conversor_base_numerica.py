numero = int(input('Digite um numero inteiro: '))

print("""
  \nESCOLHA UMA DAS BASES PARA CONVERSAO\n
  [1] converter para BINARIO
  [2] converter para OCTAL
  [3] converter para HEXADECIMAL
""")
opcao = int(input('Sua opcao: '))

if opcao == 1:
    print('{} convertido para BINARIO é igual a {:b}'.format(numero, numero))
elif opcao == 2:
    print('{} converito para OCTAL é igual a {:o}'.format(numero, numero))
else:
    print('{} convertido para HEXADECIMAL é igual a {:x}'.format(numero, numero))
