''' Autor: Allan Machado Gonçalves
    Matrícula: 134496
    Disciplina: Cálculo Numérico Computacional

    Resumo do método: A regressão polinomial é uma técnica estatística que ajusta um polinômio aos dados 
    para modelar a relação entre uma variável dependente e uma ou mais variáveis independentes. Ela expande 
    a regressão linear ao incluir termos de potência, permitindo modelar relações não lineares. O objetivo é 
    minimizar o erro entre os valores preditos e observados.
'''

import numpy as np # Importando a biblioteca numpy

def eq_normal(x, y, tam, n):  # Define a função que calcula os coeficientes da equação normal.
    a = np.zeros((tam, tam))  # Cria uma matriz quadrada de zeros com dimensão tam
    b = np.zeros((tam))  # Cria um vetor de zeros com tamanho tam
    for i in range(1, m + 2): # Estrutura de repetição vai do um até o m+2
        for j in range(1, i+1): # Estrutura de repetição vai do um até o i+1
            k = i + j - 2  # Calcula o expoente da soma dos termos.
            soma = 0  # Inicializa a variável soma.
            for l in range(n): # Estrutura de repetição vai do zero até o n
                soma += x[l] ** k  # Soma as potências dos elementos de x
            a[i - 1, j - 1] = soma  # Atribui o valor de soma à matriz a
            a[j - 1, i - 1] = soma  # Preenche a matriz simetricamente
        soma = 0  # Reinicializa a variável soma
        for l in range(n): # Estrutura de repetição vai do zero até o n
            soma += y[l] * (x[l] ** (i - 1))  # Calcula o produto de y pelo polinômio de x
        b[i - 1] = soma  # Atribui o valor da soma ao vetor b
    return a, b  # Retorna a matriz a e o vetor b

def eliminacao_progressiva(A, B, n): # definindo a função "eliminação progressiva" com os parâmetros A, B e n.
    for k in range(n-1): # estrutura de repetição para percorrer os pivôs, vai do zero até n-1.
        for i in range(k+1, n): # estrutura de repetição para percorrer as linhas abaixo do pivô.
            fator = A[i, k] / A[k, k] # a variável fator recebe o resultado de A[i, k] dividido por A[k, k] (ambos são posições da matriz).
            for j in range(k, n): # estrutura de repetição para percorrer as colunas depois do pivô.
                A[i, j] = A[i, j] - (fator * A[k, j]) # A[i, j] vai receber o resultado da operação, esse passo serve para eliminar as variáveis formando o triangular superior.
            B[i] = B[i] - (fator * B[k]) # B[i] vai receber o resultado da multiplicação de determinada linha.
    return A, B # retorna a matriz A e o vetor B
    
def subs_progressiva(A, B, X, n): # definindo a função "substuição progressiva" com os parâmetros A, B, X e n.
    X[n] = B[n] / A[n, n] # X[n] recebe o resultado de B[n] divido por A[n, n], X[n] representa o valor de X3 nesse caso
    for i in range(n, -1, -1): # Estrutura de repetição que percorre as linhas de baixo para cima, com excessão da última.
        soma = B[i] # variável soma guarda o valor de B na posição i
        for j in range(i+1, n+1): # Estrutura de repetição que percorre as colunas depois do elemento diagonal
            soma = soma - (A[i, j] * X[j]) # soma guarda o resultado da operação de b[i] - A[i, j].X[j]
        X[i] = soma / A[i, i] # e por fim, o vetor X na posição i vai guardar o valor da operação anterior divido por A[i, i]
    X = np.round(X, 6) # arrendondando o vetor x com seis algarismos significativos
    return X # retorna o vetor X

def soma_quadrados(y, n):  # Define a função para calcular a soma dos quadrados
    y_barra = sum(y)/n  # Calcula a média dos valores de y
    st = 0  # inicializa a variável st
    for i in range(n): # estrutura de repetição vai do zero até o n
        st += (y[i] - y_barra) ** 2  # soma os quadrados das diferenças de y
    st = np.round(st, 2)  # arredonda o valor de st para 2 casas decimais
    return st  # retorna o valor de st

def soma_residuos(x, X, y, n, m):  # define a função para calcular a soma dos resíduos
    aux = [0] * n  # inicializa um vetor auxiliar de zeros com tamanho 'n'
    sr = 0  # inicializa a variável 'sr' para armazenar a soma dos resíduos
    for i in range(n): # estrutura de repetição vai do zero até o n
        for j in range(m+1): # estrutura de repetição vai do zero até o m+1
            aux[i] += X[j] * (x[i] ** j)  # calcula o valor predito pela regressão
    for i in range(n): # estrutura de repetição vai do zero até n
        sr += (y[i] - aux[i]) ** 2  # soma os quadrados das diferenças entre os valores observados e preditos
    return sr  # retorna o valor de sr


def erro_padrao(sr, n, m):  # Define a função para calcular o erro padrão
    return (sr / (n - (m+1))) ** 0.5  # Calcula e retorna o erro padrão

def coe_determinacao(sr, st):  # Define a função para calcular o coeficiente de determinação
    return (st - sr) / st  # Calcula e retorna o valor de R²

tam = 3 # Definindo o tamanho da matriz
m = 2 # Ordem do polinômio
x = [0, 1, 2, 3, 4, 5] # Valores da lista x
y = [2.1, 7.7, 13.6, 27.2, 40.9, 61.1] # valores da lista y
n = len(x) # Número de dados

a, b = eq_normal(x, y, tam, n) # Calculando os elementos da equação normal
eliminacao_progressiva(a, b, tam) # chamando a função de eliminação progressiva
X = [0] * tam # criando o vetor X com o tamanho n
tam -= 1 # decrementando a variável n
X = subs_progressiva(a, b, X, tam) # chamando a função substituição progressiva 

st = soma_quadrados(y, n)  # Calcula a soma dos quadrados totais
sr = soma_residuos(x, X, y, n, m)  # Calcula a soma dos resíduos
er = erro_padrao(sr, n, m)  # calcula o erro padrão
r = coe_determinacao(sr, st)  # calcula o coeficiente de determinação

print("Coeficiente de determinação: {:.6f}".format(r))  # exibe o coeficiente de determinação
print("Erro padrão: {:.6f}".format(er))  # exibe o erro padrão