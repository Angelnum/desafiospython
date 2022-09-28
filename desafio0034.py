from time import sleep
sal = float(input('Digite o salário atual do funcionário: '))
print('CALCULANDO...')
sleep(4)
if sal <= 1250.00:
    print('O salario que antes era de R${:.2f} passou a ser de R${:.2f} '.format(sal, sal + (sal*15/100)))
else:
    print('O salario que antes era de R${:.2f} passou a ser R${:.2f} '.format(sal, sal + (sal*10/100)))
