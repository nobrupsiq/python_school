# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%

salario_funcionario = float(input('Salario R$'))

if salario_funcionario > 1250:
    aumento_salario = salario_funcionario + (salario_funcionario * 0.10)
    print(f'Voce recebeu um aumento de 10% R${aumento_salario}')
if salario_funcionario <= 1250:
    aumento_salario = salario_funcionario + (salario_funcionario * 0.15)
    print(f'Voce recebeu um aumento de 15% R${aumento_salario}')
