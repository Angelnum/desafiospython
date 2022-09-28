salario = float(input('qual é o salario do funcionario? '))
aumento = salario + (salario*15/100)
print('o salario do funcionario que antes era R${:.2f} após o reajuste passou a ser R${:.2f} '.format(salario, aumento))
