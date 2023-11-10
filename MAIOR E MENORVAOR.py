resp =''
soma= media=quant= menor=maior=0
while resp in 'sS':
    num = int(input('numero :'))
    soma+=num
    quant+=1
    if num == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num 
    resp = str(input('quer continuar [S/N]')).upper().strip()[0]
media= num / quant 
print('a quantide de numeros é {}\n e a media é {} \n o maior numero é {}\n e o menor é {}'.format(quant,media,maior,menor))
