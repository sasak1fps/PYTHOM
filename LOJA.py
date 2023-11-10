print('-'*20)
print('LOJA BARATAO')
print('-'*20)
tot = totmil = maior = menor=  cont =0
barato = ' '
while True:
    produto = str(input('digite o nome do produto  '))
    preço = float(input('digite o valor do produto  '))
    cont+=1
    tot += preço
    if preço> 1000:
        totmil +=1
    if cont ==1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar [S/N]  ').upper().strip()[0])
    if resp == 'N':
        break


print(f'preço total: {tot}')
print(f'preço acima de mil: {totmil}')
print(f'o produto mais barato é {barato} custa {menor} ')