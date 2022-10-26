op = input('Qual a operação? ')
valor_1 = int(input('Digite o primeiro valor: '))
valor_2 = int(input('Digite o segundo valor: '))
if op == 'soma':
    s = valor_1 + valor_2
    print(s)
elif op == 'subtração':
    sub = valor_1 - valor_2
    print(sub)
elif op == 'multiplicação':
    mult = valor_1 * valor_2
    print(mult)
elif op == 'divisão':
    div = valor_1 / valor_2
    print(div)

