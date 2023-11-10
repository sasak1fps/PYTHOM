matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = mai = scol = 0
for l in  range(0,3):
    for c in range(0,3):
        matriz[l][c]= int(input(f'digite um numero  para [{l} , {c}] '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l] [c]:^4}]', end='')
        if matriz[l][c] %2==0:
            spar += matriz[l][c]
    print() 
print(f'soma dos pares é {spar}')
for l in range(0,3):
    scol +=matriz[l][2]
print(f'a soma da terceira coluna é {scol} ')
for c in range(0,3):
    if c ==0:
        mai = matriz[1][c]
    elif matriz[1][c]>mai:
        mai = matriz[1][c]
print(f'o maior elemento na segunda coluna: {mai}')