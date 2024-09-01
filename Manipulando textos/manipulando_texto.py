frase = 'Curso em Video Python'
# UMA LISTA DE STRING ELA É IMUTAVEL. NÃO CONSEGUIMOS MODIFICAR, MAS CONSEGUIMOS MODIFICAR ATRAVES DE METODOS

# Começa do caracter numero 9 e termina no caracter 21 pulando de dois em dois
frase[9:21:2]  # Quando eu omito de onde irá começar, irá começar contar do zero
frase[:5]
frase[15:]  # Indiquei o inicio e não sei o final. Inicia do caracter 15 até o final
frase[9::3]  # Inicia do caracter 9 e vai pulando de 3 em 3 até o final.
len(frase)  # Conta quantos caracter possui.
frase.count('o')  # Irá mostrar quantas vezes possui um caracter em uma string
frase.count('o', 0, 13)  # Do zero até N quantos caracter possui?
# Quantas vezes encontrou a o trecho ou a palavra especificada. Irá dizer em qua momento começou a palavra
frase.find('deo')
frase.find('Android')  # Se não existe, retorna -1
'Curso' in frase  # existe a palavra curso in frase?
frase.replace('Python', 'Android')  # Troca uma palavra pela outra
frase.upper()  # Transforma todas as letras em caixa alta
frase.lower()  # Faz o inverso da upper
frase.capitalize()  # Mantem so a primeira letra da string em caixa alta
frase.title()  # Faz o capitalize palavra por palavra
frase.strip()  # Remove todos os espaços inuteis da string
frase.rstrip()  # Remove todos os espaços inuteis da direita
frase.lstrip()  # Remove todos os espaços inuteis da esquerda

# FUNCIONALIDADES DE DIVISÃO DE STRINGS

frase.split()  # Divide as palavras onde tem um espaço, e transforma em uma lista
' '.join(frase.split())
