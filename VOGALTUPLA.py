palavras = ('aprender' , 'progrmar', 'linguagem', 'pythom','curso','gratis','estudar','praticar','trabalhar','mercado','programar','futuro')
vogal = ( 'a' , 'e' , 'i' ,'o' , 'u')
for p in palavras:
    print(f'\n na palavra  \033[1;32m{p}\033[m temos '  , end='')
    for letras in p:
        if letras in 'aeiou':
            print(f'\033[1;31m{letras}\033[m ' , end=' ')