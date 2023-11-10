#from math import factorial
#n = int(input('digio o numero para fatorial '))
#f =factorial(n)
#print(f)

n = int(input('digt um nmr:  '))
c = n 
f=1
print('CALCULANDO {}! = '.format(n))
while  c > 0:
  print('{} '.format(c), end=' ')
  print(' x ' if c > 1 else ' = ',end='')
  f*=c
  c -= 1
print('{}'.format(f))
  


    