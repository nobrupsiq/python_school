total = 0
cont = 0

for i in range(1, 501, 2):
  if i % 3 == 0:
    total += i
    cont += 1

print(f'A soma de todos os {cont} valores solicitados é {total}')