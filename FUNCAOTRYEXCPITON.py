
def leiaint(msg):
  

 while True:
    try:
         n = int(input(msg))
    except(ValueError,TypeError):
         print('\033[0;31mERRO, digite um numero valido \033[m')
         continue
    except(KeyboardInterrupt):
        print(f'\033[0;33m USUARIO INTERROMPEU A EXECUCAO DO PROGRAMA \033[m')
        return 0
    else:
            return n 
def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError,TypeError):
            print(f'\033[0;31m ERRO DIGITE UM NUMERO VALIDO\033[0;31m')
        except(KeyboardInterrupt):
            print('\033[0;33m O USUARIO NAO FINALIZOU O PROGRAMA \033[m')
            return 0 
        else:
            return n 
num = leiaint('digite um numero  inteiro')
print(f'voce digitou o numero inteiro {num} ')
num1 = leiafloat('digite um numero real ')
print(f'voce digitou o numero real {num1} ')



