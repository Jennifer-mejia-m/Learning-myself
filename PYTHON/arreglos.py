squares = [x ** 2 for x in range(10)]
print(squares)

temps = [[0.0 for h in range(3)] for d in range(4)]
print(temps)

rooms = [[[False for r in range(3)] for f in range(4)] for t in range(3)]
print(rooms)

var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")

t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += t[i][i] #el primer[1] hace referencia al índice de general, el 2do[] referencia a lo que está dentro del índice
    print(t)
print(s)



