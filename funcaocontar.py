from time import sleep
def contar_numeros(inicio, fim, passo):
    if inicio < fim:
        numero_atual = inicio
        while numero_atual < fim:
            print(numero_atual , flush=True)
            sleep(0.5)
            numero_atual += passo

    elif inicio > fim:
        numero_atual = inicio
        while numero_atual > fim:
            print(numero_atual ,  flush=True)
            sleep(0.5)
            numero_atual -= passo


contar_numeros(1,10,1)
contar_numeros(10,0,2)
# Input
print('sua vez de escolher os valores')
inicio = int(input('Qual o número inicial: '))
fim = int(input('Qual o número final: '))
passo = int(input('Qual o número de passos: '))

# Function call
contar_numeros(inicio, fim, passo)
