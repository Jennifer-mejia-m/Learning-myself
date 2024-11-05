import time

contar = "Mississippi"
#cuenta = 1, no es necesario crear esta variable, se puede hacer directamente al empezar el for
for cuenta in range(1,6):
    print(cuenta ,"", contar)
# Escribe un bucle for que cuente hasta cinco.
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    # Cuerpo del bucle, emplea : time.sleep(1)
    time.sleep(1)
print("Lista o no, aquí vengo")

#for: Se usa para iterar sobre una colección de elementos, sabiendo cuántas veces se va a ejecutar el bloque de código.

user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()

vocales = "AEIOU"

for letter in user_word: #en este caso el rango viene a ser el contenido de la cadena ingresada?
    if letter in vocales:
        continue
    print(letter)

    
    