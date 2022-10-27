ran = int(input('How many numbers will be entered? '))
lista_num = []
for i in range(ran):
    valor = int(input("Type a number: "))
    lista_num.append(valor)

lista_par = []
lista_impar = []
for i in lista_num:
    if (i % 2) == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
print(' The even numbers are: {0}\n The odd numbers are: {1}' 
    .format(lista_par, lista_impar))
