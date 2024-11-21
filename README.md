# Álgebra Linear Teacher

Desenvolvi este repositório enquanto estudava para a disciplina de Álgebra Linear e queria uma forma rápida de conferir as respostas dos meus exercícios. Meu objetivo é disponibilizar ferramentas práticas para que você verifique se a resposta das suas atividades estão corretas (e também uma forma que achei de tornar estudo de linear menos chato). Espero que goste! 😊

## Matrizes

### Scripts Disponíveis

1. **Escalonador de Matriz** (`escalonador.py`)

   - obtém a Forma Escada de uma matriz
   - calcula o posto e a nulidade da matriz

2. **Verificador de Forma Escada** (`is_escada.py`)

   - Verifica os critérios para uma matriz na Forma Escada:
     - Coeficiente líder igual a 1
     - Zeros acima e abaixo do coeficiente líder
     - Linhas nulas abaixo das linhas não nulas
     - Coeficientes líderes progressivamente à direita

3. **Multiplicador de Matrizes** (`multiplicador.py`)
   - Mostra o resultado da multiplicação de duas matrizes

## Como Usar

### Requisitos

- Python 3
- Dependências NumPy e Sympy

### Instalando as Dependências

Se você ainda não tem as bibliotecas necessárias, pode instalá-las com:

```bash
pip install numpy sympy
```

### Executando os Scripts

```bash
python nome_do_script.py
```

### Formato de Entrada

Para os scripts de matriz, você deve fornecer os dados linha por linha, separando os elementos com espaços. Quando terminar, basta pressionar Enter em uma linha vazia.

Exemplo de entrada:

```
1 2 3
4 5 6
7 8 9
[Enter em uma linha vazia para finalizar]
```

## Contribuições

Se você quiser contribuir, fique à vontade para:

- Adicionar novos scripts
- Sugerir novas funcionalidades
- Corrigir bugs
- Melhorar a documentação

<div align="center">© Guilherme Boia</div>
