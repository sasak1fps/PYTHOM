def notas(*n , sit=False):
    r = dict()
    r['total'] = len(n)
    r['max'] =   max(n)
    r['min'] =   min(n)
    r['media'] = sum(n)/ len(n)
    if r['media']  >7:
        r['situacao'] = 'BOM'
    elif r['media'] >=5:
        r['situacao'] = 'REGULAR'
    elif r['media'] <5 :
        r['situacao'] = 'RUIM'
    return r

resp = notas(5.5 , 9 , 9, 9)
print(resp)