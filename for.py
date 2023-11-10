for c in range(1,10):
    print('\033[1;32mhello world\033[m')

for c in range(1,10):
      print('\033[1;32m {} \033[m'.format(c))

i= int(input('incio'))
p= int(input('passo')) 
f= int(input('fim'))
for c in range(10,0,-1 ): 
      print('\033[1;32m {} \033[m'.format(c))

for c in range(i,f+1,p ): 
    print('\033[1;32m {} \033[m'.format(c))
    if f == 0:
     print('fim')


for n in range(0,10,3):
    print (n)  