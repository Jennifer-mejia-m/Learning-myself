my_list = [10, 1, 8, 3, 5]
total = 0
 
for i in my_list:
    total += i
 
print(total)

#ordenamiento burbuja

my_list = [8, 10, 6, 2, 4]  # lista a ordenar
 
for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones
    if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] 

print(my_list) #al imprimir la lista, no va a arrojar la lista ordenada porque no hay un while que le indica que vuelva a repetir el proceso.

my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while. con que se de un solo intercambio, esta variable vuelve a ser true por lo que
                #se mete otra vez en el loop for y vuelve a comparar hasta que ya no haya ningún intercambio, será false y terminará el loop.

while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

#encontrar valores únicos

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

my_list1 = []

for i in range (len(my_list)):
    if my_list[i] not in my_list1:
        my_list1.append(my_list[i])
#
print("La lista con elementos únicos:")
print(my_list1)


