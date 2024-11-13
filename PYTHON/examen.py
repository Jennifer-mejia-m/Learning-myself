my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)

my_list =  [x * x for x in range(5)]

x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z)

print("a", "b", "c", sep="sep")

dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']

for k in range(len(dct)):
    v = dct[v]

print(v)

def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)


print(fun(0, 3))

tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)

dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")

lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")















