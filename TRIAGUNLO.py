r1 = float(input('primerio segmento '))
r2 = float(input('segundo segmento  '))
r3 = float(input('terceiro segmento '))
if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r2+r1:
    print('os segmentos formas um triangulo')
    if r1 == r2 ==r3:
        print('\033[32mEQUILATERO\033[m')
    elif r1!=r2!=r3!=r1:
        print('\033[32mESCALENO\033[m')
    else:
        print('\033[32mISOSCELES\033[m')
else:
    print('os segmentos nao formam um triangulo')