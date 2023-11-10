peso = float(input('digite seu peso :  '))
altura = float(input('digite sua altura : '))
imc =peso / (altura**2) 
print('seu IMC È {}'.format(imc))

if imc < 18.5:
    print('\033[1;31mmagro\033[m')

elif imc <= 18.5  < 25:
    print('\033[1;31mbom\033[m')

elif imc <= 25 and imc < 30:
    print('\033[1;32m sobre peso\033[m')

elif imc <= 30 and imc < 40:
    print('\033[1;31mobeso\033[m')

elif imc >40:
    print('\033[1;31mobesidade morbida\033[m ')
