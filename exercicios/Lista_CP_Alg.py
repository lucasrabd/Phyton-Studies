import random
import time

# Função para ordenar com o algoritmo Bubble Sort
def bubble_sort(lista): 
    """
    Função para ordenar a lista usando o algoritmo Bubble Sort.

    Parâmetros:
        lista (list): A lista a ser ordenada.

    Retorna:
        None: A lista é ordenada in-place.
    """
    n = len(lista)
    for i in range(n-1):
        for j in range(n-i-1):
            if(lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Função para ordenar com o algoritmo Selection Sort
def selection_sort(lista):
    """
    Função para ordenar a lista usando o algoritmo Selection Sort.

    Parâmetros:
        lista (list): A lista a ser ordenada.

    Retorna:
        None: A lista é ordenada in-place.
    """
    for i in range(len(lista)):
        min_index = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

# Função para ordenar com o algoritmo Insertion Sort
def insertion_sort(lista):
    """
    Função para ordenar a lista usando o algoritmo Insertion Sort.

    Parâmetros:
        lista (list): A lista a ser ordenada.

    Retorna:
        None: A lista é ordenada in-place.
    """
    for i in range(1, len(lista)):
        n = lista[i]
        j = i - 1
        while j >= 0 and n < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = n

# Função para ordenar com o algoritmo Merge Sort
def merge_sort(lista):
    """
    Função para ordenar a lista usando o algoritmo Merge Sort.

    Parâmetros:
        lista (list): A lista a ser ordenada.

    Retorna:
        None: A lista é ordenada in-place.
    """
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
    """
    Função para medir o tempo de execução dos algoritmos de ordenação.

    Parâmetros:
        tamanho (int): O tamanho da lista a ser ordenada.

    Retorna:
        tuple: Uma tupla contendo as listas de tempos de execução para Bubble Sort, Selection Sort, Insertion Sort e Merge Sort, respectivamente.
    """
    bubble_tempo = []
    selection_tempo = []
    insertion_tempo = []
    merge_tempo = []

    # Executa cada algoritmo de ordenação três vezes para obter uma média do tempo de execução
    for _ in range(3):
        lista = list(range(1, tamanho+1))  # Cria uma lista ordenada
        random.shuffle(lista)  # Mistura a lista para torná-la aleatória
        inicio = time.time()  # Marca o tempo de início da ordenação
        bubble_sort(lista.copy())  # Ordena a lista usando Bubble Sort e calcula o tempo de execução
        fim = time.time()  # Marca o tempo de fim da ordenação
        tempo_bubble = fim - inicio  # Calcula o tempo de execução do Bubble Sort
        bubble_tempo.append(tempo_bubble)  # Adiciona o tempo de execução à lista de tempos

        # Repete o mesmo processo para os outros algoritmos de ordenação (Selection Sort, Insertion Sort e Merge Sort)

    return bubble_tempo, selection_tempo, insertion_tempo, merge_tempo

# Loop para executar o código três vezes
for i in range(3):
    tamanho = int(input(f'Digite o tamanho da lista: '))

    # Obtém os tempos de execução dos algoritmos de ordenação para a lista de tamanho especificado
    bubble_tempo, selection_tempo, insertion_tempo, merge_tempo = get_time(tamanho)

    # Imprime os tempos de execução médios de cada algoritmo para a rodada atual
    print(f'Rodada {i+1}:')
    print(f'Tempo de ordenação com Bubble Sort: {bubble_tempo[0]:.2f} segundos')
    print(f'Tempo de ordenação com Selection Sort: {selection_tempo[0]:.2f} segundos')
    print(f'Tempo de ordenação com Insertion Sort: {insertion_tempo[0]:.2f} segundos')
    print(f'Tempo de ordenação com Merge Sort: {merge_tempo[0]:.2f} segundos')
    print('-' * 30)
