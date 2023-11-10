print('='*30)
print(f'{"Lojas TUPLAS":^30}')
print('='*30)
listagem = ('lapis ' , 1.75     ,   'borracha' , 2  ,'caderno', 15.90 ,'estojo',25  ,'transferidor' , 4.20  , 'compasso' ,9.99  , 'mochila', 120.32  , 'canetas' ,  22.30 , 'livro' ,  34.90)
for pos in range(0 , len(listagem)):
    if pos %2==0:
      print(f'{listagem[pos]:.<30}', end='')
    else:
      print(f'\033[1;32mR${listagem[pos]:>7.2f}\033[m')