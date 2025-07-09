# tests/test_kendall.py

from utils.kendallTau import kendallTau

def test_kendall_ordenado():
    vetor = [1, 2, 3, 4, 5]
    resultado = kendallTau(vetor, len(vetor))
    assert resultado == 1.0  # totalmente ordenado

def test_kendall_reverso():
    vetor = [5, 4, 3, 2, 1]
    resultado = kendallTau(vetor, len(vetor))
    assert resultado == -1.0  # totalmente invertido

def test_kendall_parcial():
    vetor = [1, 3, 2, 4, 5]
    resultado = kendallTau(vetor, len(vetor))
    assert round(resultado, 2) == 0.8  # há uma inversão apenas (3, 2)

def test_kendall_empates():
    vetor = [1, 2, 2, 3]
    resultado = kendallTau(vetor, len(vetor))
    # empates são ignorados, C = 4, D = 0 → (4 - 0)/(4 + 0) = 1.0
    assert resultado == 1.0

def test_kendall_todos_iguais():
    vetor = [1, 1, 1, 1]
    resultado = kendallTau(vetor, len(vetor))
    assert resultado == 0  # C + D = 0, retorno forçado para 0
