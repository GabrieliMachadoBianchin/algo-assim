# main.py
import numpy as np
from utils.mergeSort import mergeSort  

if __name__ == "__main__":
    vetor = np.array([10, 5, 3, 8, 9, 1, 2])
    print("Antes da ordenação:", vetor)
    mergeSort(vetor)
    print("Depois da ordenação:", vetor)
