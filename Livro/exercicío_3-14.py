# Você é dono de uma loja que vende produtos. Sua política é de dar desconto para quem compra à vista, vender pelo preço de etiqueta para quem paga em 5 vezes e cobrar juros de quem compra em 10 vezes. Escreva um programa que leia o valor de uma compra e imprima três valores, todos com até duas casas decimais:

# • O valor para pagamento à vista, com desconto de 9%.
# • O valor da prestação para pagamento em 5 vezes, sem desconto nem juros.
# • O valor da prestação para pagamento em 10 vezes, com 17% de juros.


value = float(input('Valor do produto R$ '))
avista = value - (value * 9 / 100)
dezvezes = value + (value * 17 / 100)
print(dezvezes)
