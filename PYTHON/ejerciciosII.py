# Pregunta 1: Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla

for i in range(1, 11):
    if i%2==0:
        continue
    print(i)

#Pregunta 2: Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:

x = 1
while x < 11:
    if x%2==0:
        x+=1
        continue
    print(x)
    x+=1

# Crea un programa con un bucle for y una sentencia break. El programa debe iterar sobre los caracteres en una dirección de correo electrónico, 
# salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")        

#Pregunta 4: Crea un programa con un bucle for y una sentencia continue. El programa debe iterar sobre una cadena de dígitos,
# reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla.    

for digit in "0165031806510":
    if digit == "0":
        digit = "x"
    print(digit, end="")        

for digit1 in "0165031806510":
    if digit1 =="0":
        print("x", end="")
        continue
    print(digit1, end="")
