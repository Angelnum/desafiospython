casa = float(input('Qual é o valor da casa? R$:' ))
salário = float(input('Qaul é o salário do comprador? R$:' ))
anos = int(input('Quanto anos de financiamento? R$:' ))
prestação = casa / (anos*12)
if (salário*30/100) < prestação:
    print('Para pagar uma casa de {:.2f} a prestação será de {:.2f} em {} anos.'.format(casa, prestação, anos))
    print('EMPRÉSTIMO NEGADO')
else:
    (salário*30/100) > prestação
    print('Para pagar uma casa de {:.2f} a prestação será de {:.2f} em {} anos. '.format(casa, prestação, anos))
    print('O EMPRÉSTIMO SERÁ CONCEDIDO')
