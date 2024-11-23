'''Autor: Allan Machado Gonçalves
   Matrícula: 134496
   Disciplina: Cálculo Numérico Computacional

   Resumo do método: A Regra do Trapézio é um método numérico para aproximar o valor de uma integral definida. Ela divide o intervalo de integração em 
   subintervalos e aproxima a área sob a curva como uma soma de trapézios. A fórmula utiliza a média das áreas das bases do trapézio e a altura, que é 
   o tamanho do subintervalo. É especialmente útil quando a função não tem uma primitiva simples ou quando se busca uma solução aproximada.
'''

def f(x): # definindo a f(x) a ser integrada
  return 0.2 + 25*x - 200*(x ** 2) + 675*(x ** 3) - 900*(x ** 4) + 400*(x ** 5) # retorna o valor da f(x)

a = 0 # variável a indica o início do intevalo de integração
b = 0.8 # variável b indica o final do intevalo de integração
n = 10 # número de subintervalos
h = (b - a)/n # calculando o tamanho de cada subintervalo
soma = f(a) + f(b) # soma dos valores da função nos pontos extremos

for i in range(1, n): # itera sobre os subintervalos intermediários
  xi = a + i * h # calcula o ponto intermediário xi
  soma += 2 * f(xi) # # Adiciona o dobro do valor de f(xi) à soma

i = (h / 2) * soma # calculando a integral aproximada usando a fórmula do trapézio 
print(f"{i:.6f}") # imprime o resultado formatado com 6 casas decimais