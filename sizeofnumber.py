x = int(input('digite um nmr :  '))
y = int(input('digite um nmr :  '))
if x < y :
    print(' o numer {} é menor'.format(x))
if y > x :
    print('o numero {} é maior '.format(y))
else:
    print('{} e {} sao iguais'.format(x , y))

a = int(input('digite um nmr :  '))
b = int(input('digite um nmr :  '))
c = int(input('digite um nmr :  '))
menor = a 
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>a:
    maior =b
if c>a and c>b:
    maior =c 
print( 'o menor valor foi {} ' .format(menor))
print('o maior valor foi {}  '.format(maior))