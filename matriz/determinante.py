import numpy as np
from typing import List
from utils import ler_matriz

def verificar_matriz_quadrada(matriz: np.ndarray) -> bool:
    return matriz.shape[0] == matriz.shape[1]

def main():
    # Lê a matriz da entrada
    A = ler_matriz()
    
    # Verifica se é quadrada
    if not verificar_matriz_quadrada(A):
        print(f"\nErro: A matriz deve ser quadrada para ter inversa!")
        print(f"Matriz fornecida tem dimensões {A.shape[0]}x{A.shape[1]}")
        return
    
    print("\nMatriz fornecida:")
    print(A)
    
    det_numpy = round(np.linalg.det(A))
    print(f"\nDeterminante: {det_numpy}")
    

if __name__ == "__main__":
    main()