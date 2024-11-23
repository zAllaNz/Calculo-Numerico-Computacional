''' Autor: Allan Machado Gonçalves
    Matrícula: 134496
    Disciplina: Cálculo Numérico Computacional

    Resumo do método: A interpolação polinomial de Newton é um método para encontrar o polinômio que passa por um conjunto de pontos dados.
    Utiliza o conceito de diferenças divididas para construir o polinômio de forma incremental, adicionando termos à medida que novos pontos 
    são incluídos. A vantagem do método é sua eficiência em adicionar novos pontos sem recalcular o polinômio inteiro.
'''

import numpy as np # importando a biblioteca numpy

def interpolacao_polinomial(x, y, z, n, d): # definindo a função de interpolação polinomial de Newton
  for i in range(n): # Estrutura de repetição no intervalo de 0 até n-1
    d[i, 0] = y[i] # todas as linhas da coluna 0 receberá o valor de y na posição de i

  for j in range(1,n): # Estrutura de repetição no intervalo de 1 até n - 1
    for i in range(n-j): # Estrutura de repetição no intervalo de 0 até n - j
      d[i, j] = (d[i+1, j-1] - d[i, j-1]) / (x[i+j] - x[i]) # Calcula a diferença dividida e armazena na matriz d

  xtermos = 1 # inicializando a variável xtermos com o valor de 1
  yint = d[0, 0] # inicializando a variável yint com o valor d

  for ordem in range(1, n): # Estrutura de repetição no intervalo de 1 até n-1
    xtermos = xtermos * (z - x[ordem - 1]) # Calculando o produto dos termos (z - x[ordem - 1])
    yint += d[0, ordem] * xtermos # Somando o termo correspondente ao resultado final yint

  return yint # Retorna o valor interpolado final

x = [1, 4, 6, 5]  # vetor x 
y = [0, 1.386294, 1.791759, 1.609438] # vetor y
z = 2 # Valor para interpolação
n = len(x) # tamanho do vetor x
d = np.zeros((n, n)) # criando uma matriz d de tamanho n x n com valores zero

resultado = interpolacao_polinomial(x, y, z, n, d) # chamando a função de interpolação polinomial
print(resultado) # imprimindo o resultado