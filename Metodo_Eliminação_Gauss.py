''' Autor: Allan Machado Gonçalves
    Matrícula: 134496
    Disciplina: Cálculo Numérico Computacional

    Resumo do método: A eliminação gaussiana, também conhecida como escalonamento, é um método para resolver sistemas de equações lineares,
    transformando a matriz dos coeficientes em uma forma triangular superior por meio de operações elementares de linha. Primeiro, forma-se a 
    matriz aumentada combinando a matriz dos coeficientes com o vetor dos termos constantes. Em seguida, realiza-se a eliminação progressiva para 
    cada coluna, seleciona-se um pivô (o maior valor absoluto na coluna), normaliza-se a linha do pivô, e elimina-se os elementos abaixo do pivô. 
    Após obter a matriz triangular superior, resolve-se o sistema por substituição progressiva, começando pela última equação e substituindo os 
    valores encontrados nas equações anteriores, até resolver todas as variáveis.
'''

import numpy as np # importando a biblioteca numpy

def eliminacao_progressiva(A, B, n): # definindo a função "eliminação progressiva" com os parâmetros A, B e n.
    for k in range(n-1): # estrutura de repetição para percorrer os pivôs, vai do zero até n-1.
        for i in range(k+1, n): # estrutura de repetição para percorrer as linhas abaixo do pivô.
            fator = A[i, k] / A[k, k] # a variável fator recebe o resultado de A[i, k] dividido por A[k, k] (ambos são posições da matriz).
            for j in range(k, n): # estrutura de repetição para percorrer as colunas depois do pivô.
                A[i, j] = A[i, j] - (fator * A[k, j]) # A[i, j] vai receber o resultado da operação, esse passo serve para eliminar as variáveis formando o triangular superior.
            B[i] = B[i] - (fator * B[k]) # B[i] vai receber o resultado da multiplicação de determinada linha.
    print(A)
    print(B)
    return A, B # retorna a matriz A e o vetor B
    
def subs_progressiva(A, B, X, n): # definindo a função "substuição progressiva" com os parâmetros A, B, X e n.
    X[n] = B[n] / A[n, n] # X[n] recebe o resultado de B[n] divido por A[n, n], X[n] representa o valor de X3 nesse caso
    for i in range(n, -1, -1): # Estrutura de repetição que percorre as linhas de baixo para cima, com excessão da última.
        soma = B[i] # variável soma guarda o valor de B na posição i
        for j in range(i+1, n+1): # Estrutura de repetição que percorre as colunas depois do elemento diagonal
            soma = soma - (A[i, j] * X[j]) # soma guarda o resultado da operação de b[i] - A[i, j].X[j]
        X[i] = soma / A[i, i] # e por fim, o vetor X na posição i vai guardar o valor da operação anterior divido por A[i, i]
    return X # retorna o vetor X
    
def trocar_linhas(matriz, linha_1, linha_2): # definindo a função para trocar linhas caso necessário
    if(matriz.ndim == 1): # estrutura de seleção, caso o vetor seja 1D
        matriz[linha_1], matriz[linha_2] = matriz[linha_2], matriz[linha_1] # realizando a troca de linhas
    else: # caso o vetor não seja 1D
        matriz[[linha_1], [linha_2]] = matriz[[linha_2], [linha_1]]
    
def pivotamento_parcial(A, B, n): # definindo a função para realizar o pivotamento parcial
    for j in range(n): # estrutura de repetição para percorrer as colunas
        indice_pivo = max(range(j, n), key=lambda i: abs(A[i,j])) # é utilizado max com lambda para encontrar o índice da linha com o maior valor absoluto
        if(indice_pivo != j): # estrutura de seleção para trocar de linhas se necessário
            trocar_linhas(A, j, indice_pivo) # chamando a função "trocar linhas" com os parâmetros A, j e indice_pivo
            trocar_linhas(B, j, indice_pivo) # chamando a função "trocar linhas" com os parâmetros B, j e indice_pivo

A = np.array([[3, -0.1, -0.2],[0.1, 7, -0.3],[0.3, -0.2, 10]]) # Criando a matriz A
B = np.array([7.85, -19.3, 71.4]) # Criando a matriz B
n = len(A) # n retorna o tamanho da matriz
pivotamento_parcial(A, B, n) # chamando a função de pivotamento parcial
eliminacao_progressiva(A, B, n) # chamando a função de eliminação progressiva
X = [0] * n # criando o vetor X com o tamanho n
n -= 1 # decrementando a variável n
subs_progressiva(A, B, X, n) # chamando a função substituição progressiva
X = np.round(X, 6) # arrendondando o vetor x com seis algarismos significativos
print("Soluções aproximadas:") # printando string
for i in range(len(X)): # laço de repetição
    print(f"x{i+1} = {X[i]}") # print com os valores de X
