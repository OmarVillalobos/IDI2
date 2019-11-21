import random


class Nodo:
    def __init__(self, dato =0, arr = []):
        self.izq =None
        self.der =None
        self.dato = dato
        self.arr = arr
    def insertar(self, dato):
        if self.dato:
            if self.izq is None:
                self.izq = Nodo(dato)
            elif self.der is None:
                self.der = Nodo(dato)
            else:
                self.izq.insertar(dato)
        else:
            self.dato=dato 

    def tree_navigation(self):
        if self.dato:
            self.arr.append(self.dato)
            if self.izq:
                self.izq.tree_navigation()
            if self.der:
                self.der.tree_navigation()
    
    def find_value_true(self,search):
        return print(search in self.arr)
    
    def find_incidence(self, incidence):
        if incidence in self.arr:
            matches = [x for x in self.arr if x == incidence]
            return print('incidence = {0}'.format(len(matches)))
        else:
            print('no incidence')
    
    def find_min_value(self):
       return print('Min Value is  = {0}'.format(min(self.arr)))



#%%
#  main 
lista=[random.randrange(1,10) for x in range(20)]
#%%
for i in range(len(lista)):
    if i == 0:
        raiz = Nodo(lista[i])
    else:
        raiz.insertar(lista[i])
raiz.tree_navigation()

#%%

raiz.find_incidence(7)   
raiz.find_value_true(2000)
raiz.find_min_value()