def message():
    print("Ingresar valor: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

def introduction(first_name, last_name="Smith"):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Jorge", "Perez")
introduction("Yanina")

