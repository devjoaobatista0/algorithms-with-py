"""
             entrada          saida
dados 1   0      0     1        0 
dados 2   1      1     1        1 
dados 3   1      0     1        1 
dados 4   0      1     1        0 

dados?    1      0     0        ?

TODAS AS SAIDAS É IGUAL AO PRIMEIRO NUMEROR DA ENTRADA.

"""


import numpy as np

#MATRIZ COM AS ENTRADAS.
treinamento_entrada = np.array([[0, 0, 1],
                                [1, 1, 1],
                                [1, 0, 1],
                                [0, 1, 1],])

#RESULTADO DE CADA ENTRADA
treinamento_resultado = np.array([[0, 1, 1, 0]]).T

#multiplica cada número aleatório por 2 e, em seguida, subtrai 1. Isso resulta em números aleatórios que variam entre -1 e 1.
weights= 2 * np.random.random((3,1)) - 1

#FUNCAO SIGMOID
# a funcao de ativacao serve para restrigir a amplitude da saída de um neurônio a um valor finito.
def sigmoid(x):
  return 1/(1 + np.exp(-x))

#DERIVADA DA FUNCAO SIGMOID PARA AJUSTE.
# a derivada de uma função descreve como essa função está mudando em relação à sua variável independente, geralmente em probabilidade.
def sigmoid_derivate(output):
    return output * (1 - output)

for i in range(10000):
    input_layer = treinamento_entrada
    #NP.DOT MESCLA CADA ENTRADA COM SEU WEIGHT
    output = sigmoid(np.dot(input_layer, weights))
    erro = treinamento_resultado - output
    ajuste = erro * sigmoid_derivate(output)
    # AQUI O INPUT LAYER(MATRIZ) ESTA COM A TRANSPOSTA, PORQUE EXISTE REGRAS DE MULTIPLICAÇÃO ENTRE MATRIZES 
    # E TRANSPOSTA NOS AJUDA NISSO.
    weights += np.dot(input_layer.T, ajuste)
    
    
print(output)