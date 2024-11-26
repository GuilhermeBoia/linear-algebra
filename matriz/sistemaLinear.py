import numpy as np

def escalonamento(matrix):
    m, n = matrix.shape
    for i in range(min(m, n)):
       
        max_row = i + np.argmax(abs(matrix[i:, i]))  
        matrix[[i, max_row]] = matrix[[max_row, i]]  

        if abs(matrix[i, i]) < 1e-10:
            continue  

        matrix[i] = matrix[i] / matrix[i, i] 
        for j in range(i + 1, m):
            matrix[j] -= matrix[j, i] * matrix[i]  
    return matrix

def calcula_posto(matrix):
    
    matrix_escada = escalonamento(matrix.copy())
    return sum(not all(abs(elem) < 1e-10 for elem in row) for row in matrix_escada)

def analisa_sistema(A, b):
    
    A_aumentada = np.hstack([A, b.reshape(-1, 1)])
    
    posto_A = calcula_posto(A)
    posto_A_aumentada = calcula_posto(A_aumentada)
    
    n = A.shape[1]  
    if posto_A != posto_A_aumentada:
        return "Sistema incompatível: não possui solução."

    if posto_A == n:
        return "Sistema possível e determinado: solução única."
    else:
        grau_liberdade = n - posto_A
        return (f"Sistema possível e indeterminado: infinitas soluções.\n"
                f"Grau de liberdade: {grau_liberdade} (escolha {grau_liberdade} incógnitas livres).")

def main():
    print("Digite apenas os termos da matriz de incógnitas(a) linha por linha, separando os elementos com espaços.")
    print("Para terminar, pressione Enter em uma linha vazia.")
    
    matriz_entrada = []
    while True:
        linha = input(" ")
        if linha.strip() == "":
            break
        matriz_entrada.append(list(map(float, linha.split())))
    
    print("Digite os termos independentes(b) em uma linha :")
    termos_b = list(map(float, input("").split()))
    
    A = np.array(matriz_entrada)
    b = np.array(termos_b)
    
    resultado = analisa_sistema(A, b)
    print(resultado)

if __name__ == "__main__":
    main()