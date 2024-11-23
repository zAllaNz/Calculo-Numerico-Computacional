'''Autor: Allan Machado Gonçalves
   Matrícula: 134496
   Disciplina: Cálculo Numérico Computacional

   Resumo do método: A Regra 1/3 de Simpson é um método numérico para aproximação de integrais definidas. Ela utiliza uma parabólica (polinômio de 
   segundo grau) para aproximar a função integranda em cada par de subintervalos. O método divide o intervalo de integração em subintervalos pares, 
   calculando a integral aproximada com base nos valores da função nos pontos extremos e nos pontos intermediários.
'''

def f(x): # definindo a f(x) a ser integrada
  return 0.2 + 25*x - 200*(x ** 2) + 675*(x ** 3) - 900*(x ** 4) + 400*(x ** 5) # retorna o valor da f(x)

a = 0 # variável a indica o início do intevalo de integração
b = 0.8 # variável b indica o final do intevalo de integração
n = 4 # número de subintervalos
h = (b - a)/n # calculando o tamanho de cada subintervalo
soma_pares = 0 # soma dos valores da função nos pontos pares
soma_impares = 0 # soma dos valores da função nos pontos ímpares

for i in range(1, n): # laço de repetição, pula o primeiro e último ponto
  if(i % 2 == 0): # se o resto de divisão de i por 2 for igual a zero, então i é par
    soma_pares += f(a + i * h) # adiciona o valor de f(xi) à soma dos pares
  else: # caso seja impar
    soma_impares += f(a + i * h) # adiciona o valor de f(xi) à soma dos ímpares

i = (h/3) * (f(a) + 4 * soma_impares + 2 * soma_pares + f(b)) # calcula a integral aproximada usando a Regra de Simpson
print(f"{i:.6f}") # imprime o resultado formatado com 6 casas decimais