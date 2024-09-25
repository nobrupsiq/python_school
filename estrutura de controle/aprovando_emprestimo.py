"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
1° Pergunte o valor da casa 
2° O salário do comprador
3° Em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.
"""

valor_da_casa = float(input('Valor da casa: R$'))
salario_do_comprador = float(input('Salario do comprador: R$'))
anos_financiamento = int(input('Quantos anos de financiamento? '))

valor_da_prestacao = valor_da_casa / (anos_financiamento * 12)
calculo_salario = salario_do_comprador * 30 / 100

print(
    f"Para pagar uma casa de R${valor_da_casa:.2f}, em {anos_financiamento} anos a prestacao sera de R${valor_da_prestacao:.2f}")

if calculo_salario >= valor_da_prestacao:
    print('Emprestimo APROVADO!')
else:
    print('Emprestimo NEGADO!')
