"""
Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

primeiro_numero = float(input('Digite o primeiro número: '))
segundo_numero = float(input('Digite o segundo número: '))

escolha_do_usuario = 0

while escolha_do_usuario != '5':
    escolha_do_usuario = input("""
        O que você quer fazer com os seus números?

        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa
         """)
    escolha_do_usuario = escolha_do_usuario
    if escolha_do_usuario == '1':
        soma = primeiro_numero + segundo_numero
        print(f'A soma dos dos números: {primeiro_numero} e {segundo_numero} é {soma}')

    if escolha_do_usuario == '2':
        multiplicacao = primeiro_numero * segundo_numero
        print(f'A multiplicação dos dos números: {primeiro_numero} e {segundo_numero} é {multiplicacao}')

    if escolha_do_usuario == '3':
        if primeiro_numero > segundo_numero:
            print(f'O número {primeiro_numero} é maior que o {segundo_numero}')
        else:
            print(f'O número {segundo_numero} é maior que o {primeiro_numero}')

    if escolha_do_usuario == '4':
        primeiro_numero = float(input('Digite o 1° novo número: '))
        segundo_numero = float(input('Digite o 2° novo número: '))
        
    if escolha_do_usuario == '5':
        escolha_do_usuario = '5'
        

