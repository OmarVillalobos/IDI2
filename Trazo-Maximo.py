import numpy as np
import random as rd 
class Juego():
    def __init__ (self,size):
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.size = size
        self.score = 0
        self.pos1 = [0,0]
        self.pos2 = [self.size-1,self.size-1]
        self.val1 = 0
        self.val2 = 0



    def insertar(self):
        if self.score:
            if self.izq is None:
                self.izq = Nodo(dato)
            elif self.der is None:
                self.der = Nodo(dato)
            else:
                self.izq.insertar(dato)
        else:
            self.dato=dato 
    def tablero(self):
        tab = np.random.randint(self.size*2, size = (self.size,self.size))
        return(tab)
    def minimax(self, level):
        if 

        return value, pos

jugar = Juego(3)
tabl = jugar.tablero()
print(tabl)
print(tabl[0,0])
