
v1 = int(input('Digite um valor: '))
v2 = int(input('digite um segundo valor: '))
v3 = int(input('digite um terceiro e ultimo valor: '))
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print('O menor número é: {} '.format(menor))
print('O maior número é {} '.format(maior))
