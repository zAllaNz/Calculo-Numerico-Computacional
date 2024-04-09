''' Autor: Allan Machado Gonçalves
    Matrícula: 134496
    Disciplina: Cálculo Numérico Computacional
    Método: Ponto Fixo

    Resumo do método: No método do ponto fixo, a fórmula pode ser deduzida isolando o x no lado esquerdo da equação, fazemos isso através de manipulação algébrica ou simplesmente
    isolando o x em ambos os lados da equação. Após ser passado uma aproximação inicial para a raiz, a equação pode ser usada para calcular uma nova aproximação, esse processo
    é iterativo e a função g(x) é aplicada repetidamente a esse palpite, até que uma estimativa satisfatória seja atingida. Vale ressaltar que o método do ponto fixo pode não
    convergir para todas as funções, portanto é importante escolher uma g(x) adequada e verificar a convergência durante as iterações.
'''

from math import * # importando a biblioteca math para usar funções matematicas

def funcao(n): # definindo a funcao com o parâmetro n
  g_x = exp(1) ** - n # a variável g_x guarda a função definida
  return g_x # retorna o valor de g_x

def erro_relativo_percentual(x0, x1): # definindo a função de erro relativo percentual passando como parâmetros x0 e x1
  result = abs(((x1 - x0) / x1)) # a variável result guarda o valor da resolução da formula de erro relativo percentual, a função abs serve como módulo
  return result # retorna o valor de result

x0 = 0 # variável x0 tem um valor inicial de 0
x1 = funcao(x0) # a variável x1 vai receber o valor do resultado da funcao g(x) usado como parâmetro a variável x0
iter = 0 # variável de controle
max_iter = 100 # variável de controle para definir o limite de iterações do laço de repetição
tol = 0.05 # variável tol é a tôlerancia

while(iter < max_iter): # o laço de repetição será verdadeiro enquanto o iter for menor que max_iter
  erro_aproximado = erro_relativo_percentual(x0,x1) # a variável erro_aproximado receberá o valor do resultado da funçao erro_percentual_relativo

  if(erro_aproximado < tol): # estrutura de seleção, a condição será verdadeira se erro_aproximado for menor que a variável tol
    print("O erro aproximado é: {:.2f}%".format(erro_aproximado * 100)) # mostra a saída do erro_aproximado em porcentagem formatado para duas casas decimais
    print("O valor de x1 é: {:.6f}".format(x1)) # mostra a saída da variável x1 formatado para 6 casas decimais após a vírgula
    break # break é usado para sair de todas as estruturas do código
  elif(iter == max_iter-1): # estrutura de seleção, caso a primeira condícional não for verdadeira essa será checada, será verdadeiro se iter for igual a max_iter - 1
    print("Não foi encontrada uma raiz dentro dos critérios definidos") # saída informando que não foi encontrada uma raiz dentro dos critérios definidos
    break # break é usado para sair de todas as estruturas do código

  x0 = x1 # o valor da variável x0 será atualizado para o valor de x1
  x1 = funcao(x0) # o valor da variável x1 será o resultado da função definida com o x0 de parâmetro
  iter += 1 # a variável iter será incrementada em um