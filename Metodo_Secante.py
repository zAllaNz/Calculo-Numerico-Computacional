''' Autor: Allan Machado Gonçalves
    Matrícula: 134496
    Disciplina: Cálculo Numérico Computacional

    Resumo do método: O método das secantes é uma abordagem iterativa para encontrar as raízes de uma função não linear. Ele utiliza duas 
    estimativas iniciais próximas à raiz desejada e, em cada iteração, calcula uma nova estimativa usando uma linha secante entre os dois 
    pontos. Este processo continua até que a diferença entre as estimativas seja suficientemente pequena, indicando a convergência para a raiz.
'''

from math import * # importando a biblioteca math para usar funções matematicas

def funcao(x): # definindo a funcao com o parâmetro n
  f_x = (exp(1) ** - x) - x # a variável g_x guarda a função definida
  return f_x # retorna o valor de g_x

def secante(x0, x1, f_x0, f_x1): # definindo a funcao secante com o parâmetros x0, x1, f_x0, f_x1
  return x1 - ((f_x1*(x0-x1)) / (f_x0 - f_x1)) # retorna o valor com o resultado da formula da secante

def erro_relativo(x1, x2): # definindo a função de erro relativo percentual passando como parâmetros x0 e x1
  result = abs(((x2 - x1) / x2)) # a variável result guarda o valor da resolução da formula de erro relativo percentual, a função abs serve como módulo
  return result # retorna o valor de result

x0 = 0 # variável x0 tem um valor inicial de 0
x1 = 1 # variável x1 tem um valor inicial de 1
iter = 0 # variável de controle
max_iter = 100 # variável de controle para definir o limite de iterações do laço de repetição
tol = 0.01 # variável tol é a tôlerancia

while(iter < max_iter): # enquanto iter for menor que max_iter, então o loop será verdadeiro
  f_x0 = funcao(x0) # guarda o valor da função na variável f_x0
  f_x1 = funcao(x1) # guarda o valor da função na variável f_x1
  x2 = secante(x0, x1, f_x0, f_x1) # a variável x2 guarda o valor de retorno da função secante
  erro_relativo_result = erro_relativo(x1, x2) # guarda o valor da funçao do erro relativo na variável erro_relativo_result

  if(erro_relativo_result < tol): # se erro_relativo_result for menor que tol, então será verdadeiro
    print("O erro aproximado é: {:.3f}%".format(erro_relativo_result * 100)) # mostra a saída do erro_relativo percentual formatado para três casas decimais
    print("O valor de x1 é: {:.6f}".format(x2)) # imprime a variável x1 formatado para mostrar 6 casas decimais
    break # break é usado para sair de todas as estruturas do código
  elif(iter == max_iter-1): # estrutura de seleção, caso a primeira condícional não for verdadeira essa será checada, será verdadeiro se iter for igual a max_iter - 1
    print("Não foi encontrada uma raiz dentro dos critérios definidos") # saída informando que não foi encontrada uma raiz dentro dos critérios definidos
    break # break é usado para sair de todas as estruturas do código

  x0 = x1 # variável x0 recebe o valor de x1
  x1 = x2 # variável x1 recebe o valor de x2
  iter += 1 # Incrementando a variável iter
