largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede: '))

area = altura * largura

print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m²'.format(
    largura, altura, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))
