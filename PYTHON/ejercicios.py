#Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide - es plana. La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.
#Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.

#Nota: La altura se mide por el número de capas completas - si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.

#bloques 6 = altura es 3,
#bloques 20 = altura es 5,
#bloques 1000 = altura es 44

blocks = int(input("Ingresa el número de bloques: "))
height = 0

while blocks % 2 = 0:
	

print("La altura de la pirámide:", height)

### SECUENCIA DE COLLATZ

number = int(input("Ingresa un número entero positivo: "))
count = 0 

while number>1:
    print(number)  # Imprime el número actual
    if number % 2 == 0:
        number //= 2  # Si es par, lo divide entre 2
    else:
        number = number * 3 + 1  # Si es impar, aplica 3n + 1
    count += 1  # Incrementa el contador de pasos

# Imprime el último número de la secuencia
print("Pasos:", count)  # Imprime el número de pasos