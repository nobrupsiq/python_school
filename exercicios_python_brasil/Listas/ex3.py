#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = [7, 4.5, 6.8, 6]
media = 0
nota_total = 0

for i in notas:
  nota_total += i
  print(i, end=' ')

media = nota_total  / 4
print(f'Média: {media:.2f}')
