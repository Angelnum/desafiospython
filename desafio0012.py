p = float(input('insira o preço do produto para obter 5% de desconto R$: '))
d = p - (p*5/100)
print('o produto que custava R${:.2f}, com o cupom de desconto da promocao agora custa R${:.2f} reais. '.format(p, d))
