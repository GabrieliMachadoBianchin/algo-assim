"""
Kendall's Tau
"""

def kendallTau(vetor, num):
    C = 0  # pares concordantes
    D = 0  # pares discordantes

    for i in range(num):
        for j in range(i + 1, num):
            if vetor[i] < vetor[j]:
                C += 1
            elif vetor[i] > vetor[j]:
                D += 1

    if C + D == 0:
        return 0  # evita divisão por zero
    return (C - D) / (C + D)
