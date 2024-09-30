peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = peso / (altura * 2)

if imc > 0 and imc <= 18.5:
  print(f'IMC: {imc:.2f} Você está abaixo do peso.')
elif imc > 18.5 and imc <= 25:
  print(f'IMC: {imc:.2f} Você está no peso ideal.')
elif imc > 25 and imc <= 30:
  print(f'IMC: {imc:.2f} Sobrepeso.')
elif imc > 30 and imc <=40:
  print(f'IMC: {imc:.2f} Obesidade.')
else: 
  print(f'IMC: {imc:.2f} Obesidade mórbida')