import random
import time

# Função para ordenar com o algoritmo Bubble Sort
def bubble_sort(lista): 
    n = len(lista)
    for i in range(n-1):
        for j in range(n-i-1):
            if(lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1],lista[j]

# Função para ordenar com o algoritmo Selection Sort
def selection_sort(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

# Função para ordenar com o algoritmo Insertion Sort
def insertion_sort(lista):
    for i in range(1, len(lista)):
        n = lista[i]
        j = i - 1
        while j >= 0 and n < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = n

# Função para ordenar com o algoritmo Merge Sort
def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        L = lista[:meio]
        R = lista[meio:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1

# Função para medir o tempo de execução dos algoritmos de ordenação
def get_time(tamanho):
    bubble_tempo = []
    selection_tempo = []
    insertion_tempo = []
    merge_tempo = []

    for _ in range(3):
        lista = list(range(1, tamanho+1))
        random.shuffle(lista)
        inicio = time.time()
        bubble_sort(lista.copy())
        fim = time.time()
        tempo_bubble = fim - inicio
        bubble_tempo.append(tempo_bubble)

        lista = list(range(1, tamanho+1))
        random.shuffle(lista)
        inicio = time.time()
        selection_sort(lista.copy())
        fim = time.time()
        tempo_selection = fim - inicio
        selection_tempo.append(tempo_selection)

        lista = list(range(1, tamanho+1))
        random.shuffle(lista)
        inicio = time.time()
        insertion_sort(lista.copy())
        fim = time.time()
        tempo_insertion = fim - inicio
        insertion_tempo.append(tempo_insertion)

        lista = list(range(1, tamanho+1))
        random.shuffle(lista)
        inicio = time.time()
        merge_sort(lista.copy())
        fim = time.time()
        tempo_merge = fim - inicio
        merge_tempo.append(tempo_merge)

    return bubble_tempo, selection_tempo, insertion_tempo, merge_tempo

# Loop para executar o código três vezes
for i in range(3):
    tamanho = int(input(f'Digite o tamanho da lista: '))

    bubble_tempo, selection_tempo, insertion_tempo, merge_tempo = get_time(tamanho)
    print(f'Rodada {i+1}:')
    print(f'Tempo de ordenação com Bubble Sort: {bubble_tempo[0]:.2f} segundos')
    print(f'Tempo de ordenação com Selection Sort: {selection_tempo[0]:.2f} segundos')
    print(f'Tempo de ordenação com Insertion Sort: {insertion_tempo[0]:.2f} segundos')
    print(f'Tempo de ordenação com Merge Sort: {merge_tempo[0]:.2f} segundos')
    print('-' * 30)