#if: Se usa para ejecutar diferentes bloques de código basados en condiciones específicas, permitiendo la toma
#de decisiones en el flujo del programa.

number1 = int(input("Ingresa un número: "))
number2 = int(input("Ingresa un número: "))
number3 = int(input("Ingresa un número: "))

largeNumber = number1

if largeNumber < number2:
    largeNumber = number2
if largeNumber < number3:
    largeNumber = number3

print(largeNumber)

entrada = input("Ingresa el nombre de una plata: ")

if entrada == "ESPATIFILIO":
    print("Si, es la mejor plata del mundo")
elif entrada == "Espatifilio":
    print("No, esa no es la que quiero")
else:
    print("ESPATIFILIO! no "+ entrada)