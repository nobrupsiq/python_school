"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
"""
valor = int(input('Que valor você quer sacar? R$'))
cedula = 50
valor_de_saque = valor
total_cedulas = 0

while True:
  if valor_de_saque >= cedula: # SE O VALOR DO SAQUE FOR MAIOR QUE 50
    valor_de_saque -= cedula # VAI DIMINUIR 50 DO VALOR QUE A PESSOA QUER SACAR
    total_cedulas += 1 
  else: # Agora se o valor do saque for menor que 50 ele cai nesse bloco else
    if total_cedulas > 0:
      print(f'Total de {total_cedulas} cédulas de R${cedula}')
    if cedula == 50:
      cedula = 20
    elif cedula == 20:
      cedula = 10
    elif cedula == 10:
      cedula = 1
    total_cedulas = 0
    if valor_de_saque == 0:
      break