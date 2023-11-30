def fatorial(n , show = False):

    """  
        -> CALCULA FATORIAL DE UM NUMERO
        ;param n : O numero a ser calculado
        ;param show: (opcional)  mostra ou nao a conta
        ;return: o valor do fatorial de um numero n   
    """    


    f=1
    for cont in range(n,0,-1):
        if show:
            print(cont , end='')
            if cont>1:
                print(f' x ' , end='')
            else:
                print(' = ' ,end='')
        f*=cont
    return f
print(fatorial(int(input('dgt o fatorial ')), show = True) )
help(fatorial)