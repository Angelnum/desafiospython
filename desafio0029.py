from time import sleep
velo = float(input('Qual é a velociade atual do carro? '))
km = (velo - 80 ) * 7
print('Processando...')
sleep(3)
if velo >= 80:
    print('MULTADO!! Seu carro excedeu o limite de velociade e você foi multado em {:.2f} reais. '.format(km))
print('Tenha um bom dia. Dirija com segurança. ')
