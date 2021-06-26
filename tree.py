import turtle as tp


LEN: int = 30
ANGLE: int = 90

tp.left(90)
tp.speed(0)


def main() -> None:
    tree(7)


def onetree() -> None:
    tp.forward(LEN)
    tp.backward(LEN)


def tree(n: int=1) -> None:
    if n == 1:
        onetree()
        return
    tp.forward(LEN)   
    reversetree(n - 1)   
    tp.right(ANGLE)   
    tree(n - 1)  
    tp.left(ANGLE)
    tp.backward(LEN)
        

def reversetree(n: int=1) -> None:
    if n == 1:
        onetree()
        return
    tp.forward(LEN)
    tree(n - 1)  
    tp.left(ANGLE) 
    tree(n - 1) 
    tp.right(ANGLE)
    tp.backward(LEN)


def t(n: int=1) -> int:
    if n == 1:
        return 1
    return 1 + (2 * (t(n - 1)))


def o(n: int=1) -> int:
    '''\
    if n == 1:
        return 1
    return 2 * (o(n - 1))
    '''
    
    return 2 ** (n - 1)
    # 2 ** (1 - 1) == 1


main()
