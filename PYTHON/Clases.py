class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack): #subclase
    def __init__(self):        #constructor
        Stack.__init__(self)    #siempre hay q llamar al constructor de la superclase
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def pop(self):
        self.__counter += 1
        return self.__counter
	

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())