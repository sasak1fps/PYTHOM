num = coun = soma = 0
while num != 999:
        num =int(input('numero a dgt '))
        if num ==999:
                break
        soma +=num
        coun +=1
    
print('digitou {}x e a soma e {}'.format(coun,soma))