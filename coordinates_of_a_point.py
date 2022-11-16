def descobrir_quadrante(X, Y):
    if X > 0:
        if Y > 0:
            quadrante = 'Q1'
        else:
            quadrante = 'Q4'
    elif X < 0:
        if Y > 0:
            quadrante = 'Q2'
        else:
            quadrante = 'Q3'
    return quadrante

coordenadas = input().split()
X = float(coordenadas[0])
Y = float(coordenadas[1])

if X == 0:
    if Y == 0:
        print('Origem')
    elif Y != 0:
        print('Eixo Y')
elif Y == 0:
    print('Eixo X' )
else:
    print(descobrir_quadrante(X, Y))
