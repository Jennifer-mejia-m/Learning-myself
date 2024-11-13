#1ft = 0.3048 m
#1inche = 0.0254 m

def ft_and_inch_to_meters(ft,inch = 0.0):
    return ft*0.3048 + inch*0.0254

def lb_to_kg(lb):
    return lb*0.4535923

def bmi(weight,height):
    if height < 1 or height > 2.5 or weight < 20 or weight > 200:
        return False
    return weight/height**2

print(bmi(weight = lb_to_kg(176), height= ft_and_inch_to_meters(5,7)))

# Determinar si es un triángulo rectángulo

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(is_a_triangle(5,3,4))
print(is_a_triangle(1,3,4))


def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return "False"
    if c > a and c > b:
        return c**2 == a**2+b**2
    if b > a and b > c:
        return b**2 == a**2+c**2
    if a > b and a > c:
        return a**2 == b**2+c**2
    
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))    

# Determinando el área de un triángulo con la fórmulo de Herón

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)


print(area_of_triangle(1., 1., 2. ** .5))
print(area_of_triangle(1, 3, 4)) 

# Factoriales

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


for n in range(1, 6):  # probando
    print(n, factorial_function(n))

# Calculando Fibonacci = la suma de los dos números anteriores 

def fib(n):
    if n < 0:
        return False
    if n < 3:
        return 1
    
    elem1 = elem2 = 1
    the_sum = 0

    for i in range (3, n+1):
        the_sum = elem1 + elem2
        elem1, elem2 = elem2, the_sum
    return the_sum

for n in range (1,10):
    print(fib(n))    