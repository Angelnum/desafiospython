num = int(input('digite um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
ce = num // 100 % 10
milhar = num // 1000 % 10
print('analisando o numero {}... '.format(num))
print('UNIDADE: {}'.format(u))
print('DEZENA {} '.format(d))
print('centena {} '.format(ce))
print('milhar {} '.format(milhar))