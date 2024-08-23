# O carro custa 60 reais por dia e 0,15 centavos por Km rodado
dias = float(input('Quantos dias alugados? '))
kms = float(input('Quantos Km rodados? '))

total = (dias * 60) + (kms * 0.15)

print('O total a pagar é de R${:.2f}'.format(total))
