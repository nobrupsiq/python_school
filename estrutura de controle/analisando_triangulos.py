s1 = float(input('Primeiro seguimento: '))
s2 = float(input('Segundo seguimento: '))
s3 = float(input('Terceiro seguimento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
  print('Os seguimentos podem formar um TRIÂNGULO ', end='')
  if s1 == s2 == s3:
    print('EQUILÁTERO!')
  elif s1 != s2 != s3 != s1:
    print('ESCALENO')
  else:
    print('ISOSCELES')
else:
  print('Os segmentos acima não podem formar TRIÂNGULO!')
