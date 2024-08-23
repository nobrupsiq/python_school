number = float(input('Digite uma distância em metros: '))

metros = number * 1 / 1000
hm = number / 100
dam = number / 10
dm = number * 10
cm = number * 100
mm = number * 1000

print('A medida de 3.0m corresponde a\n{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(
    metros, hm, dam, dm, cm, mm))
