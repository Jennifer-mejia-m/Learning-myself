#while: Se usa para repetir un bloque de código mientras una condición sea verdadera. No sabe cuántas veces se ejecutará hasta que se evalúe la condición.

counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

counter = 5 
while counter: # es lo mismo que decir counter != 0 la condición es verdadero y sigue dentro del bucle
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)



# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande.
print("El número más grande es:", largest_number)

###

secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

entrada = int(input("Ingresa un número: "))

while entrada != secret_number:
    print("Ja ja ja! ¡Estás atrapado en mi bucle!")
    entrada = int(input("Ingresa otro número: "))
    
print("Bien hecho muggle")    





