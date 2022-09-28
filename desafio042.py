base = float(input('Digite o primeiro segmento: '))
lado1 = float(input('Digite o segundo segmento: '))
lado2 = float(input('Digite o terceiro segmento: '))
if base < lado1 + lado2 and lado1 < lado2 + base and lado2 < lado1 + base:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if base == lado1 == lado2:
        print('EQUILATERO')
    elif base != lado1 != lado2 != base:
        print('ESCALENO')
    else:
        print('ISÒSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo. ')
