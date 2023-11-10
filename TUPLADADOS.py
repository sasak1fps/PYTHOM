num = (int(input('digite um nmr :     ')) , int(input('digite um nmr :     ')) , int(input('digite um nmr :     ')), int(input('digite um nmr :     ')))
print(f'voce digitou os valores {num}')
print(f'o valor 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'o numer 3 aparecena posicao {num.index(3)}')
else:
    print('o valor 3 nao foi digitado')
for n in num:
    if n % 2 ==0:
        print(f'{n}' , end=' ')