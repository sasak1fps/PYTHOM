lanche  = ('hamburguer ', 'suco' , 'pizza','pudim' ,'batatafrita' )
print(lanche)
print(lanche[1])
print(lanche[1:3])
print(lanche[0:4])

for comida in lanche:
    print(f'eu vou comer {comida}')
print('nhamnhamnham')
for cont in range (0,len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posiçao {cont}')
for pos , comida in  enumerate(lanche):
    print(f'eu vou comer {comida} na posiçao {pos}')

a = (2,5,4)
b=(5,8,1,2)
c= b+a 
d = a +b
print(c)
print(d)