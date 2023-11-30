
def fatorial(num=1):
    f=1
    for c in range(num,0,-1):
        f*=c
    return f 
n = int(input('digite um nmr:   ' ))
print(f' o fatorial de {n} é  {fatorial(n) } ' , sep='string')
import FUNCAOFATORIAL2