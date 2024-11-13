# Sequencia fibonacci
# 0 1 1 2 3 5 8

print('-'*25 + '\nSequência de Fibonacci\n' + '-'*25)

contador = 3
anterior = 0
atual = 1
acumulador = 0

termos = int(input('Quantos termos você quer mostrar? '))
print(f'{anterior} → {atual}', end='')
while contador <= termos:
  acumulador = anterior + atual
  print(f' → {acumulador}', end='')
  anterior = atual
  atual = acumulador
  contador += 1
print(' → FIM')
