'''
-> calcula o aumento de um determinado preco,
retornando o  resultado com ou sem formatação
;param preco: o preco que se  quer reajustar
;param taxa: qual é a porcentagem  do aumento
;param formato: quer saida formatada ou nao
;return o valor reajustado , com ou sem formataçao
'''

def aumentar(preco=0,taxa=0, formato=False):
        res= preco + (preco * taxa/100)
        return res if formato is False else moedas(res)

def diminuir(preco=0 , taxa=0,formato=False):
        res = preco - (preco * taxa/100)
        return res   if formato is False else moedas(res)

def dobro( preco=0,formato=False):
        res = preco * 2
        return res if formato is False else moedas(res)

def metade(preco= 0,formato=False):
        res = preco / 2
        return res if formato is False else moedas(res)

def moedas(preco= 0 , moedas= 'R$' ):
        return f'{moedas}{preco:>.2f}' .replace('.' , ',')

def resumo(preco=0,taxaa=10 , taxar=5):
        print('~'*30)
        print('resumo do valor ' .center(30)) 
        print('~'*30)
        print(f'preco analisado:  \t{moedas(preco)}')
        print(f'COM AUMENTO:  \t{aumentar(preco , 10,True)}') 
        print(f'COM DESCONTO:  \t{diminuir(preco,10,True)}')
        print(f'O DOBRO È:  \t{dobro(preco,True)}')
        print(f'A METADE È:  \t{metade(preco,True)}')

        