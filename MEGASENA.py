from random import randint
from time import sleep
print(f'-='*30)
print(f'{"MEGA SENA":^60}')
print(f'-='*30)
tot = 1
quant = int(input('quantos jogas gostaria de sortear?  '))
lista = list()
jogos = list()

while tot <= quant:
    cont =0 
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print(f'-=*3' f'SORTEANDO {quant} JOGos' , '-='*3 )
for i , l in enumerate(jogos):
    print(f'jogo {i+1}:{l}')
    sleep(1)