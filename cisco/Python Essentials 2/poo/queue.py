"""
Una cola (queue) es un modelo de datos caracterizado por el término FIFO: primero en entrar, primero en salir.
Nota: una cola (fila) regular que conozcas de las tiendas u oficinas de correos funciona exactamente de la
misma manera: un cliente que llegó primero también es el primero en ser atendido.
"""

class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        """
        Con un solo guion sigue siendo atributo privado, 
        pero ahora si que será accesible desde cualquier subclase.
        """
        self._stack_list = []
        
    def put(self, item):
        self._stack_list.insert(0, item)
        
    def get(self):
        if len(self._stack_list) == 0:
            raise QueueError("Error: lista vacía.")
        val = self._stack_list[-1]
        del self._stack_list[-1]
        return val
        
        
"""que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")"""
    
    
class SuperQueue(Queue):
    def isempty(self):
        return len(self._stack_list) == 0
    
que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")