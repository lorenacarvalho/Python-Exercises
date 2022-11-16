valores = input().split()

valor1 = int(valores[0])
valor2 = int(valores[1])

A = max(valor1, valor2)
B = min(valor1, valor2)

if A == 0 or B == 0:
    print("Nao eh possivel realizar a operacao com 0")
elif A % B != 0: 
    print("Nao sao Multiplos")
elif A % B == 0:
    print("Sao multiplos")