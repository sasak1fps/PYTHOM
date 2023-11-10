print('\033[1;33m================LOJAS ALESSANDRO===================\033[m')
produto = float(input('digite o valor do produto :  '))

print('''
\033[1;32m[1] pagamento a vista :
[2] pagamento a vista cartao :  
[3] cartao ate 2x :
[4] cartao  3x ou mais : \033[m''')

opeçao = int(input(' escolha sua forma de pagamento ... '))

if opeçao == 1:
    saldo = produto - (produto * 10 /  100) 
    print('o produto custa \033[1;32m{} \033[m com desconto de 10% .de desconto fica \033[1;32m{}\033[m '.format(produto,saldo))

elif opeçao ==2:
    saldo = produto - (produto * 5 / 100)
    print('o produto custa \033[1;32m{}\033[m com desconto de 5% .de desconto fica \033[1;32m{}\033[m '.format(produto,saldo))

elif opeçao ==3:
    saldo = produto / 2
    print(' o produto custa \033[1;32m{}\033[m e sera parcelado em 2xde \033[1;32m{}\033[m '.format(produto,saldo))

elif opeçao == 4:
    n = int(input('quantas vezes ira parcelar?  '))
    saldo = (produto + (produto * (20 / 100)) ) / n 
    print('o produto custa \033[1;32m{}\033[m  sera parcelado em \033[1;33m{}x\033[m de \033[1;32m{}\033[m '.format(produto, n , saldo) )

else:
    print('\033[1;31mopçao invalida tente novamente!!\033[m')    
