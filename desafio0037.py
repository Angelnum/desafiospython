from time import sleep
num = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das bases para a conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
print('CONVERTENDO... ')
sleep(3)
if opção == 1:
    print('O número {} convertido para BINÁRIO é: {} '.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} convertido para OCTAL é: {} '.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} convertido para HEXADECIMAL é {} '.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente.')
