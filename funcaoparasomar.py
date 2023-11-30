from random import randint
from time import sleep

def sorteia(list):
    for cont in range (0,5):
        n= randint(1,10)
        list.append(n)
        print(f' { n } ' , end=' ' , flush=True)
        sleep(0.3)
        
def somapar(list):
    soma= 0 
    for valor in list:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando valores pares de {list} , temos {soma} ')        


numeros = list()

sorteia(numeros)
somapar(numeros)