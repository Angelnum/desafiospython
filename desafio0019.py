from random import choice
a1 = str(input('digite o nome do primeiro aluno: '))
a2 = str(input('agora do segundo aluno: '))
a3 = str(input('agora digite o nome do terceiro aluno: '))
a4 = str(input('e por fim, digite o nome do ultimo e quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('o escolhido foi:{} '.format(escolhido))
