def calcular_media(nota1, nota2, nota3):
    return ((nota1*2) + (nota2*3) + (nota3*5)) / 10

def validar(nota1, nota2, nota3):
    if nota1 < 0 or nota2 < 0 or nota3 < 0:
        return False
    elif nota1 > 10 or nota2 > 10 or nota3 > 10:
        return False
    
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

if validar(nota1, nota2, nota3) == False:
    print('Valores incompatíveis')
else:
    media = calcular_media(nota1,nota2,nota3)
    print('MÉDIA = %.1f' %media)
