print('-'*30)
dias = int(input('quantos dias o carro foi usado?: '))
km = float(input('quantos km foram percorridos com o carro?: '))
pago = (dias*60) + (km*0.15)
print('total a pagar R${:.2f}'.format(pago))
print('-'*30)
