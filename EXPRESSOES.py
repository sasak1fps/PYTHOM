expr = str(input( ' digite um a expressao:      '))
pilha = []
for sim, in expr:
    if sim == '(':
        pilha.append('(')
    elif sim == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) ==0:
    print('sua expressao e valida')
else:
    print('sua expressao esta errada ')