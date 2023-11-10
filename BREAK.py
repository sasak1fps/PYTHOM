n=s=0
while True:
    n=int(input('numero :   '))
    if n == 999:
        break
    s+=n
print(s)

nome = 'jose'
idade = 33
salario = 100
print(f'o {nome} tem {idade}anos e ganha {salario}reais')
print('o {} tem {}anos e ganha {}reais'.format(nome,idade,salario))
print('o %s tem %danos e ganha %dreais' % (nome , idade,salario))