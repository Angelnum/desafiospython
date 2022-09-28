
peso = float(input('Qual é o seu peso: '))
altura = float(input('qual é a sua altura (M): '))
imc = peso / (altura**2)
print('O IMC dessa pessoa é de {:.1f} '.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do PESO NORMAL. ')
elif 18.5 <= imc < 25:
    print('PARABÉNS, Você está na faixa de PESO NORMAL. ')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO. ')
elif 30 <= imc < 40:
    print('CUIDADO Você está em OBESIDADE. ')
else:
    print('CUIDADO Você está em OBESIDADE MÓRBIDA, procure um Médico IMEDIATAMENTE. ')
