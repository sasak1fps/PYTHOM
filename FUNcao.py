def soma(a,b):
    s = a + b ;
    print(s);

soma(1,2);
soma(8,9);
soma(4,5);

def cont(*num):
    print(num)
cont(1,7,6,4,7,9);
cont(13,4,5);
cont(0);


def dobra(lista):
    pos=0
    while pos <len(lista):
        lista[pos]*=2
        pos+=1
valores = [6,3,9,1,0,2];
dobra(valores);
print(valores);