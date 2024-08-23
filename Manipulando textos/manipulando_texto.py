frase = 'Curso em video Python'

# Começa do caracter numero 9 e termina no caracter 21 pulando de dois em dois
print(frase[9:21:2])

# Quando eu omito de onde irá começar, irá começar contar do zero
print(frase[:5])

# Indiquei o inicio e não sei o final. Inicia do caracter 15 até o final
print(frase[15:])

print(frase[9::3])  # Inicia do caracter 9 e vai pulando de 3 em 3 até o final.

print(len(frase))  # Conta quantos caracter possui.

# Irá mostrar quantas vezes possui um caracter em uma string
print(frase.count('o'))

print(frase.count('o', 0, 13))  # Do zero até N quantos caracter possui?

# Quantas vezes encontrou a o trecho ou a palavra especificada. Irá dizer em qua momento começou a palavra
print(frase.find('deo'))

print(frase.find('Android'))  # Se não existe, retorna -1

print('curso' in frase)  # existe a palavra curso in frase?
