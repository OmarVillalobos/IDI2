#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 17:26:19 2019

@author: omar
"""

#primos = []
#N = 4
#while len(primos) < N:
#    
import random
import queue 

class Nodo:
    def __init__(self, dato = 0 , arr = []):
        self.izq =None
        self.der =None
        self.dato = dato
        self.arr = arr
        self.level_arr = []
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
    
    def imprimir(self):
        if self.dato:
            print(self.dato)
            if self.izq:
                self.izq.imprimir()
            if self.der:
                self.der.imprimir()
    
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
   
    def level(self):
        cola = queue.SimpleQueue()
        cola.put(self)
        while not cola.empty():
            nodo = cola.get()
            print(nodo.dato)
            if nodo.izq:
                cola.put(nodo.izq)
            if nodo.der:
                cola.put(nodo.der) 
        #cola.get()
    def generaramp(self, N):
        prime = []
        for num in range(2,200):
            if all(num%i!=0 for i in range(2,num)):
               prime.append(num)
        
        prime = prime[0:N]
        
        for i in range(len(prime)):
            if i == 0:
                prime_tree = Nodo(prime[i])
            else:
                prime_tree.insertar(prime[i])
        return prime_tree
        
        
#%%
raiz = Nodo()
raiz.generaramp(7).level()

        
#%%
#lista=[random.randrange(1,10) for x in range(20)]
#lista = [1,3,2,4,5,6,7]
##%%
#for i in range(len(lista)):
#    if i == 0:
#        raiz = Nodo(lista[i])
#    else:
#        raiz.insertar(lista[i])
#raiz.tree_navigation()
#
##%%
#
#raiz.find_incidence(7)   
#raiz.find_value_true(2000)
#raiz.find_min_value()
#
#
##%%
#
#raiz.level() 


#%% 

#def encontrarmin(self):
#    print("Estoy en el ",self.dato)
#    ml=1000000
#    mr=1000000
#    if self.left:
#        ml=self.left.encontrarmin()
#    if self.right:
#        mr=self.right.encontrarmin()
#    return min(ml,mr,self.dato)
#
#
#def buscarprof(self,dato):
#    print("Soy el ",self.dato)
#    if self.dato==dato:
#        print("Lo encontré")
#        return True
#    else:
#        if self.left:
#            if self.left.buscarprof(dato):
#                return True
#        if self.right:
#            if self.right.buscarprof(dato):
#                return True