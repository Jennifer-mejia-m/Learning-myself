dictionary = {"llave":"zorrita","gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

dictionary1 = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for spanish, french in dictionary1.items(): #el resultado indica es una tupla
    print(dictionary1.items())

for spanish, french in dictionary1.items(): #al colocar el nombre de las variables dentro del print, desempaquetamos las tuplas
    print(spanish, "->", french)    

for key in dictionary.keys():
    print(key, "->", dictionary[key])    

for french in dictionary1.values():
    print(french)    

dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']

for k in range(len(dictionary)):
    v = dictionary[v]

print(v)

