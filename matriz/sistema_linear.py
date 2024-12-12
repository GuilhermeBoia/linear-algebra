import numpy as np
from sympy import Matrix, Rational
from utils import ler_matriz

def classificar_sistema(matriz_aumentada):
    """
    Classifica o sistema linear como possível (determinado/indeterminado) ou impossível
    baseado na matriz aumentada na forma escalonada.
    """
    num_linhas, num_colunas = matriz_aumentada.shape
    num_variaveis = num_colunas - 1
    
    # Converte para Matrix do SymPy e obtém a forma escalonada
    matriz_sympy = Matrix(matriz_aumentada)
    matriz_reduzida, pivots = matriz_sympy.rref()
    
    # Conta o número de pivôs (rank da matriz dos coeficientes)
    rank_coeficientes = len([p for p in pivots if p < num_variaveis])
    
    # Verifica se existe linha do tipo [0 0 0 ... k] onde k ≠ 0 (sistema impossível)
    for i in range(num_linhas):
        todos_zeros = all(abs(matriz_reduzida[i,j]) < 1e-10 for j in range(num_variaveis))
        if todos_zeros and abs(matriz_reduzida[i,num_variaveis]) > 1e-10:
            return "Sistema Impossível (SI)", None
    
    # Se chegou aqui, o sistema é possível
    if rank_coeficientes == num_variaveis:
        return "Sistema Possível e Determinado (SPD)", matriz_reduzida
    else:
        return "Sistema Possível e Indeterminado (SPI)", matriz_reduzida

def encontrar_solucao(matriz_reduzida):
    """
    Encontra a solução do sistema baseado na matriz reduzida.
    Para sistemas indeterminados, expressa em termos de parâmetros livres.
    """
    num_linhas, num_colunas = matriz_reduzida.shape
    num_variaveis = num_colunas - 1
    
    # Identifica variáveis básicas e livres
    colunas_pivot = []
    for i in range(num_linhas):
        for j in range(num_variaveis):
            if abs(matriz_reduzida[i,j] - 1) < 1e-10 and \
               all(abs(matriz_reduzida[k,j]) < 1e-10 for k in range(num_linhas) if k != i):
                colunas_pivot.append(j)
                break
    
    variaveis_livres = [j for j in range(num_variaveis) if j not in colunas_pivot]
    
    # Prepara a string de solução
    solucao = []
    parametro = 1
    
    for var in range(num_variaveis):
        if var in colunas_pivot:
            # Encontra a linha onde esta variável é pivot
            linha_pivot = next(i for i in range(num_linhas) if abs(matriz_reduzida[i,var] - 1) < 1e-10)
            
            # Converte para frações para melhor visualização
            termos = []
            valor_independente = Rational(str(float(matriz_reduzida[linha_pivot,num_variaveis])))
            if abs(valor_independente) > 1e-10:
                termos.append(f"{valor_independente}")
            
            # Adiciona os termos com parâmetros
            for var_livre in variaveis_livres:
                coef = -Rational(str(float(matriz_reduzida[linha_pivot,var_livre])))
                if abs(coef) > 1e-10:
                    termos.append(f"{coef if coef != -1 else '-'}t{var_livre+1}")
            
            solucao.append(f"x{var+1} = {' + '.join(termos) if termos else '0'}")
        else:
            solucao.append(f"x{var+1} = t{parametro}")
            parametro += 1
            
    return solucao

def main():
    print("Separe os elementos com espaços (último elemento de cada linha é o termo independente).")
    A = ler_matriz()
    
    print("\nMatriz aumentada fornecida:")
    print(A)
    
    classificacao, matriz_reduzida = classificar_sistema(A)
    print(f"\nClassificação do sistema: {classificacao}")
    
    if matriz_reduzida is not None:
        print("\nMatriz aumentada na forma escalonada reduzida:")
        for i in range(matriz_reduzida.shape[0]):
            elementos = [f"{Rational(str(float(elem)))}" for elem in matriz_reduzida.row(i)]
            print(f"[{' '.join(elementos)}]")
        
        if classificacao != "Sistema Impossível (SI)":
            print("\nSolução do sistema:")
            solucao = encontrar_solucao(matriz_reduzida)
            for eq in solucao:
                print(eq)

if __name__ == "__main__":
    main()