'''
TO DO
1) FUNÇÃO PARA IMPRIMIR OS NÚMEROS PARES DA LISTA
2) FUNÇÃO PARA IMPRIMIR OS NÚMEROS ÍMPARES DA LISTA
3) FUNÇÃO PARA SEPARAR EM UMA NOVA LISTA OS ELEMENTOS PARES
4) FUNÇÃO PARA SEPARAR EM UMA NOVA LISTA OS ELEMENTOS ÍMPARES
5) FUNÇÃO PARA VERIFICAR SE UM NÚMERO ESTÁ CONTIDO NA LISTA
'''




def tamanho_lista():
    print('*- TAMANHO DA LISTA -*')
    t = int(input('Tamanho: '))
    return t

def criar_lista(t):
    print('*- CRIAR UMA LISTA -*')
    print('---------------------')
    lista = []
    i=0
    while i<t:
        n = int(input('Número: '))
        lista.append(n)
        i+=1
    return lista


def imprimir(lista):
    print(' *- IMPRIMINDO A LISTA -*')
    print('-------------------------')
    for i in lista:
        print('------------------------')
        print('Elemento: ' , i)

#Principal
t = tamanho_lista()
lista = criar_lista(t)
imprimir(lista)