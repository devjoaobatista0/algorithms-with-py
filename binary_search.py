
quantidade_numeros = int(input('Digite quantos numeros quer em sua lista: '))   
minha_lista = []
for i in range(0,quantidade_numeros):
    minha_lista.append(i)


numero_escolhido = int(input('Pesquisa Binaria! Digite um numero para fazermos a pesquisa binaria na lista e mostrar quantas etapas demoramos pra achar: '))

def pesquisa_binaria(lista, item):
    contador_etapas = 0 #DECLARANDO A VARIAVEL CONTADOR ETAPAS COMO GLOBAL DENTRO DA FUNÇÃO PARA PODER MODIFICA-LA
    baixo = 0  
    alto = len(lista) - 1 
    
    while baixo <= alto:
        meio = int((baixo + alto) / 2)
        chute = lista[meio]

        if chute == item:
            print(f'Voce achou o item! precisou de {contador_etapas} etapas para encontrar!')
            return meio
        contador_etapas +=1
            
        if chute  > item:
            alto = meio -1
        else:
            baixo = meio + 1

    print('O item nao esta na lista')
    return None

   


#pesquisa_binaria(minha_lista, 3)
pesquisa_binaria(minha_lista, numero_escolhido)



# A BINARY_SEARCH SO FUNCIONA EM LISTAS ORDENADAS.


