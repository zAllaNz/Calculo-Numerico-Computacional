''' Autor: Allan Machado Gonçalves
    Matrícula: 134496
    Disciplina: Cálculo Numérico Computacional

    Resumo do método: O método de Newton-Raphson é uma técnica iterativa para encontrar raízes de uma função. Ele usa uma abordagem de aproximação linear para se aproximar da 
    raiz da função. O processo começa com uma estimativa inicial da raiz e, em seguida, calcula-se a tangente à curva da função nesse ponto. A interseção dessa tangente com o 
    eixo x fornece uma nova estimativa da raiz, que é mais precisa do que a estimativa inicial. Esse processo é repetido até que a diferença entre as estimativas sucessivas 
    seja suficientemente pequena ou até que um número máximo de iterações seja atingido. 
'''

from math import * # importando a biblioteca math para usar funções matematicas

def funcao(x): # definindo a funcao com o parâmetro n
  f_x = (exp(1) ** - x) - x # a variável g_x guarda a função definida
  return f_x # retorna o valor de g_x

def derivada_funcao(x): # definindo a funcao com o parâmetro n
  df_x = -(exp(1) ** - x) - 1 # a variável g_x guarda a função definida
  return df_x # retorna o valor de g_x

def newton_raphson(x0, f_x0, df_x0): # definindo a função newton_raphson com os parâmetros x0, f_x0, df_x0
  return x0 - (f_x0)/(df_x0) # retorna o valor da função

def erro_relativo(x0, x1): # definindo a função de erro relativo percentual passando como parâmetros x0 e x1
  result = abs(((x1 - x0) / x1)) # a variável result guarda o valor da resolução da formula de erro relativo percentual, a função abs serve como módulo
  return result # retorna o valor de result

x0 = 0 # variável x0 tem um valor inicial de 0
iter = 0 # variável de controle
max_iter = 100 # variável de controle para definir o limite de iterações do laço de repetição
tol = 0.01 # variável tol é a tôlerancia

while(iter < max_iter): # enquanto iter for menor que max_iter, então o loop será verdadeiro
  f_x0 = funcao(x0) # guarda o valor da função na variável f_x0
  df_x0 = derivada_funcao(x0) # guarda o valor da função derivada_funcao na variável df_x0
  x1 = newton_raphson(x0, f_x0, df_x0) # guarda o valor da função newton_raphson na variável x1
  erro_relativo_result = erro_relativo(x0, x1) # guarda o valor da funçao do erro relativo na variável erro_relativo_result

  if(erro_relativo_result < tol): # se erro_relativo_result for menor que tol, então será verdadeiro
    print("O erro aproximado é: {:.3f}%".format(erro_relativo_result * 100)) # mostra a saída do erro_relativo percentual formatado para três casas decimais
    print("O valor de x1 é: {:.6f}".format(x1)) # imprime a variável x1 formatado para mostrar 6 casas decimais
    break # break é usado para sair de todas as estruturas do código
  elif(iter == max_iter-1): # estrutura de seleção, caso a primeira condícional não for verdadeira essa será checada, será verdadeiro se iter for igual a max_iter - 1
    print("Não foi encontrada uma raiz dentro dos critérios definidos") # saída informando que não foi encontrada uma raiz dentro dos critérios definidos
    break # break é usado para sair de todas as estruturas do código

  x0 = x1 # variável x0 recebe o valor de x1
  iter += 1 # Incrementando a variável iter