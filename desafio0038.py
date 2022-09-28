v1 = int(input('Digite o primeiro número: '))
v2 = int(input('Dgite o segundo número: '))
maior = v1
if v2 > v1:
    maior = v2
    print('O maior número é: {} '.format(maior))
if v1 == v2:
    print('Os números são iguais.')
