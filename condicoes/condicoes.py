n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a seunda nota: '))
media = (n1 + n2) / 2
print('A sua media foi {:.1f}'.format(media))
print('PARABÉNS' if media >= 6 else 'Estude mais!')
