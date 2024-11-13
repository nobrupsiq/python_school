# Tratando varios valores


numero = contador = acumulador = 0

while numero != 999:
  acumulador += numero;
  numero = int(input('Digite um número [999 para parar]: '))
  contador += 1
print(f'Você digitou {contador - 1} números e a soma entre eles foi {acumulador}')