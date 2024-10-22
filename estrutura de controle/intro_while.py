# for i in range(1, 10):
#   print(i)
# print('FIM')


# resposta = 'S'

# while resposta == 'S':
#   n = int(input('Digite um valor: '))
#   resposta = str(input('Quer continuar? '))
# print('Fim')

n = 1
par = 0
impar = impar = 0


while n != 0:
  n = int(input('Digite um valor: '))
  if n != 0:
    if n % 2 == 0:
      par +=1
    else:
      impar += 1
print(f'Você digitou {par} numeros pares e {impar} numeros impares')