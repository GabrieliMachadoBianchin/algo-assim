# tests/test_kendall_fast.py

from utils.kendallTauOtimizado import kendallTauOtimizado

def test_kendall_otimizado_ordenado():
    vetor = [1, 2, 3, 4, 5]
    assert kendallTauOtimizado(vetor) == 1.0

def test_kendall_otimizado_reverso():
    vetor = [5, 4, 3, 2, 1]
    assert kendallTauOtimizado(vetor) == -1.0

def test_kendall_otimizado_misto():
    vetor = [1, 3, 2, 4, 5]
    assert round(kendallTauOtimizado(vetor), 2) == 0.8

def test_kendall_otimizado_iguais():
    vetor = [7, 7, 7, 7]
    assert kendallTauOtimizado(vetor) == 0.0
