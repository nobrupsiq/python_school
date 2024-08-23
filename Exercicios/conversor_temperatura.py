# formula (0°C x 9/5) + 32 = 32°F

temperatura = float(input('Informe a temperatura em °C:'))
formula = (temperatura * 9 / 5) + 32
print('A temperatura de {:.2f}°C corresponde a {:.1f}°F!'.format(
    temperatura, formula))
