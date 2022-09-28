from time import sleep
print('-/-'*15)
base = float(input('Digite o primeiro segmento: '))
lado1 = float(input('Digite o segundo segmento: '))
lado2 = float(input('Digite o terceiro segmento: '))
print('Analisando, Por favor aguarde... ')
sleep(3)
if base < lado1 + lado2 and lado1 < lado2 + base and lado2 < lado1 + base:
    print('É POSSÍVEL fazer um triângulo a partir desses segmentos.')
else:
    print('NÃO é fazer um triângulo a partir desses segmentos.')
print('-/-'*15)