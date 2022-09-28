nome = str(input('digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('seu nome em letras maiusculas é: {} '.format(nome.upper()))
print('-'*45)
print('seu nome em letras minusculas é: {} '.format(nome.lower()))
print('-'*45)
print('seu nome ao todo contem {} letras. '.format(len(nome) - nome.count(' ')))
print('-'*45)
print('seu primeiro nome tem {} letras '.format(nome.find(' ')))
print('-'*45)
primeironome = nome.split()
print('seu nome é muito bonito, {}. tenha um ótimo dia. '.format(primeironome[0]))









'''
Uma string utiliza o número 0 como representação do primeiro caracter.
Uma string é imutável, apenas se podem mudar temporariamente ou então temos que recorrer a uma atribuição.
print(frase[3])         Imprime a terceira letra
print(frase[3:13])      Imprime da terceira letra á décima terceira.*(Décima terceira letra não incluida)
print(frase[:13])       Imprime do princípio até á décima terceira letra.*
print(frase[13:])       Imprime da décima terceira letra até ao final.
print(frase[1:13:2])    Imprime da primeira letra á décima terceira, omitindo uma letra de dois em dois.*
print(frase[::2])       Imprime a string inteira, omitindo uma letra de dois em dois.
print(frase.count('o')) Imprime quantos o's minusculos tem na string frase.
print(frase.upper().count('o')) Transforma toda a string em maiusculas e imprime quantos o's minusculos têm a string.
print(len(frase))               Imprime o numero total de caracteres da string frase.(Incluindo espaçoes)
print(len(frase.strip()))       Retira os espaçoes existentes no começo e no final da string e imprime a quantidade de
                                caracteres da string, já com os espaços retirados.
print(frase.replace('Python', 'Android'))   Caso esista um conjunto de caracteres seguidos, neste caso Python, na
                                            string, estes são substituidos por os indicados, Android neste caso.(Se for
                                            preciso, o numero de caracteres aumenta)
print('Curso' in frase)                     Retorna False ou True, dependendo se a palavra curso está dentro da string
                                            frase.
print(frase.find('Video'))                  Retorna -1 caso a palavra indicada, no caso Video, não esteja presente na
                                            string. Caso contrário, retorna o numero no qual começa essa palavra na
                                            string.
print(frase.split())                        Cria uma lista que separa todas as palavras. As palavras são identificadas
                                            através dos espaços entre elas.
'''