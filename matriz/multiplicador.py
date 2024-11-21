import numpy as np

def main():
    print("Digite a matriz linha por linha, separando os elementos com espaços.")
    print("Para terminar, pressione Enter em uma linha vazia.")
    print("\nDigite a primeira matriz:")
    
    matriz1 = []
    while True:
        linha = input()
        if linha.strip() == "":
            break
        matriz1.append(list(map(float, linha.split())))
    
    print("\nDigite a segunda matriz:")
    matriz2 = []
    while True:
        linha = input()
        if linha.strip() == "":
            break
        matriz2.append(list(map(float, linha.split())))
    
    A = np.array(matriz1)
    B = np.array(matriz2)
    
    if A.shape[1] != B.shape[0]:
        print("\nErro: Não é possível multiplicar essas matrizes.")
        print(f"Lembre-se que o número de colunas da 1 deve ser igual ao número de linhas da 2 ({A.shape[1]} != {B.shape[0]})")
        return
    
    resultado = np.matmul(A, B)
    
    print("\nResultado da multiplicação:")
    print(resultado)

if __name__ == "__main__":
    main()