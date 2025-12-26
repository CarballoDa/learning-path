# ========================
# Procedural style stack 
# ========================


STACK = []

def push(item): # push
    STACK.append(item)

def pop():
    last_item = STACK[-1]
    del STACK[-1]
    return last_item

# Tests


push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())


# ================
# POO style stack
# ================

class Stack:
    # Constructor
    def __init__(self):
        self.__stack_list = [] # Private attr using __
        
        
    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

   
# Tests 

stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())


# ==============================
# POO style stack - inheritance
# ==============================


class ProStack(Stack):
    def __init__(self):
        super().__init__()
        self.__sum = 0
        self.__pop_counter = 0
        self.__push_counter = 0
    
    def push(self, val):
        self.__sum += val
        self.__push_counter += 1
        return super().push(val)
    
    def pop(self):
        val = super().pop()
        self.__sum -= val
        self.__pop_counter += 1
        return val
    
    def get_sum(self):
        return self.__sum
    
    def get_counter(self):
        return self.__pop_counter
        
        
# Tests


stack_object = ProStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())
    
del stack_object
    
stack_object = ProStack()
    
for i in range(100):
    stack_object.push(i)
    stack_object.pop()
print(stack_object.get_counter())