def calcular_perimetro(lado1, lado2, lado3):
    return lado1 + lado2 + lado3
def calcular_area(base1, base2, altura):
    area = ((base1 + base2) * altura)/2
    return area 

primeira_entrada = input().split()
entrada_float = []

for i in primeira_entrada:
    entrada_float.append(float(i))

lados_ordenados = sorted(entrada_float)

A = lados_ordenados[0]
B = lados_ordenados[1]
C = lados_ordenados[2]

if (A + B) > C:
    print('Perimetro = %.1f' %calcular_perimetro(lado1=A, lado2=B, lado3=C))
else:
    print('Area: %.1f' %calcular_area(base1=entrada_float[0], 
    base2=entrada_float[1], altura=entrada_float[2]))