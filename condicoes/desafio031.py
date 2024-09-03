# Desenvolva um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200Km e R$ 0,45 para viagens mais longas.

distancia_viagem = float(input('Digite a distancia da sua viagem: '))

if distancia_viagem <= 200 and distancia_viagem > 0:
    calculo = distancia_viagem * 0.50
    print('Distancia: {:.2f}Km\nValor a pagar R${}'.format(
        distancia_viagem, calculo))
else:
    calculo = distancia_viagem * 0.45
    print('Distancia: {:.2f}Km\nValor a pagar R${}'.format(
        distancia_viagem, calculo))
