n = int(input('digite a sua velocidade  '))
if n >=80: 
    print('voce foi multado em {} !! '.format(( n - 80 ) * 7 ) )
else:
    print('voce nao foi multado')