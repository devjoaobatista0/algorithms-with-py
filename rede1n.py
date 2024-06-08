# REDE NEURAL COM 1 NEURONIO


import math


input = 1
output_desire = 0
input_weight = 0.5
learning_rate = 0.10


#FUNCAO DE ATIVAÇAO
def activation(sum):  #FUNCAO DEGRAU.
    if sum >= 0:
        return 1 
    else:
        return 0    
     
print("entrada", input, "desejado", output_desire)

error = math.inf #COMEÇANDO COM O ERRO INFINITO.

iteration = 0

bias = 1 #FUNCIONA COMO UM NEURONIO VIRTUAL, AJUDA A AJUSTAR A INTERCEPTAÇÃO DA FUNCAO DE ATIVAÇÃO.  
bias_weight = 0.5

while not error == 0:
    iteration +=1
    
    print('########### Iteracao: ', iteration)
    print(f'peso {input_weight:.2f} ')
    sum = (input * input_weight) + (bias * bias_weight)

    output = activation(sum)

    print("saida", output)

    error = output_desire - output

    print("erro", error)


    # APRENDENDO
    if not error == 0:  #SAIDA DESEJADA == 0
        input_weight = input_weight + learning_rate * input * error  
        bias_weight = bias_weight + learning_rate * bias * error

print('PARABENS!! A REDE APRENDEU.')

