contador = 0
total_da_soma = 0

while True:
  numero = int(input('Digite um número [999 para sair]: '))
  if numero == 999:
    break
  contador += 1
  total_da_soma += numero
print(f'Foram digitados {contador} números e a soma desses números é {total_da_soma}')