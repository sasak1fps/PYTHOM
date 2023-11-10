num = coun = soma = 0
num =int(input('numero a dgt '))
while num != 999:
        soma +=num
        coun +=1
        num =int(input('numero a dgt '))
print('digitou {}x e a soma e {}'.format(coun,soma))