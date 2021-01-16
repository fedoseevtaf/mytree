#==============================================================#
lenconst = 30
angleconst = 90

#==============================================================#
import turtle as tp

#==============================================================#
tp.left(90)
tp.speed(0)

#==============================================================#

def onetree():
    tp.forward(lenconst)
    tp.backward(lenconst)
    
def tree(n):
    if n == 1:
        onetree()
    else:
        tp.forward(lenconst)
        
        reversetree(n - 1)
        
        tp.right(angleconst)
        
        tree(n - 1)
        
        tp.left(angleconst)
        tp.backward(lenconst)
        

def reversetree(n):
    if n == 1:
        onetree()
    else:
        tp.forward(lenconst)
        
        tree(n - 1)
        
        tp.left(angleconst)
        
        tree(n - 1)
        
        tp.right(angleconst)
        tp.backward(lenconst)


def t(n):
    if n == 1:
        return 1
    else:
        return 1 + (2 * (t(n - 1)))

def o(n):
    #if n == 1:
        #return 1
    #else:
        #return 2 * (o(n - 1))
    
    return 2 ** (n - 1)

tree(7)
