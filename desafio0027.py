
nome = str(input('digite seu nome completo: ').strip())
primeironome = nome.split()
print('seu primeiro nome é : {}'.format(primeironome[0]))
print('seu ultimo nome é :{}'.format(primeironome[len(primeironome)-1]))
