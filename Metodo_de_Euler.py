'''Autor: Allan Machado Gonçalves
   Matrícula: 134496
   Disciplina: Cálculo Numérico Computacional

   Resumo do método: O Método de Euler é uma técnica para resolver equações diferenciais aproximadas. Ele usa a fórmula yi+1 = yi + h * f(xi, yi)
   onde h é o tamanho do passo e f é a derivada da função. O método avança em pequenos passos, atualizando o valor de y com base na derivada.
   É simples, mas pode ser impreciso para grandes passos ou funções complexas.
'''

import numpy as np # importando a biblioteca numpy
import matplotlib.pyplot as plt # Importando a biblioteca matplot.lib

def f(x, y): # definindo a f(x) a ser integrada
  return -2*(x ** 3) + 12*(x ** 2) - 20*x + 8.5 # retorna o valor da f(x)

def eq_exata(x): # definindo a solução exata
  return (-0.5 * x**4) + (4 * x**3) - (10 * x**2) + (8.5 * x) + 1 # retorna o valor da equação exata

def erro_relativo_percentual(y_vdd, y_euler): # Função para calcular o erro relativo percentual
  return (abs((y_vdd - y_euler)/y_vdd)) * 100 # retona o valor do erro relativo percentual

a = 0 # variável a indica o início do intevalo de integração
b = 4 # variável b indica o final do intevalo de integração
h = 0.5  # tamanho do passo
n = int((b - a)/h) # número de subintervalos
x0 = 0 # condição inicial de x0
y0 = 1 # condição inicial de y0
lista_x = [0] * (n+1) # criando uma lista com tamanho n+1 para guardar os valores de x
lista_y = [0] * (n+1) # criando uma lista com tamanho n+1 para guardar os valores de y
y_vdd = []
lista_x[0] = x0 # inicializa o primeiro valor de x
lista_y[0] = y0 # inicializa o primeiro valor de y

for i in range(n): # loop para iterar em cada intervalo
  lista_y[i+1] = lista_y[i] + (h * (f(lista_x[i], lista_y[i]))) # calcula o próximo valor de y usando o método de Euler
  lista_x[i+1] = lista_x[i] + h  # calcula o próximo valor de x

for i in range(n+1): # itera sobre todos os pontos calculados
    y_vdd.append(eq_exata(lista_x[i]))  # calcula o valor exato de y para o valor atual de x
    erro_rp = erro_relativo_percentual(y_vdd[i], lista_y[i])  # calcula o erro relativo percentual entre o valor exato e o valor aproximado
    print(f"{i}: Y Verdadeiro: {y_vdd[i]:.6f}, Y Euler: {lista_y[i]:.6f}, Erro Relativo Percentual: {erro_rp:.6f}%")  # imprime o índice, valor verdadeiro, valor aproximado e erro relativo percentual
  
plt.plot(lista_x, lista_y, label='Solução Aproximada (Euler)', marker='o')  # plotando a solução aproximada
plt.plot(lista_x, y_vdd, label='Solução Exata', marker='o')  # plotando a solução exata
plt.title("Comparação da Solução Aproximada e Exata") # título do gráfico
plt.legend() # legenda do gráfico
plt.grid(True) # ativa a grid do gráfico
plt.show() # exibe o gráfico