# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.

velocity = float(input('Qual a velocidade do carro em KM? '))

valor = 7
if velocity > 80:
    multa = velocity
    print('Velocidade: {}Km/h -> Você foi multado!'.format(velocity))
    calculo_de_multa = (velocity - 80) * 7
    print('Total a pagar R${:.2f}'.format(calculo_de_multa))
else:
    print('Velocidade: {}Km/h -> Velocidade permitida!'.format(velocity))
