tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    # salida: 4

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

#Pregunta 5: Escribe un programa que convierta la lista my_list en una tupla.

my_list = ["car", "Ford", "flower", "Tulip"]
t =  tuple(my_list)
print(t)

#Pregunta 6: Escribe un programa que convierta la tupla colors en un diccionario.
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary=dict(colors)

print(colors_dictionary)

