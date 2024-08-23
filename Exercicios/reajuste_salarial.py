salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(
    salario, aumento))

# 2° Exercicio proposto

preco_produto = float(input('Qual o valor do produto? R$'))
desconto_avista = preco_produto - (preco_produto * 15 / 100)
juros_a_prazo = preco_produto + (preco_produto * 5 / 100)
print('Pagamento a vista 15% de desconto R${:.2f}\nPagamento parcelado juros de 5% R${:.2f}'.format(
    desconto_avista, juros_a_prazo))
