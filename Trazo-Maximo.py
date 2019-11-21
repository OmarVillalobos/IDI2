import numpy as np
import random as rd 
class Juego():
    def __init__ (self,size,tablero):
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.size = size
        self.tablero = tablero
        self.pos1 = [0,0]
        self.pos2 = [self.size-1,self.size-1]
        self.val1 = self.tablero[0,0]
        self.val2 = self.tablero[self.size-1,self.size-1]
        self.score = self.val1 - self.val2
    
    def validar(self, pos):
        if pos[0] < 0 or pos[0] > size-1:
            return False
        elif pos[1] < 0 or pos[1] > size-1:
            return False
        elif self.tablero[pos[0],pos[1]] == -1:
            return False
        else:
            return True



#     def insertar(self):
#         if self.score:
#             if self.izq is None:
#                 self.izq = Nodo(dato)
#             elif self.der is None:
#                 self.der = Nodo(dato)
#             else:
#                 self.izq.insertar(dato)
#         else:
#             self.dato=dato 

     def minimax(self, level):
         
    
         return value, pos

jugar = Juego(3)


# main
def tablero(size):
    tab = np.random.randint(size*2, size = (size,size))
    return(tab)
tab = tablero(3)
print(tab)

#%% Validar function creation process
pos = [0,2]
def validar(pos, size, tablero):
    if pos[0] < 0 or pos[0] > size-1:
        return False
    elif pos[1] < 0 or pos[1] > size-1:
        return False
    elif tablero[pos[0],pos[1]] == -1:
        return False
    else:
        return True
tab[1,2] = -1
print(validar(pos,3,tab))
