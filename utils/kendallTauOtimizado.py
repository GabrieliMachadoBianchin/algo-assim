#utils/kendallTauOtimizado.py
"""
Apenas preve casos do Kendall Tau-a, ou seja, ignora empates
"""

def contaInversao(vetor):
    def mergeSort(vetor2):
        if len(vetor2) <= 1:
            return vetor2, 0

        meio = len(vetor2) // 2
        esquerda, inversaoEsquerda = mergeSort(vetor2[:meio])
        direita, inversaoDireita = mergeSort(vetor2[meio:])
        intercalado, mergeInversao = merge(esquerda, direita)

        return intercalado, inversaoEsquerda + inversaoDireita + mergeInversao
    
    def merge(esquerda, direita):
        resultado = []
        i = j = inversao = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] <= direita[j]:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                inversao += len(esquerda) - i
                j +=1

        resultado.extend(esquerda[i:])
        resultado.extend(direita[j:])
        return resultado, inversao
    
    _, total_inversoes = mergeSort(vetor)
    return total_inversoes

def kendallTauOtimizado(vetor):
    n = len(vetor)
    if n < 2:
        return 0.0
    
    D = contaInversao(vetor[:]) # cópia
    totalPares = n * (n - 1) // 2
    return 1 - (2*D/ totalPares)
