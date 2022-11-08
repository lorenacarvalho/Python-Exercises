def calculo (valor_atualizado, indice):
    quantas_notas = 0
    while valor_atualizado >= indice:
        valor_atualizado = valor_atualizado - indice
        quantas_notas += 1
    return (valor_atualizado, quantas_notas)

valor_atualizado = int(input())
valor_atual = valor_atualizado
notas_possiveis = [100, 50, 20, 10, 5, 2, 1]
lista_notasUsadas = []

if valor_atualizado > 0 and valor_atualizado < 1000000:
    print(valor_atualizado)
    for i in range(len(notas_possiveis)):
        cedula = notas_possiveis[i]
        retorno = calculo(valor_atualizado=valor_atual, indice=cedula)
        valor_atual = retorno[0]
        print('{} nota(s) de R$ {},00'.format(retorno[1], notas_possiveis[i]))

else:
    print('Valor Ilegal')
