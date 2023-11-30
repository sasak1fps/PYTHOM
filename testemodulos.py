from moodulos import moedas
from moodulos import dados
        #beforeex108
#p = float(input('digite o preco :  R$' ))
#print(f' a metade de {moedas.moedas(p)} é {moedas.moedas(moedas.metade(p))}')
#print(f' a aumentando de {moedas.moedas(p)} é {moedas.moedas(moedas.aumentar(p , 10))}')
#print(f' diminuindo de {moedas.moedas(p)} é {moedas.moedas(moedas.diminuir(p , 10))}')
#print(f' o dobro de {moedas.moedas(p)} é {moedas.moedas(moedas.dobro(p))}')



#p = float(input('digite o preco :  R$' ))
p = dados.leiadinheiro('digite o preco : R$')
print(f' a metade de {moedas.moedas(p)} é {moedas.metade(p,True)}')
print(f' o dobro de {moedas.moedas(p)} é {moedas.dobro(p,True)}')
print(f' a aumentando em 13% {moedas.moedas(p)} é {moedas.aumentar(p , 13,True)}')
print(f' diminuindo em 13% {moedas.moedas(p)} é {moedas.diminuir(p , 13,True)}')
print(f'{moedas.resumo(p,10,5)}')

