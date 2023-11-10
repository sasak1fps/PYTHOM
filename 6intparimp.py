soma = 0
count = 0
for c in range(6):
    n = int(input(' digite um nmr:  '))
    if n % 2 ==0:
        print('{} + {}'.format(n,n))
        soma = soma + n
        count = count + 1
        print('voce informou {} numreos e a soma é {} '.format(count,soma))

    elif n % 2 ==1:
        print('erro'.format())