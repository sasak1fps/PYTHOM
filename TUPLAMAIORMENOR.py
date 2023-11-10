from random import randint
n = (randint (1,10),randint (1,10),randint (1,10),randint (1,10),randint (1,10))
print(f'eu sorteei o valor: ' , end='')
for c in n:
    print(f'{c} ',end='' )
print(f' \no maior valor valor:  {max(n)}')
print(f' o menor valor valor:  {min(n)}')