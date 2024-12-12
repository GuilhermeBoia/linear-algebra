import numpy as np
from sympy import Matrix, Rational
from typing import Union, List

from utils import (
    ler_matriz,
    calcular_cofator,
    mostrar_matriz,
    verificar_matriz_quadrada,
)

def calcular_matriz_cofatores(matriz: np.ndarray) -> np.ndarray:
    """
    Calcula a matriz de cofatores
    """
    n = len(matriz)
    matriz_cofatores = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            matriz_cofatores[i][j] = calcular_cofator(matriz, i, j)
            
    return matriz_cofatores

def calcular_matriz_adjunta(matriz: np.ndarray) -> np.ndarray:
    """
    Calcula a matriz adjunta (transposta da matriz de cofatores)
    """
    return calcular_matriz_cofatores(matriz).T

def main():
    # Lê a matriz da entrada
    A = ler_matriz()
    
    # Verifica se é quadrada
    if not verificar_matriz_quadrada(A):
        print(f"\nErro: A matriz deve ser quadrada para ter inversa!")
        print(f"Matriz fornecida tem dimensões {A.shape[0]}x{A.shape[1]}")
        return
    
    # Mostra a matriz original
    mostrar_matriz(A, "Matriz original")
    
    # Calcula e mostra a matriz de cofatores
    matriz_cofatores = calcular_matriz_cofatores(A)
    mostrar_matriz(matriz_cofatores, "Matriz de cofatores")
    
    # Calcula e mostra a matriz adjunta
    matriz_adjunta = calcular_matriz_adjunta(A)
    mostrar_matriz(matriz_adjunta, "Matriz adjunta (transposta da matriz de cofatores)")

if __name__ == "__main__":
    main()