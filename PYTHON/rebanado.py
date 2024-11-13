my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
new_list1 = my_list[1:]
print(new_list)
print(new_list1)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")

