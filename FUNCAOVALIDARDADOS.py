def leiaint(msg):
    ok =False
    valor = 0
    while True:
        n= str(input(msg))
        if n.isnumeric():
            valor= int(n)
            ok=True
        else:
            print('\033[0;31m ERRO DIGITE NMR VALIDO\033[m')
        if ok:
            break
    return valor

n = leiaint('digite um numero ')
print(f'voce acabou de  digitar numero ')



