n = int(input('digite um numero :')) 
for c in range(0,11,1):
    print('\033[1;33m{}\033[m x \033[1;33m{}\033[m = \033[1;32m{}\033[m'.format(n,c,n*c))