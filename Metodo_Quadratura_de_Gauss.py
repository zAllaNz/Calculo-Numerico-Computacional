'''Autor: Allan Machado Gonçalves
   Matrícula: 134496
   Disciplina: Cálculo Numérico Computacional

   Resumo do método: A quadratura de Gauss é um método numérico eficiente para calcular aproximações de integrais definidas. Utilizando pontos e 
   pesos específicos baseados nos polinômios de Legendre, ela maximiza a precisão para polinômios de grau elevado. A quadratura de Gauss ajusta 
   esses pontos e pesos ao intervalo de integração para obter a integral aproximada com alta exatidão.
'''

import numpy as np # importando a biblioteca numpy

def f(x): # definindo a f(x) a ser integrada
  return 0.2 + 25*x - 200*(x ** 2) + 675*(x ** 3) - 900*(x ** 4) + 400*(x ** 5) # retorna o valor da f(x)

a = 0 # variável a indica o início do intevalo de integração
b = 0.8 # variável b indica o final do intevalo de integração
n = 4 # número de subintervalos
x, c = np.polynomial.legendre.leggauss(n) # pegando os valores das abscissas (x) e dos pesos (c).
x_t = [0] * n  # inicializa uma lista para os pontos transformados
c_t = [0] * n  # inicializa uma lista para os pesos ajustados
soma = 0 # inicializa a soma
for i in range(n): # itera sobre cada ponto e peso da quadratura de Gauss
  x_t[i] = ((b + a) + (b - a) * x[i])/2 # transforma o ponto x[i] para o intervalo [a, b]
  c_t[i] = (b - a)/2 * c[i] # ajusta o peso c[i] para o intervalo [a, b]
  soma += c_t[i] * f(x_t[i])  # soma cada ponto na integral aproximada

integral_aproximada = soma # o valor da integral aproximada é a soma final
print(f"{integral_aproximada:.6f}") # imprime o resultado formatado com 6 casas decimais
