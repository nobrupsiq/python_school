import math
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))

semLib = (oposto ** 2) + (adjacente ** 2)

hipotenusa = math.hypot(oposto, adjacente)  # Com LIB
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
