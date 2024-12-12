import numpy as np
from sympy import Matrix, Rational
from typing import Union, List, Tuple

def parse_number(s: str) -> float:
    """Converte uma string para número, aceitando tanto decimais quanto frações"""
    try:
        if '/' in s:
            num, den = map(int, s.split('/'))
            return float(num) / float(den)
        else:
            return float(s)
    except ValueError as e:
        raise ValueError(f"Formato inválido: {s}. Use decimais (ex: 1.5) ou frações (ex: 3/7)")

def ler_matriz() -> np.ndarray:
    """
    Lê uma matriz da entrada padrão, aceitando decimais e frações
    Retorna a matriz como um array numpy
    """
    print("Digite a matriz linha por linha, separando os elementos com espaços.")
    print("Você pode usar números decimais (1.5) ou frações (3/7)")
    print("Para terminar, pressione Enter em uma linha vazia.")
    
    matriz_entrada = []
    while True:
        try:
            linha = input()
            if linha.strip() == "":
                break
            linha_numeros = [parse_number(x.strip()) for x in linha.split()]
            matriz_entrada.append(linha_numeros)
        except ValueError as e:
            print(f"Erro: {e}")
            print("Por favor, digite a linha novamente.")
            continue
    
    return np.array(matriz_entrada)

def calcular_cofator(matriz: np.ndarray, i: int, j: int) -> float:
    """
    Calcula o cofator do elemento (i,j) da matriz
    """
    # Remove a linha i e coluna j para obter a menor complementar
    menor = np.delete(np.delete(matriz, i, axis=0), j, axis=1)
    
    # Calcula o determinante da menor complementar
    det_menor = np.linalg.det(menor)
    
    # Multiplica pelo fator (-1)^(i+j)
    cofator = det_menor * (-1) ** (i + j)
    
    return cofator

def formatar_matriz(matriz: np.ndarray, usar_fracoes: bool = True) -> List[List[str]]:
    """
    Formata a matriz para exibição, opcionalmente convertendo para frações
    """
    if usar_fracoes:
        return [[str(Rational(str(float(elem))).limit_denominator()) for elem in row] for row in matriz]
    else:
        return [[f"{elem:.6f}" for elem in row] for row in matriz]

def mostrar_matriz(matriz: np.ndarray, nome: str, usar_fracoes: bool = True):
    """
    Exibe a matriz formatada com um título
    """
    print(f"\n{nome}:")
    matriz_formatada = formatar_matriz(matriz, usar_fracoes)
    max_len = max(len(elem) for row in matriz_formatada for elem in row)
    
    for row in matriz_formatada:
        print("[" + " ".join(elem.rjust(max_len) for elem in row) + "]")

def verificar_matriz_quadrada(matriz: np.ndarray) -> bool:
    """
    Verifica se a matriz é quadrada
    """
    return matriz.shape[0] == matriz.shape[1]

def verificar_singular(matriz: np.ndarray) -> Tuple[bool, float]:
    """
    Verifica se a matriz é singular (determinante = 0)
    Retorna (é_singular, determinante)
    """
    det = np.linalg.det(matriz)
    return abs(det) < 1e-10, det

# Funções auxiliares para manipulação de matrizes
def matriz_para_sympy(matriz: np.ndarray) -> Matrix:
    """
    Converte uma matriz numpy para matriz SymPy
    """
    return Matrix(matriz)

def matriz_para_numpy(matriz: Matrix) -> np.ndarray:
    """
    Converte uma matriz SymPy para matriz numpy
    """
    return np.array(matriz.tolist(), dtype=float)