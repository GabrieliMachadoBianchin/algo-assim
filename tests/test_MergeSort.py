# tests/test_merge_sort.py
import numpy as np
from utils.mergeSort import mergeSort

def test_merge_sort_ordenado():
    vetor = np.array([1, 2, 3, 4, 5])
    esperado = vetor.copy()
    mergeSort(vetor)
    assert np.array_equal(vetor, esperado)

def test_merge_sort_reverso():
    vetor = np.array([5, 4, 3, 2, 1])
    esperado = np.array([1, 2, 3, 4, 5])
    mergeSort(vetor)
    assert np.array_equal(vetor, esperado)

def test_merge_sort_misto():
    vetor = np.array([10, -2, 0, 3, 1])
    esperado = np.array([-2, 0, 1, 3, 10])
    mergeSort(vetor)
    assert np.array_equal(vetor, esperado)

def test_merge_sort_vazio():
    vetor = np.array([])
    mergeSort(vetor)
    assert vetor.size == 0
