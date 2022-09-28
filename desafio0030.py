from time import sleep
num = int(input('Me diga um número qualquer: '))
print('-=-'*10)
print('ANALISANDO O NÚMERO {} '.format(num))
print('-=-'*10)
sleep(3)
if (num%2) == 0:
    print('o numero {} é PAR.'.format(num))
else:
    print('o numero {} é IMPAR'.format(num))
