# Crie um programa que leia no nome de uma cidade e diga se ela começa ou nao com o nome "SANTO".

city_name = input('Em que cidade voce nasceu? ').strip()
print(city_name[:5].upper() == 'SANTO')
