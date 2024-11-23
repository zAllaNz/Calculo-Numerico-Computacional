''' Autor: Allan Machado Gonçalves
    Matrícula: 134496
    Disciplina: Cálculo Numérico Computacional

    Resumo do método: O método de Gauss-Seidel é um algoritmo iterativo que refina soluções para sistemas de equações lineares, 
    utilizando valores atualizados imediatamente. Isso geralmente resulta em uma taxa de convergência mais rápida em comparação 
    com o método de Jacobi. Ele converge para a solução em matrizes diagonalmente dominantes ou simétricas e positivas definidas.
'''
import numpy as np

def norma(vetor): # definindo a função norma para calcular o erro relativo
    tam = len(vetor) # tam recebe o tamanho do vetor
    norm = 0 # variável norm recebe o valor 0
    for i in range(tam): # estrutura de repetição vai do zero até o tamanho do vetor
        norm += vetor[i] ** 2 # é somado ao valor da variável norm o resultado do vetor na posição i elevado na dois
    return norm ** 0.5 # retorna o resultado da raiz quadrada de norm

def erro_relativo(X, x_antigo): # função para calcular o erro relativo
   x0 = norma(X) # variável x0 chama a função norma e guarda o valor da operação 
   x1 = norma(x_antigo) # variável x1 chama a função norma e guarda o valor da operação 
   return abs((x0 - x1) / x0) # retorna o valor do erro relativo
    

A = np.array([[15, -3, -1],[-3, 18, -6],[-4, -1, 12]]) # Criando a matriz A
B = np.array([3800, 1200, 2350]) # Criando a matriz B
n = len(A) # n retorna o tamanho da matriz
X = np.zeros(n) # cria um vetor de tamanho N com valores de 0 em todas as posições
iter_max = 100 # variável de controle para definir o limite de iterações do laço de repetição
tol = 0.05 # variável tol é a tôlerancia
iter = 0 # variável de controle
x_antigo = X.copy()

while(iter < iter_max): # laço de repetição que vai rodar enquanto iter for menor que iter_max
    for i in range(n): # estrutura de repetição vai do zero até o tamanho da matriz A
        soma = 0 # inicializa a variável soma com valor zero
        for j in range(n): # estrutura de repetição vai do zero até o tamanho da matriz A
            if(j < i): # estrutura de seleção caso j seja menor que i
                soma += A[i, j] * X[j] # variável soma atribui o resultado da operação entre A[i, j] vezes X[j] ao seu valor
            elif(j > i):
                soma += A[i, j] * x_antigo[j] # variável soma atribui o resultado da operação entre A[i, j] vezes x_antigo[j] ao seu valor
        X[i] = (B[i] - soma)/A[i, i] # o vetor X na posição i vai armazenar o resultado da operação de 1 divido por A[i, i] vezes B[i] menos a soma

    
    erro_relativo_result = erro_relativo(X, x_antigo) # guarda o valor da funçao do erro relativo na variável erro_relativo_result
    if(erro_relativo_result < tol): # se erro_relativo_result for menor que tol, então será verdadeiro
        X = np.round(X, 6) # arrendondando o vetor x com seis algarismos significativos
        print("O erro aproximado é de {:.2f}%".format(erro_relativo_result * 100)) # mostra a saída do erro_relativo_result em porcentagem formatado para duas casas decimais
        print("O valor do vetor X é:",X) # mostra a saída do vetor X formatado
        break # break é usado para sair de todas as estruturas do código

    x_antigo = X.copy() # faz uma cópia do vetor X para o x_antigo
    iter += 1 # incrementa a variável iter em mais um
