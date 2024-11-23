''' Autor: Allan Machado Gonçalves
    Matrícula: 134496
    Disciplina: Cálculo Numérico Computacional

    Resumo do método: O método de Lagrange é uma técnica de interpolação polinomial que constrói o polinômio como uma soma 
    de termos, cada um associado a um ponto específico. Cada termo é ajustado para ser zero nos demais pontos e um no ponto 
    atual. Isso garante que o polinômio passe por todos os pontos dados. É útil para calcular valores intermediários em dados 
    discretos.
'''

def lagrange(x, y, z, n): # definindo a função de interpolação polinomial de lagrange 
  soma = 0 # inicializando soma com valor zero
  for i in range(n): # Estrutura de repetição no intervalo de 0 até n
    L = y[i] # Inicializa o termo Lagrange com o valor de y[i]
    for j in range(n): # Estrutura de repetição no intervalo de 0 até n
      if(i != j): # se i for diferente de j
        L = L * (z - x[j])/(x[i]-x[j]) # Calcula o termo de Lagrange
    soma += L # soma vai acumular o valor de L
  return soma # retorna soma

x = [1, 4, 6, 5]  # vetor x 
y = [0, 1.386294, 1.791759, 1.609438] # vetor y
z = 2 # Valor para interpolação
n = len(x) # tamanho do vetor x

result = lagrange(x, y, z, n) # Chamando a função de lagrange
print(f"Resultado da Interpolação: {result:.6f}") # Imprimindo o resultado final com 6 casas decimais