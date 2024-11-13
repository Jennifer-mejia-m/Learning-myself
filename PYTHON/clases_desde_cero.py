#se crea una clase y un objeto que es one_persona(se instancia un objeto)

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

one_persona = Persona ("Janko", 3)

#print(one_persona.nombre)
#print(one_persona.edad)

# crea una subclase de Persona no se sobreescribe el método init, hereda lo de Persona

class Estudiante(Persona):
    pass

# crea una subclase sobreescribiendo el método init

class Universitario(Persona):
    def __init__(self, nombre, matricula, universidad): #agrego todos los atributos que tendrá el objeto
        Persona.__init__(self, nombre) #con sus atributos originales de la clase base
        self.matricula = matricula
        self.universidad = universidad

universitario1 = Universitario ("Carlos",3, "hjgjh567", "uladech")       

print(universitario1.matricula)
print(universitario1.nombre)
print(universitario1.universidad)

# otro modelo de subclase, donde la clase se inició sin parámetros y por eso no se trabaja como el ejemplo anterior de Universitario(Persona)

class Stack:
    def __init__(self): #el constructor se ha inicializado sin parámetros
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
    
class AddingStack(Stack): #la subclase se está construyendo sin parámetros, solo indica los atributos con los que inicializa
    def __init__(self):
        Stack.__init__(self) 
        self.__sum = 0    

#no entiendo
class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2
 
 
example_object = ExampleClass()
 
print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))        





