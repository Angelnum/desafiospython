from math import radians, sin, cos, tan
ang = float(input('digite o angulo que voce quer saber o seno, cosseno e tangente: '))
seno = sin(radians(ang))
cose = cos(radians(ang))
tange = tan(radians(ang))
print('o angulo de {:.2f} tem o SENO de {:.2f} '.format(ang, seno))
print('o angulo de {:.2f} tem o COSSENO de {:.2f} '.format(ang, cose))
print('o angulo de {:.2f} tem a TANGENTE de {:.2f} '.format(ang, tange))
