import numpy as np

def verifica_criterios_escada(matrix):
    if len(matrix) == 0:
        return True, []
        
    num_rows, num_cols = matrix.shape
    criterios_feridos = set()
    
    leading_positions = []
    for i, row in enumerate(matrix):
        pos = -1
        for j, elem in enumerate(row):
            if abs(elem) > 1e-10:
                pos = j
                break
        if pos != -1:
            leading_positions.append((i, pos))
            
            if abs(row[pos] - 1) > 1e-10:
                criterios_feridos.add("Critério I: O primeiro elemento não nulo de uma linha não nula deve ser 1")
                
            for k in range(num_rows):
                if k != i and abs(matrix[k][pos]) > 1e-10:
                    criterios_feridos.add("Critério II: Cada coluna que contém o primeiro elemento não nulo deve ter zeros nas outras posições")
                    break
    
    encontrou_linha_nula = False
    for i in range(num_rows):
        row_is_zero = all(abs(elem) < 1e-10 for elem in matrix[i])
        if row_is_zero:
            encontrou_linha_nula = True
        elif encontrou_linha_nula:
            criterios_feridos.add("Critério III: Toda linha nula deve ocorrer abaixo de todas as linhas não nulas")
            break
    
    for i in range(len(leading_positions)-1):
        if leading_positions[i][1] >= leading_positions[i+1][1]:
            criterios_feridos.add("Critério IV: O primeiro elemento não nulo de cada linha deve ocorrer à direita do primeiro elemento não nulo da linha anterior")
            break
    
    return len(criterios_feridos) == 0, sorted(list(criterios_feridos))

def main():
    print("Digite a matriz linha por linha, separando os elementos com espaços.")
    print("Para terminar, pressione Enter em uma linha vazia.")
    
    matriz_entrada = []
    while True:
        linha = input()
        if linha.strip() == "":
            break
        matriz_entrada.append(list(map(float, linha.split())))
    
    A = np.array(matriz_entrada)
    
    eh_escada, motivos = verifica_criterios_escada(A)
    print("Está na forma escada? ", end="")
    print(eh_escada)
    if not eh_escada:
        for motivo in motivos:
            print(" " +motivo)

if __name__ == "__main__":
    main()