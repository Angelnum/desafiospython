nota1 = float(input('Digite a primeira nota do Aluno: '))
nota2 = float(input('Digite a segunda nota do Aluno: '))
r = (nota1 + nota2)/2
print('Tirando {} e {} a média do Aluno é de {:.1f} '.format(nota1, nota2, r))
if r < 5.0:
    print('O Aluno esta REPROVADO. ')
elif r >= 7.0:
    print('O Aluno está APROVADO. ')
elif 7 > r >= 5:
    print('O Aluno está de RECUPERAÇÃO. ')
