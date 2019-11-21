class Nodo:
    def __init__(self, dato = 0):
        self.izq = None
        self.der = None
        self.dato = dato

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

    def imprimir(self):
        if self.dato:
            print(self.dato)
            if self.izq:
                self.izq.imprimir
            if self.der:
                self.der.imprimir
            

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sorted_array_to_bst(nums):
    
    if not nums:
        return None
    mid_val = len(nums)//2
    node = TreeNode(nums[mid_val])
    node.left = sorted_array_to_bst(nums[:mid_val])
    node.right = sorted_array_to_bst(nums[mid_val+1:])
    return node

def preOrder(node): 
    if not node: 
        return      
    print(node.val)
    preOrder(node.left) 
    preOrder(node.right)   
    
result = sorted_array_to_bst([1, 2, 3, 4, 5, 6, 7])
preOrder(result)

raiz = Nodo()
raiz.insertar(3)
raiz.imprimir()
print(raiz)


raiz = TreeNode()
result = raiz.sorted_array_to_bst([1, 2, 3, 4, 5, 6, 7])
node = preOrder(result)