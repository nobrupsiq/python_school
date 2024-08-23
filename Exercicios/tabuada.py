number = int(input('Digite um número para ver sua tabuada: '))

print('-'*11)
for i in range(1, 11):
    print('{} x {:2} = {}'.format(number, i, (number*i)))
print('-'*11)
