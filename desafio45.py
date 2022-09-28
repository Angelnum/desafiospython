from random import randint
from time import sleep
itens = ['PEDRA', 'PAPEL', 'TESOURA']
escolha = print('''SUAS OPÇÕES
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA ''')
computador = randint(0, 2)
jogador = int(input('Qual você escolhe? '))
pedr = 0 > 2 and 0 < 1
pap = 1 > 0 and 1 < 2
teso = 2 > 1 and 2 < 0
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print(7*'-=-')
print('jogador jogou {} '.format(itens[jogador]))
print('computador jogou {} '.format(itens[computador]))
print(7*'-=-')
if jogador == computador:
    print('\033[0:35mEMPATE!')
elif jogador < computador:
    print('\033[0:31mVOCE PERDEU! ')
elif jogador > computador:
    print('\033[0;32mVOCÊ GANHOU! ')
