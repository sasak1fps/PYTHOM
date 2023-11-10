print('===================================')
print('                 PA                ')
print('===================================')
n = int(input('primeiro termo:  '))
ultimo = int(input('ultimo termo:  '))
r = int(input('RAZAO  '))
for c in range(n,ultimo,r):
    print('{}'.format(c), end=' -> ')