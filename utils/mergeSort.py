import numpy as np

def mergeMeu(vetor, esquerda, meio, direita):
    n1 = meio - esquerda + 1
    n2 = direita - meio

    vetorEsquerda = np.empty(n1, dtype=vetor.dtype)
    vetorDireita = np.empty(n2, dtype=vetor.dtype)

    for i in range(n1):
        vetorEsquerda[i] = vetor[esquerda + i]
    for j in range(n2):
        vetorDireita[j] = vetor[meio + 1 + j]

    i = 0
    j = 0
    k = esquerda

    while i < n1 and j < n2:
        if vetorEsquerda[i] <= vetorDireita[j]:
            vetor[k] = vetorEsquerda[i]
            i += 1
        else:
            vetor[k] = vetorDireita[j]
            j += 1
        k += 1

    while i < n1:
        vetor[k] = vetorEsquerda[i]
        i += 1
        k += 1

    while j < n2:
        vetor[k] = vetorDireita[j]
        j += 1
        k += 1


def mergeSortRecursivo(vetor, esquerda, direita):
    if esquerda < direita:
        meio = (esquerda + direita) // 2
        mergeSortRecursivo(vetor, esquerda, meio)
        mergeSortRecursivo(vetor, meio + 1, direita)
        mergeMeu(vetor, esquerda, meio, direita)


def mergeSort(vetor):
    if vetor.size > 0:
        mergeSortRecursivo(vetor, 0, vetor.size - 1)

    
