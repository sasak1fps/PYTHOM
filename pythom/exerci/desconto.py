produto = float(input('digite o preço do produto '))
desconto = float(input('digite o desconto '))
des= produto * (desconto / 100)
tot = produto - des 
print(' o valor do produto é  {}  e com descondo de  {}%  , o novo valor sera de  {}  '.format(produto, desconto  , tot ))

p = float(input('digite o valor do p '))
d = float(p -  p * (5 / 100) )
print('o produto custa {}  com {}% ,de desconto  o novo valor é {} '.format(p , 5 , d ))