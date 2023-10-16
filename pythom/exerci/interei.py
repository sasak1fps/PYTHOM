import math 
a = float(input('digite um numero  quebrado : '))
print('o  numero digitado foi {} \n sua parte a redondade  é {} \n sua parte reduzida é  {} \n seu inteiro é {}'.format(a , math.ceil(a) ,  math.floor(a) , math.trunc(a)))