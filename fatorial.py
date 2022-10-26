numero = int(input('Type a number: '))
fatorial = numero
contador = 1 
while (numero - contador) > 1:
    fatorial = fatorial * (numero - contador)
    contador += 1
print('The factorial of {0} is: {1}' .format(numero, fatorial))
