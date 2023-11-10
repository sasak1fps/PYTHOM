listanum = []
mai = men = 0
for c in range (0,5):
    listanum.append(int(input(f'digite um valor para posiçao {c}:  ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c] 

print(f'voce digitou {listanum} ')
for i  ,v in enumerate(listanum):
    if v == mai:
        print(f'o maior valor é {mai} nas posiçoes {i} ' , end=' ')
    elif v == men:
        print(f' \n o menor valor é {men} nas posiçoes  {i} ' , end=' ')
