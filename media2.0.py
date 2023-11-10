n1 = float(input('''digite a peimeira nota2:\033[4;32m \033[m'''))
n2 = float(input('''digite a segunda nota:\033[4;32m  \033[m'''))
media = (n1 + n2) / 2

if media >= 7 :
    print('parabens voce passou de ano com media \033[4;32m{}\033[m :'.format(media))
elif media >= 5 and media <7:
    print('voce esta de recuperaçao com media \033[4;31m{}\033[m'.format(media))
elif media < 5:
    print('voce esta reprovadoo!!!!\033[4;35;47m {}\033[m'.format(media))

    s=19 // 2 
    n = 19 %2
    
    print(s,n)