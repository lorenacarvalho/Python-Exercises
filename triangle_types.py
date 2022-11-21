import sys
primeira_entrada = input().split()
entrada_float = [float(i) for i in primeira_entrada]

lados_ordenados = sorted(entrada_float, reverse=True)

A = lados_ordenados[0]
B = lados_ordenados[1]
C = lados_ordenados[2]

if A >= B + C:
    print('NAO FORMA TRIANGULO')
    sys.exit()
if A**2 == (B**2) + (C**2):
    print('TRIANGULO RETANGULO')
if A**2 > (B**2) + (C**2):
    print('TRIANGULO OBTUSANGULO')
if A**2 < (B**2) + (C**2):
    print('TRIANGULO ACUTANGULO')
if A == B == C :
    print('TRIANGULO EQUILATERO')
if (A == B != C) or (A != B == C) or (A == C != B):
    print('TRIANGULO ISOSCELES')
        