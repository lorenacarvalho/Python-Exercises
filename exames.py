def calcular_media(nota1, nota2, nota3, nota4):
    return ((nota1*2) + (nota2*3) + (nota3*4) + (nota4*1)) / 10
def validar(nota1, nota2, nota3, nota4):
    if nota1 < 0 or nota2 < 0 or nota3 < 0 or nota4 < 0:
        return False
    elif nota1 > 10 or nota2 > 10 or nota3 > 10 or nota4 > 10:
        return False
def reavaliar(media):
    nota5 = float(input())
    media_atualizada = ((media + nota5) / 2)
    return (media_atualizada, nota5)

lista_notas = []
notas = input().split()
for i in notas:
    lista_notas.append(float(i))
 
nota1 = lista_notas[0]
nota2 = lista_notas[1]
nota3 = lista_notas[2]
nota4 = lista_notas[3]
media = calcular_media(nota1, nota2, nota3, nota4)
mensagem = 'Media: %.1f\n' %media

if media >= 7.0:
    print(mensagem + 'Aluno aprovado.')
elif media < 5.0:
    print(mensagem + 'Aluno reprovado.')
elif media >= 5.0 and media < 7.0:
    print(mensagem + 'Aluno em exame.')
    reavaliacao = reavaliar(media)
    print('Nota do exame: %.1f' %reavaliacao[1])
    media_final = reavaliacao[0]
    if media_final >= 5.0:
        print('Aluno aprovado.\nMedia final: %.1f' %media_final)
    elif media_final < 5.0:
        print('Aluno reprovado.\nMedia final: %.1f' %media_final)
