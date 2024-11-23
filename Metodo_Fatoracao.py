''' Autor: Allan Machado Gonçalves
    Matrícula: 134496
    Disciplina: Cálculo Numérico Computacional

    Resumo do método: A fatoração LU decompõe uma matriz A em uma matriz triangular inferior L e uma matriz triangular superior U, 
    formando A = LU. Para resolver o sistema Ax = B, primeiro resolve-se Ld = B usando substituição progressiva, e depois Ux = x 
    usando substituição regressiva. Este método é eficiente e utilizado em aplicações científicas e de engenharia.
'''

import numpy as np # importando a biblioteca numpy

def decomposicao(A, n): # definindo a função "decomposição" para decompor a matriz A em LU
    for k in range(n-1): # estrutura de repetição vai do zero até n-1
        for i in range(k+1, n): # estrutura de repetição onde i recebe o valor de k + 1
            fator = A[i, k] / A[k, k] # a variável fator recebe o resultado de A[i, k] dividido por A[k, k] (ambos são posições da matriz).
            A[i, k] = fator # a posição da matriz A[i, k] recebe o valor de fator
            for j in range(k+1, n): # estrutura de repetição onde j recebe o valor de k + 1
                A[i, j] -= fator * A[k, j] # a posição da matriz A[i, j] vai subtrair seu o valor depois de realizada a operação entre fator e A[k, j]
    return A

def subs_progressiva(A, B, D, n): # definindo a função "Substituição Progressiva" para manipular a matriz B
    for i in range(n): # estrutura de repetição vai do zero até o tamanho da matriz A
        soma = B[i] # variável soma vai receber o valor do vetor B na posição de i
        for j in range(i): # estrutura de repetição vai do zero até o valor de i
            soma -= A[i, j] * D[j] # soma vai armazenar a operação de A[i, j] * D[j] menos o seu valor atual
        D[i] = soma # o vetor D na posição i vai guardar o valor de soma
    D = np.round(D, 6) # arrendondando o vetor D com seis algarismos significativos
    return D # retorna o vetor D

def subs_regressiva(A, D, X, n): # definindo a função "Substituição regressiva
    for i in range(n-1, -1, -1): # esse loop vai rodar invertido, ou seja, de n-1 até 0
        soma = D[i] # soma vai receber o valor do vetor D na posição i
        for j in range(i+1, n): # estrutura de repetição onde i recebe o valor de k + 1
            soma -= A[i, j] * X[j] # soma vai armazenar a operação de A[i, j] * X[j] menos o seu valor atual
        X[i] = soma / A[i, i] # o vetor X na posição i vai receber o resultado da soma dividida pela matriz A na posição [i, i]
        X = np.round(X, 6) # arrendondando o vetor X com seis algarismos significativos
    return X # retorna o vetor X 

A = np.array([[3, -0.1, -0.2],[0.1, 7, -0.3],[0.3, -0.2, 10]]) # Criando a matriz A
B = np.array([7.85, -19.3, 71.4]) # Criando a matriz B
n = len(A) # n retorna o tamanho da matriz
D = [0] * n # cria um vetor de tamanho N com valores de 0 em todas as posições
X = [0] * n # cria um vetor de tamanho N com valores de 0 em todas as posições
A = decomposicao(A, n) # matriz A vai guardar o resultado da função decomposição
D = subs_progressiva(A, B, D, n) # matriz D vai guardar o resultado da função substituição progressiva
X = subs_regressiva(A, D, X, n) # vetor X vai guardar o resultado da função substituição regressiva

print("o vetor X tem valor de: ", X) # imprime o valor do vetor X
