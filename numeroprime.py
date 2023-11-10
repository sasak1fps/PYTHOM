n=int(input('dgt nmr primo:   '))
p = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m ',end=' ')
        p+=1
    else:
        print('\033[31m', end=' ')
        print('{}'.format(c), end=' ')
print('\033[m o numero {} foi divisivel {} '.format(n,p))
if p == 2:
        print('E PRIMO')
else:
        print('NAO È PRIMO')
