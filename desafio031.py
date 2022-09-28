from time import sleep
dist = float(input('Qual é a distância da viagem? '))
print('Você está prestes a fazer uma viagem de {:.1f}km. '.format(dist))
valor1 = dist*0.50
valor2 = dist*0.45
print('CALCULANDO VALOR... ')
sleep(3)
if dist <= 200:
    print('O custo da viagem será de: {:.1f} reais. '.format(valor1))
else:
    print('O custo da sua viagem será de {:.2f}'.format(valor2))
