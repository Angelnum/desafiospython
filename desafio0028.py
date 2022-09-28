'''from random import choice
print('-=-'*20)
print('Vou pensar em um número de 0 a 5. Tente advinhar... ')
print('-=-'*20)
listadenumeros =  [0, 1, 2, 3, 4, 5]
print('PROCESSANDO... ')
sleep(3)
escolhido = choice(listadenumeros)
numero = int(input('Em que número eu pensei? '))
if numero == escolhido:
    print('Parabens, você venceu a máquina! ')
else:
    print('Você perdeu! ')'''

#este de cima eu fiz sozinho e funciona igual ao do desafio mas eu vou deixar o do desafio aqui embaixo tbm


from time import sleep
from random import randint
computador = randint(0, 5) #faz o computador "pensar" em um numero aleatorio
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar... ')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta advinhar o numero aleatorio
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns, você me venceu! ')
else:
    print('GANHEI! Eu pensei no número {} e não no número {} '.format(computador, jogador))


