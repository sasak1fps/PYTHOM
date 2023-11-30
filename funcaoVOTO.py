def voto():
    from datetime import date
    anoatual = date.today().year
    nascimento = int(input('em que ano voce nasceu '))
    idade = anoatual - nascimento  
    if idade <16:
        return(f' Com {idade}   NAO VOTA')
    elif 16<= idade <18 or idade >65:
        return(f' Com {idade}  VOTO OPCIONAL ')
    else:
        return(f' COM {idade} VOTO OBRIGATORIO')
print(voto())