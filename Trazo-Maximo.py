import numpy as np
import random as rd 
class Juego():
    def __init__ (self,size,tablero):
        self.left = 'Left'
        self.right = 'Right'
        self.up = 'Up'
        self.down = 'Down'
        self.size = size
        self.tablero = tablero
        self.tablero_final = tablero
        self.pos1 = [0,0]
        self.pos2 = [self.size-1,self.size-1]
        self.val1 = self.tablero[0,0]
        self.val2 = self.tablero[self.size-1,self.size-1]
        self.score = self.val1 - self.val2
    
    def validar(self, pos):
        if pos[0] < 0 or pos[0] > self.size-1:
            return False
        elif pos[1] < 0 or pos[1] > self.size-1:
            return False
        elif self.tablero[pos[0],pos[1]] == -1:
            return False
        else:
            return True

    def minimax(self, score, level, player, pos1, direction):
        valD = None
        dirD = None
        valU = None
        dirU = None
        valL = None
        dirL = None
        valR = None
        dirR = None
        if player:
            #valm = self.tablero[pos1[0], pos1[1]]
            if level == 0 or self.tablero[pos1[0],pos1[1]] == - 1:
                return self.tablero[pos1[0], pos1[1]], direction
            #self.tablero[pos1[0], pos1[1]] = - 1   
            if self.validar([pos1[0] + 1, pos1[1]]): #Down
                valD , dirD = self.minimax(score + self.tablero[pos1[0] + 1, pos1[1]] , level -1, False, [pos1[0] + 1, pos1[1]], self.down)
            elif self.validar([pos1[0] - 1,pos1[1]]): #Up
                valU , dirU = self.minimax(score + self.tablero[pos1[0] - 1, pos1[1]] , level -1, False, [pos1[0] - 1, pos1[1]], self.up)
            elif self.validar([pos1[0],pos1[1] - 1]): #Left
                valL , dirL = self.minimax(score + self.tablero[pos1[0], pos1[1] - 1] , level -1, False, [pos1[0], pos1[1] - 1], self.left)
            elif self.validar([pos1[0],pos1[1] + 1]): #Right
                valR , dirR = self.minimax(score + self.tablero[pos1[0], pos1[1] + 1] , level -1, False, [pos1[0], pos1[1] + 1], self.right)
            
            ardir = [valD,valU,valL,valR]
            dirm = [dirD,dirU,dirL,dirR]
            ardir_r = []
            dirm_r = []
            for i in range(len(ardir)):
                if ardir[i] != None:
                    ardir_r.append(ardir[i])
                    dirm_r.append(dirm[i])
            valm = max(ardir_r)
            direction = dirm[ardir_r.index(valm)]
            return valm, direction

        else:
            if level == 0 or self.tablero[self.pos2[0],self.pos2[1]] == - 1:
                return self.tablero[self.pos2[0],self.pos2[1]], direction
            #self.tablero[self.pos2[0],self.pos2[1]] = - 1
            if self.validar([self.pos2[0] + 1,self.pos2[1]]): #Down
                valD , dirD = self.minimax(score - self.tablero[self.pos2[0] + 1,self.pos2[1]] , level -1, True, [self.pos2[0] + 1,self.pos2[1]], self.down)
            elif self.validar([self.pos2[0] - 1,self.pos2[1]]): #Up
                valU , dirU = self.minimax(score - self.tablero[self.pos2[0] - 1,self.pos2[1]] , level -1, True, [self.pos2[0] - 1,self.pos2[1]], self.up)
            elif self.validar([self.pos2[0],self.pos2[1] - 1]): #Left
                valL , dirL = self.minimax(score - self.tablero[self.pos2[0],self.pos2[1] - 1] , level -1, True, [self.pos2[0],self.pos2[1] - 1], self.left)
            elif self.validar([self.pos2[0],self.pos2[1] + 1]): #Right
                valR , dirR = self.minimax(score - self.tablero[self.pos2[0],self.pos2[1] + 1] , level -1, True, [self.pos2[0],self.pos2[1] + 1], self.right)
            
            ardir = [valD,valU,valL,valR]
            dirm = [dirD,dirU,dirL,dirR]
            ardir_r = []
            dirm_r = []
            for i in range(len(ardir)):
                if ardir[i] != None:
                    ardir_r.append(ardir[i])
                    dirm_r.append(dirm[i])
            valm = min(ardir_r)
            direction = dirm[ardir_r.index(valm)]
        return valm, direction

# main
def tablero(size):
    tab = np.random.randint(size*2, size = (size,size))
    return(tab)


tab = tablero(3)
jugar = Juego(3, tab)

print(jugar.minimax(tab[0,0]-tab[2,2],3,True,[0,0],'Down'))





#%% self.Validar function creation process
# pos = [0,2]
# def self.validar(pos, size, self.tablero):
#     if pos[0] < 0 or pos[0] > size-1:
#         return False
#     elif pos[1] < 0 or pos[1] > size-1:
#         return False
#     elif self.tablero[pos[0],pos[1]] == -1:
#         return False
#     else:
#         return True
# tab[1,2] = -1
# print(self.validar(pos,3,tab))
