number = float(input('Quanto dinheiro você tem na carteira? R$'))

# 1 real equivale a 0.1821129 dolares
# 1 dolar custa 5,48 reais
result = number / 5.48

print('Com R${} você pode comprar U${:.2f}'.format(number, result))
