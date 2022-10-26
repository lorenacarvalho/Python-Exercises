valor_1 = int(input('Type the first value: '))
valor_2 = int(input('Type the second value: '))
op = input('Which operation? ')
if op == 'sum':
    s = valor_1 + valor_2
    print(s)
elif op == 'sub':
    sub = valor_1 - valor_2
    print(sub)
elif op == 'multi':
    mult = valor_1 * valor_2
    print(mult)
elif op == 'div':
    div = valor_1 / valor_2
    print(div)
else: 
    print('This operation is invalid')
