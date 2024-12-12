import numpy as np
from utils import (
    ler_matriz,
    mostrar_matriz,
    verificar_matriz_quadrada,
    verificar_singular
)
from adjunta import calcular_matriz_adjunta

def calcular_matriz_inversa(matriz: np.ndarray):
    """
    Calcula a matriz inversa usando o método da matriz adjunta
    """
    # Verifica se é singular
    is_singular, det = verificar_singular(matriz)
    if is_singular:
        return None, det
        
    matriz_adjunta = calcular_matriz_adjunta(matriz)
    matriz_inversa = matriz_adjunta / det
    
    return matriz_inversa, det

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
    
    # Calcula a inversa
    inversa, det = calcular_matriz_inversa(A)
    
    if inversa is None:
        print("\nA matriz não possui inversa (determinante = 0)")
        return
        
    # Mostra os resultados
    print(f"\nDeterminante: {round(det)}")
    mostrar_matriz(calcular_matriz_adjunta(A), "Matriz adjunta")
    mostrar_matriz(inversa, "Matriz inversa")
    
    # Verifica o resultado
    produto = np.matmul(A, inversa)
    mostrar_matriz(produto, "A * A^(-1) (deve ser próxima da identidade)", usar_fracoes=True)

if __name__ == "__main__":
    main()