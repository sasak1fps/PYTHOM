while True:
    nume=int(input('tabuada de qual valor :      '))
    if nume <0:
            break
    print('\033[1;34m-\033[m'*30)
    for c in range(0,10):
        c+=1
        print(f'\033[1;32m{nume}\033[m \033[1;31mx\033[m \033[1;32m{c}\033[m \033[1;31m=\033[m \033[1;32m{nume*c}\033[m')
    print('\033[1;34m-\033[m'*30)
print('acabou')