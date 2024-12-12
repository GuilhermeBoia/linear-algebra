import numpy as np
from sympy import Matrix, Rational

from utils import ler_matriz

def format_rational(rational):
    if rational.denominator == 1:
        return str(rational.numerator)
    elif rational.denominator < 1000:
        return f"{rational.numerator}/{rational.denominator}"
    else:
        return f"{float(rational):.4f}"

def main():
    A = ler_matriz()
    
    A_reduced = Matrix(A).rref()
    reduced_matrix, pivots = A_reduced
    
    rank = len(pivots)
    nullity = A.shape[1] - rank
    
    print("Matriz na forma escalonada reduzida por linhas:")
    rational_matrix = [[Rational(str(elem)) for elem in row] for row in reduced_matrix.tolist()]
    
    max_lengths = [0] * len(rational_matrix[0])
    for row in rational_matrix:
        for j, elem in enumerate(row):
            max_lengths[j] = max(max_lengths[j], len(format_rational(elem)))
    
    for row in rational_matrix:
        formatted_row = [format_rational(elem).rjust(max_lengths[j]) for j, elem in enumerate(row)]
        print(f"[{' '.join(formatted_row)}]")
    
    print(f"\nPosto (quantidade de linhas não nulas na matriz): {rank}")
    print(f"Nulidade (colunas - posto): {A.shape[1]} - {rank} = {nullity}")

if __name__ == "__main__":
    main()