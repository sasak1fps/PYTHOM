n = float(input('qual a distancia da sua viagem :  '))
print('voce esta fazendo uma viagem de {}km'.format(n))
if  n <= 200:
    print('o valor da viagem é {:.2f}R$  '.format(n * 0.50))
else:
    print('o valor da viagem é {:.2f}R$  '.format (n * 0.45))
