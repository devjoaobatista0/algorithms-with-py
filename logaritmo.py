import math

def log_pesquina_binaria(numero):

    if numero <= 0:
        return float('nan')
    
    
    print(numero)
    return math.log2(numero)
    

numero_Comprimento = int(input('Digite o comprimento da lista que deseja saber o numero maximo de estapas para se achar em uma pesquisa binaria: '))

resultado = log_pesquina_binaria(numero_Comprimento)

print(f'O total de etapas é: {resultado}')
