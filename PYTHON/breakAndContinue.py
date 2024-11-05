# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

word = "chupacabra"

soli = input("Ingresa la palabra clave: ")

while soli != word:
    soli = input("ingresa la palabra clave: ")
    if word == soli:
        break

print("Has dejado el bucle con éxito")

#Agregando letras a una variable

word_without_vowels = ""

user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()

vocales = "AEIOU"

for letter in user_word:
    if letter in vocales:
        continue
    word_without_vowels += letter

print(word_without_vowels)
